from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_order, name='add_order'),
    path('list/', views.list_orders, name='list_orders'),
    path('delete/<int:order_id>/', views.delete_order, name='delete_order'),


]
