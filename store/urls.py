from django.urls import path
from .views import (
    laptop_list, laptop_detail, laptop_create, laptop_update, laptop_delete
)

app_name = 'store'

urlpatterns = [
    path("", laptop_list, name="laptop_list"),
    path("<int:pk>/", laptop_detail, name="laptop_detail"),
    path("add/", laptop_create, name="laptop_create"),
    path("<int:pk>/edit/", laptop_update, name="laptop_update"),
    path("<int:pk>/delete/", laptop_delete, name="laptop_delete"),
]
