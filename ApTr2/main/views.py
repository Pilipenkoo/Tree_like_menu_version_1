from django.shortcuts import render
from main.models import MenuItem
# Create your views here.

def home(request):
    return render (request,'main.html')


def menu_view(request,url_menu=None):
    if url_menu:
        url_menu = request.build_absolute_uri()
        menu_items = MenuItem.objects.filter(url = url_menu)
    else:
        menu_items = MenuItem.objects.all()
    return render (request, 'menu.html',{'menu_items':menu_items,'url':url_menu})
