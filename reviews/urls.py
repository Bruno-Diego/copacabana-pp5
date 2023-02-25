from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:product_id>/review/',
         views.add_review, name='add_review'),
]
