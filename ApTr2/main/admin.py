from typing import Any
from django.contrib import admin
from main.models import MenuItem

# Register your models here.

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ( 'title','parent','url','named_url')
    list_filter = ['parent',]
    
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        
        provide_url = form.cleaned_data.get('url')
        
        if provide_url and provide_url.isdigit():
            obj.url = f'http://127.0.0.1:8000/menu/{provide_url}/'
        
        
        return super().save_model(request, obj, form, change)

admin.site.register(MenuItem,MenuItemAdmin)
