from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('product_upload/', views.upload_laptop, name='upload_laptop'),
]