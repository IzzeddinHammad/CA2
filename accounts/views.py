from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from .forms import CustomerCreationForm
from .models import Customer


class SignUpView(CreateView):
    model = Customer
    form_class = CustomerCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # new user saved here
        response = super().form_valid(form)

        #cutomer added to group here
        customer_group, created = Group.objects.get_or_create(name='Customer')
        self.object.groups.add(customer_group)

        #post signup login
        login(self.request, self.object)
        return response # Redirect to success URL