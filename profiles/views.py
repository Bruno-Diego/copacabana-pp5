from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, PurchasedProduct
from .forms import UserProfileForm

from checkout.models import Order, OrderLineItem


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please \
                ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    purchases = PurchasedProduct.objects.filter(user_profile=profile)
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'purchases': purchases,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def add_to_purchased(request, order_id, PurchasedForm):
    profile = get_object_or_404(UserProfile, user=request.user)
    line_item = OrderLineItem.objects.filter(order_id=order_id)
    purchased_list = PurchasedProduct.objects.filter(user_profile=profile)
    for product in line_item:
        form = PurchasedForm()
        if request.method == 'POST':
            if PurchasedProduct.objects.filter(product_name=product.product.name).exists():
                continue
            else:
                purchased_product = form.save(commit=False)
                purchased_product.user_profile = profile
                purchased_product.product = product.product
                purchased_product.product_name = product.product.name
                purchased_product.product_size = product.product_size
                purchased_product.save()
        else:
            return print('Failed to add product')
    return print('Purchase completed!')
