from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer

class CustomerCreationForm(UserCreationForm):
    class Meta :
        model = Customer
        fields = UserCreationForm.Meta.fields + ("age",)

class CustomerChangeForm(UserChangeForm):
    class Meta :
        model = Customer
        fields = UserChangeForm.Meta.fields