from django.shortcuts import get_object_or_404
from store.models import Cart, CartItem, Laptop
import uuid

class CartManager:
    def __init__(self, request, user=None):
        """
        Manages cart functionality. Works for both logged-in users and guests.
        """
        self.request = request
        self.user = user
        self.cart = self.get_or_create_cart()

    def get_or_create_cart(self):
        """
        Retrieves an existing cart or creates a new one.
        - If a user is logged in, it fetches their cart or creates one.
        - If not logged in, it creates a session-based cart.
        """
        cart = None

        # Check if user is logged in
        if self.user and self.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=self.user)
            self.request.session["cart_id"] = str(cart.id)  # Store cart in session
        else:
            cart_id = self.request.session.get("cart_id")
            if cart_id:
                try:
                    cart = Cart.objects.get(id=cart_id)
                except Cart.DoesNotExist:
                    cart = None

            # Create a new session cart if none exists
            if not cart:
                cart = Cart.objects.create(id=uuid.uuid4())  # Generate new UUID
                self.request.session["cart_id"] = str(cart.id)  # Store in session

        return cart

    def add_to_cart(self, laptop_id):
        """Adds a laptop to the cart or increases quantity if already added."""
        laptop = get_object_or_404(Laptop, id=laptop_id)
        cart_item, created = CartItem.objects.get_or_create(cart=self.cart, laptop=laptop)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return cart_item

    def remove_from_cart(self, item_id):
        """Removes a specific item from the cart."""
        cart_item = get_object_or_404(CartItem, id=item_id, cart=self.cart)
        cart_item.delete()

    def update_cart_item_quantity(self, item_id, action):
        """Updates the quantity of a cart item (increase or decrease)."""
        cart_item = get_object_or_404(CartItem, id=item_id, cart=self.cart)
        if action == "increase":
            cart_item.quantity += 1
        elif action == "decrease" and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()

    def get_cart_items(self):
        """Returns all items in the cart."""
        return self.cart.items.all()

    def get_total_price(self):
        """Calculates the total price of items in the cart."""
        return sum(item.total_price() for item in self.get_cart_items())

    def clear_cart(self):
        """Clears all items from the cart."""
        self.cart.items.all().delete()
