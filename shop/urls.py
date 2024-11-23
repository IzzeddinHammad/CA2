from django.urls import path
from .views import CoffeeList , CoffeeDetail,CoffeeCreate,CoffeeUpdate,CoffeeDelete , SearchResulutListView

urlpatterns = [
    path('',CoffeeList.as_view(),name='home'),
    path('Coffee/<uuid:pk>/',CoffeeDetail.as_view(),name='coffee_detail'),
    path('Coffee/new/',CoffeeCreate.as_view(),name='new_coffee'),
    path('Coffee/<uuid:pk>/Update/',CoffeeUpdate.as_view(),name='coffee_update'),
    path('Coffee/<uuid:pk>/Delete/',CoffeeDelete.as_view(),name='delete_coffee'),
    path('search/', SearchResulutListView.as_view(),name='search_results'),
]