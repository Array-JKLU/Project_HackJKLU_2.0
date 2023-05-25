from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("buy/", views.item_buy, name="buy"),
    path("items/", views.item_list, name="items")
]