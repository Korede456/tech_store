from .models import CartItem, Cart

def cart_count(request):
    """Context processor to add cart count to all templates."""
    cart_count = 0
    cart_id = request.session.get("cart_id")  # Get cart ID from session
    
    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
            cart_count = CartItem.objects.filter(cart=cart).count()
        except Cart.DoesNotExist:
            cart_count = 0
    
    return {"cart_count": cart_count}
