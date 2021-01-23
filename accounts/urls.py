from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('about/', views.about, name='about'),
    path('customer/<str:pk>', views.customer, name='customer'),
    path('products/', views.products, name='products'),
    path('order/', views.order_create, name='order_create'),
    path('order/update/<str:pk>/', views.order_update, name='order_update'),
    path('order/delete/<str:pk>/', views.order_delete, name='order_delete'),
]