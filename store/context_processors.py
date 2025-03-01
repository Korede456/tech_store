from .models import Cart

def cart_count(request):
    """Context processor to add cart count to all templates."""
    cart_count = 0
    cart_id = request.session.get("cart_id")

    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
            cart_count = cart.item_count()
        except Cart.DoesNotExist:
            cart_count = 0

    return {"cart_count": cart_count}
