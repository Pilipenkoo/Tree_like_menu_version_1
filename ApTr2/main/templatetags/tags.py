from django import template
from main.models import MenuItem
from django.template.loader import render_to_string

register = template.Library()

def get_child_menu_items(menu_item):
    children = menu_item.children.all()
    all_children = list(children)
    for child in children:
        all_children.extend(get_child_menu_items(child))
    return all_children
    

@register.simple_tag(takes_context=True)
def draw_menu(context,named_url):
    request = context['request']
    url = request.build_absolute_uri()

    menu_items = MenuItem.objects.filter(named_url=named_url)  # Получаем основные элементы меню (верхний уровень)
    all_items = []


    
    for item in menu_items:
        all_items.append(item)

        
        item_children = get_child_menu_items(item)
        
        for children in item_children:
            all_items.append(children)

    return render_to_string('menu_paint.html',{'menu_items':all_items,'url':url})
