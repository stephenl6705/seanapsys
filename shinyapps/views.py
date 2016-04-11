from django.shortcuts import render
from shinyapps.models import ShinyGroup, ShinyItem
from setup_db import save_selected_group

def shiny_page(request):
    if request.user.is_authenticated():
        found = save_selected_group(ShinyGroup,request.user.username,selected_status=True)
        if found:
            group_ = ShinyGroup.objects.get(selected=True)
            return render(request, 'shiny_home.html', {
                'items': ShinyItem.objects.filter(group=group_),
                'username': group_.username,
            })
    return render(request, 'shiny_home.html')
    #return HttpResponseRedirect(reverse('error'))
