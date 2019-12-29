from django.shortcuts import render
from django.views.generic import ListView
from testapp.models import Item
# Create your views here.
class List_view(ListView):
    model = Item
    template_name="testapp/list.html"
    context_object_name= "Item_list"
