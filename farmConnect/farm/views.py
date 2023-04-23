from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Commodity

def is_member(user):
    return user.groups.filter(name='farmers').exists()

@user_passes_test(is_member)
def index(request):
    return render(request, 'farm.html')


@user_passes_test(is_member)
def commodity_list(request):
    commodities = Commodity.objects.all()
    return render(request, 'commodity_list.html', {'commodities': commodities})

@user_passes_test(is_member)
def commodity_add(request):
    if request.method == 'POST':
        commodities = ['wheat', 'crackedWheat', 'corn', 'barley', 'semolina', 'rice', 'oats', 'pearlMillet', 'greenGram', 'sorghum']
        for i in commodities:
            if i in request.POST:
                farmer = request.user
                price = request.POST[i+'1']
                quantity = request.POST[i+'2']
                commodity = Commodity(farmer=farmer, name=i, price=price, quantity=quantity)
                commodity.save()
        return redirect(reverse('commodity_list'))
    else:
        return render(request, 'commodity_add.html')