from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('about/', views.about, name='about'),
    path('customer/<str:pk>', views.customer, name='customer'),
    path('products/', views.products, name='products'),
]