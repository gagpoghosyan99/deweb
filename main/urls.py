from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
]


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
]


urlpatterns = [
    path('products/', views.product_list, name='product_list'),
]
