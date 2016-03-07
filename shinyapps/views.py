from django.http import HttpResponse
from django.shortcuts import render

def shiny_page(request):
    if request.method == 'POST':
        if request.POST.get('username','') == 'langestrst01':
            return render(request, 'shiny_home.html', {
                'new_shinyapp': 'Movie Explorer',
            })
        elif request.POST.get('username','') == 'ruser':
            return render(request, 'shiny_home.html', {
                'new_shinyapp': 'Hello App',
            })
    return render(request, 'shiny_home.html')
