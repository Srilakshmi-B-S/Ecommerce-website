from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('buy/<int:product_id>/', views.delivery_details, name='delivery_details'),
   path('payment/<int:delivery_id>/', views.payment, name='payment'),
    path('confirmation/<int:delivery_id>/', views.confirmation, name='confirmation'),
]