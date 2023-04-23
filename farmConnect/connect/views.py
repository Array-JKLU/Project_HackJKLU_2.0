from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from .models import Item
from farm.models import Commodity

def is_member(user):
    return user.groups.filter(name='consumers').exists()

@user_passes_test(is_member)
def index(request):
    query = '''SELECT t.id, t.name, t.price, t.quantity FROM (
        SELECT t.*, row_number() OVER (
        PARTITION BY name ORDER BY price DESC, quantity DESC
        ) AS seqnum FROM farm_commodity t)
        t WHERE seqnum = 1;'''
    commodities = Commodity.objects.raw(query)
    return render(request, 'connect.html', {'commodities': commodities})

@user_passes_test(is_member)
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})