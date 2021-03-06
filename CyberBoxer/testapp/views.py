from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, FormView, TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from testapp.models import Item
from testapp.forms import Registration
from django.contrib.auth.models import User
# Create your views here.
class List_view(ListView):
    model = Item
    template_name="testapp/list.html"
    context_object_name= "Item_list"

class Detail_view(DetailView):
    model =Item
    template_name="testapp/detail.html"

class Sign(CreateView):
   template_name='testapp/registration.html'
   form_class=UserCreationForm
   success_url="/accounts/login"
def Logout(request):
    return render(request,"testapp/logout.html")
