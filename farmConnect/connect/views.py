from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Item
from farm.models import Commodity

def is_member(user):
    return user.groups.filter(name='consumers').exists()

@user_passes_test(is_member)
def index(request):
    return render(request, 'connect.html')

@user_passes_test(is_member)
def item_buy(request):
    query = '''SELECT t.id, t.name, t.price, t.quantity FROM (
        SELECT t.*, row_number() OVER (
        PARTITION BY name ORDER BY price DESC, quantity DESC
        ) AS seqnum FROM farm_commodity t)
        t WHERE seqnum = 1;'''
    commodities = Commodity.objects.raw(query)
    if request.method == 'POST':
        items = ['wheat', 'crackedWheat', 'corn', 'barley', 'semolina', 'rice', 'oats', 'pearlMillet', 'greenGram', 'sorghum']
        for i in items:
            if i in request.POST:
                quantity = request.POST[i+'2']
                # commodity = Commodity.objects.filter(name=i, quantity=quantity)
                # commodity.delete()
        return redirect(reverse('item_list'))
    else:
        return render(request, 'item_buy.html', {'commodities': commodities})

@user_passes_test(is_member)
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})