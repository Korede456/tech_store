from django.shortcuts import render, get_object_or_404, redirect
from .models import Laptop
from .forms import LaptopForm, AddressForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Laptop, Order, OrderItem, Cart, Address
from .utils.cart import CartManager
from django.http import JsonResponse



def laptop_list(request):
    query = request.GET.get("q")
    brand_filter = request.GET.get("brand")
    condition_filter = request.GET.get("condition")

    laptops = Laptop.objects.all()

    if query:
        laptops = laptops.filter(model__icontains=query)

    if brand_filter:
        laptops = laptops.filter(brand=brand_filter)

    if condition_filter:
        laptops = laptops.filter(condition=condition_filter)

    brands = Laptop.objects.values_list("brand", flat=True).distinct()
    conditions = Laptop.objects.values_list("condition", flat=True).distinct()

    return render(
        request,
        "store/laptop_list.html",
        {"laptops": laptops, "brands": brands, "conditions": conditions},
    )


def laptop_detail(request, pk):
    laptop = get_object_or_404(Laptop, id=pk)

    # Collect all image fields dynamically
    laptop_images = [
        getattr(laptop, f"img_{i}") for i in range(1, 7) if getattr(laptop, f"img_{i}")
    ]

    # Get similar products
    similer_laptops = (
        Laptop.objects.filter(processor=laptop.processor, ram=laptop.ram)
        .exclude(id=pk)
        .order_by("?")[:4]
    )

    return render(
        request,
        "store/laptop_detail.html",
        {
            "laptop": laptop,
            "laptop_images": laptop_images,
            "similer_products": similer_laptops,
        },
    )


def laptop_create(request):
    if request.method == "POST":
        form = LaptopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Laptop added successfully!")
            return redirect("laptop_list")
    else:
        form = LaptopForm()
    return render(request, "laptops/laptop_form.html", {"form": form})


def laptop_update(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    if request.method == "POST":
        form = LaptopForm(request.POST, request.FILES, instance=laptop)
        if form.is_valid():
            form.save()
            messages.success(request, "Laptop updated successfully!")
            return redirect("laptop_detail", pk=pk)
    else:
        form = LaptopForm(instance=laptop)
    return render(request, "laptops/laptop_form.html", {"form": form})


def laptop_delete(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    laptop.delete()
    messages.success(request, "Laptop deleted successfully!")
    return redirect("laptop_list")


@login_required
def add_to_cart(request, laptop_id):
    cart_manager = CartManager(request.user)
    cart_manager.add_to_cart(laptop_id)
    return redirect("store:laptop_list")


@login_required
def cart_view(request):
    cart_manager = CartManager(request.user)
    cart_items = cart_manager.get_cart_items()
    total_price = cart_manager.get_total_price()

    return render(
        request,
        "store/cart.html",
        {"cart_items": cart_items, "total_price": total_price},
    )


@login_required
def remove_from_cart(request, item_id):
    cart_manager = CartManager(request.user)
    cart_manager.remove_from_cart(item_id)
    return redirect("store:cart_view")


@login_required
def update_cart_item_quantity(request, item_id, action):
    cart_manager = CartManager(request.user)
    cart_manager.update_cart_item_quantity(item_id, action)
    redirect("store:cart_view")

@login_required
def delivery_info(request):
    addresses = Address.objects.filter(user=request.user)
    form = AddressForm()

    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect("store:checkout")  # Redirect to checkout page after adding address

    return render(
        request, "store/checkout.html", {"addresses": addresses, "form": form}
    )


@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    addresses = Address.objects.filter(user=request.user)
    
    if cart.items.count() == 0:
        messages.error(request, "Your cart is empty.")
        return redirect("sotre:cart_view")  # Redirect to cart page if empty

    if request.method == "POST":
        address_id = request.POST.get("address_id")
        if not address_id:
            messages.error(request, "Please select an address.")
            return redirect("store:checkout")

        address = get_object_or_404(Address, id=address_id, user=request.user)

        # Create order
        total_price = sum(item.total_price() for item in cart.items.all())
        order = Order.objects.create(user=request.user, address=address, total_price=total_price)

        # Move cart items to order items
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                laptop=item.laptop,
                quantity=item.quantity,
                price=item.laptop.price,  # Store price at time of order
            )

        # Clear cart after checkout
        cart.items.all().delete()

        return redirect("order_success", order_id=order.id)  # Redirect to success page

    return render(request, "store/checkout.html", {"cart": cart, "addresses": addresses, "form": AddressForm()})