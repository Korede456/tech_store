from django.shortcuts import get_object_or_404
from store.models import Cart, CartItem, Laptop


class CartManager:
    def __init__(self, user):
        self.user = user
        self.cart, created = Cart.objects.get_or_create(user=user)

    def add_to_cart(self, laptop_id):
        """Adds a laptop to the cart or increases quantity if already added."""
        laptop = get_object_or_404(Laptop, id=laptop_id)
        cart_item, created = CartItem.objects.get_or_create(
            cart=self.cart, laptop=laptop
        )

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
