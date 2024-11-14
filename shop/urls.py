from django.urls import path
from .views import CoffeeList , CoffeeDetail

urlpatterns = [
    path('',CoffeeList.as_view(),name='home'),
    path('Details/<int:pk>/',CoffeeDetail.as_view(),name='coffee_detail')
]