from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('account/', views.commodity_list, name='commodity_list'),
    path('add/', views.commodity_add, name='commodity_add'),
]