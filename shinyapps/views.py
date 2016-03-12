from django.shortcuts import render
from .models import ShinyGroup, ShinyItem
from setup_db import save_selected_group

def shiny_page(request):
    if request.method == 'POST':
        save_selected_group(ShinyGroup,request.POST.get('username',''),selected_status=True)
        group_ = ShinyGroup.objects.get(selected=True)
        return render(request, 'shiny_home.html', {
            'items': ShinyItem.objects.filter(group=group_),
            'username': group_.username,
        })
    return render(request, 'shiny_home.html')
