from django.views.generic import ListView , DetailView
from .models import  coffee
# Create your views here.

class CoffeeList(ListView):
    model = coffee
    template_name = 'home.html'
    context_object_name = 'coffee_list_all'

class CoffeeDetail(DetailView):
    model = coffee
    template_name = 'coffee_detail.html'