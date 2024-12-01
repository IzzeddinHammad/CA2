from django.urls import path , reverse_lazy
from .views import SignUpView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = 'accounts'



urlpatterns = [

    path('create/', SignUpView.as_view(), name='signup'),
]