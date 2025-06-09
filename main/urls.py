from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,                   name='home'),
    path('products/', views.product_list,        name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('pricing/', views.pricing,        name='pricing'),
    path('contact/', views.contact,        name='contact'),
]
