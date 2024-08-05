from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]