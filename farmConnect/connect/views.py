from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from .models import Item

def is_member(user):
    return user.groups.filter(name='consumers').exists()

@user_passes_test(is_member)
def index(request):
    return render(request, 'connect.html')

@user_passes_test(is_member)
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})