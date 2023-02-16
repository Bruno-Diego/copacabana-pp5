from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from products.models import Product
from profiles.models import UserProfile
# Create your models here.


class Review(models.Model):
    product_title = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                 MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.product_title.name} by \
            {self.user_profile.user.username}'
