from django.urls import path , reverse_lazy
from .views import SignUpView
from django.contrib.auth import views as auth_views
app_name = 'accounts'



urlpatterns = [
    path('create/', SignUpView.as_view(), name='signup'),
]