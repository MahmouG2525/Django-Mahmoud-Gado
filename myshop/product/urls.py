from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('list/', views.product_list, name='product_list'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),

]
