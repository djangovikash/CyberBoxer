from django.shortcuts import render
from django.views.generic import ListView,DetailView
from testapp.models import Item
# Create your views here.
class List_view(ListView):
    model = Item
    template_name="testapp/list.html"
    context_object_name= "Item_list"

class Detail_view(DetailView):
    model =Item
    template_name="testapp/detail.html"
