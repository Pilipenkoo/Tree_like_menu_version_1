from django.urls import path
from .views import menu_view



urlpatterns = [
    path('<slug:url_menu>/',menu_view, name ='menu'),
    path('',menu_view, name ='menu_all'),
]