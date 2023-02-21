from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data,
         name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
    path('status/create/', views.order_status_create, name='add_status'),
    path('status/<int:pk>/update/', views.order_status_edit, name='order_status_update'),
    path('status/<int:pk>/delete/', views.order_status_delete, name='order_status_delete'),
    path('statuslist/', views.order_status_list, name='order_status_list'),
]
