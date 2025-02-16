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
)

app_name = "store"

urlpatterns = [
    path("", laptop_list, name="laptop_list"),
    path("<int:pk>/", laptop_detail, name="laptop_detail"),
    path("add/", laptop_create, name="laptop_create"),
    path("<int:pk>/edit/", laptop_update, name="laptop_update"),
    path("<int:pk>/delete/", laptop_delete, name="laptop_delete"),
    path("cart/", cart_view, name="cart_view"),
    path("cart/add/<int:laptop_id>/", add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:item_id>/", remove_from_cart, name="remove_from_cart"),
    path(
        "cart/update/<int:item_id>/<str:action>/",
        update_cart_item_quantity,
        name="update_cart_item_quantity",
    ),
]
