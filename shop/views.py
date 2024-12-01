from django.views.generic import ListView , DetailView , UpdateView , CreateView , DeleteView
from .models import Coffee
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render
# Create your views here.





class CoffeeList(ListView):
    model = Coffee
    template_name = 'home.html'
    context_object_name = 'coffee_list_all'



class CoffeeDetail(DetailView):
    model = Coffee
    template_name = 'coffee_detail.html'


class CoffeeCreate(CreateView):
    model = Coffee
    template_name = 'new_coffee.html'
    fields = ['name','description','available','stock','price']


class CoffeeUpdate(UpdateView):
    model = Coffee
    template_name = 'update_coffee.html'
    fields = ['name','description','available','stock','price']
    success_url = reverse_lazy('home')


class CoffeeDelete(DeleteView):
    model = Coffee
    template_name = 'delete_coffee.html'
   



class SearchResulutListView(ListView):
    model = Coffee
    context_object_name = 'coffee_list'
    template_name = 'coffee/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Coffee.objects.filter(Q (name__icontains=query) | Q (price__icontains = query) | Q (description__icontains = query) | Q (id__icontains = query))



