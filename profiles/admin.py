from django.contrib import admin

# Register your models here.
from .models import PurchasedProduct


@admin.register(PurchasedProduct)
class PurchasedProductAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'product', 'date_purchased')
    list_filter = ('user_profile', 'product', 'date_purchased')
    search_fields = ('user_profile__username', 'product__name')
    date_hierarchy = 'date_purchased'
