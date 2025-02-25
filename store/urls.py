from django.urls import path
from .views import (
    laptop_list,
    laptop_detail,
    laptop_create,
    laptop_update,
    laptop_delete,
    cart_view,
    add_to_cart,
    remove_from_cart,
    update_cart_item_quantity,
    checkout,
    delivery_info,
    paystack_callback,
    paystack_payment,
    order_detail,
    order_list,
)

app_name = "store"

urlpatterns = [
    path("", laptop_list, name="laptop_list"),
    path("<uuid:pk>/", laptop_detail, name="laptop_detail"),
    path("add/", laptop_create, name="laptop_create"),
    path("<uuid:pk>/edit/", laptop_update, name="laptop_update"),
    path("<uuid:pk>/delete/", laptop_delete, name="laptop_delete"),
    path("cart/", cart_view, name="cart_view"),
    path("cart/add/<uuid:laptop_id>/", add_to_cart, name="add_to_cart"),
    path("cart/remove/<uuid:item_id>/", remove_from_cart, name="remove_from_cart"),
    path(
        "cart/update/<uuid:item_id>/<str:action>/",
        update_cart_item_quantity,
        name="update_cart_item_quantity",
    ),
    path('delivery/', delivery_info, name='delivery_info'),
    path('checkout/', checkout, name='checkout'),
    path("paystack/<uuid:order_id>/", paystack_payment, name="paystack_payment"),
    path("paystack/callback/", paystack_callback, name="paystack_callback"),
    path("order/<uuid:order_id>/", order_detail, name="order_detail"),
    path("orders/", order_list, name="orders"),
]
