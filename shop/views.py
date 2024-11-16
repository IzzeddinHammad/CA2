from django.views.generic import ListView , DetailView , UpdateView , CreateView , DeleteView
from .models import  coffee
from django.urls import reverse_lazy
# Create your views here.

class CoffeeList(ListView):
    model = coffee
    template_name = 'home.html'
    context_object_name = 'coffee_list_all'



class CoffeeDetail(DetailView):
    model = coffee
    template_name = 'coffee_detail.html'


class CoffeeCreate(CreateView):
    model = coffee
    template_name = 'new_coffee.html'
    fields = ['name','description','price']


class CoffeeUpdate(UpdateView):
    model = coffee
    template_name = 'update_coffee.html'
    fields = ['price']
    success_url = reverse_lazy('home')


class CoffeeDelete(DeleteView):
    model = coffee
    template_name = 'delete_coffee.html'
    success_url = reverse_lazy('home')