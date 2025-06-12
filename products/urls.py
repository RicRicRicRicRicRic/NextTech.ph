# products/urls.py
from django.urls import path
from . import views 

app_name = 'products'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('list/', views.product_list, name='product_list'),
    path('detail/<int:pk>/', views.product_detail, name='product_detail'),
]
