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

def itemImage(item):
    images = {
        'Tomato': '',
        'Potato': ''
    }

@user_passes_test(is_member)
def commodity_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        
        commodity = Commodity(name=name, price=price, quantity=quantity, image=itemImage(name))
        commodity.save()
        
        return redirect(reverse('commodity_list'))
    else:
        return render(request, 'commodity_add.html')