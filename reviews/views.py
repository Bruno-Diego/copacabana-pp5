from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product_title = product
            review.user_profile = user
            review.save()
            messages.success(request, 'Your review has been added.')
            return HttpResponseRedirect(reverse('product_detail',
                                                args=[product_id]))
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {'form': form, 'product': product}
    return render(request, template, context)
