from django.shortcuts import render
from .models import ShinyGroup, ShinyItem
from setup_db import save_selected_group, get_selected_item

def shiny_page(request):
    if request.method == 'POST':
        save_selected_group(ShinyGroup,request.POST.get('username',''),selected_status=True)
        new_item = get_selected_item(ShinyItem,ShinyGroup)
        return render(request, 'shiny_home.html', {
            'shinyapp_id': new_item.itemid,
            'username': new_item.group.username,
            'shinyapp_dirname': new_item.dirname,
            'shinyapp_name': new_item.name,
        })
    return render(request, 'shiny_home.html')
