from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user_profile', 'rating', 'date')
    list_filter = ('date', 'rating')
    search_fields = ('product__name', 'user_profile__username')
    date_hierarchy = 'date'
    ordering = ('-date',)


admin.site.register(Review, ReviewAdmin)
