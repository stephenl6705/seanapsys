from django.http import HttpResponse
from django.shortcuts import render

def shiny_page(request):
    if request.method == 'POST':
        if request.POST.get('username','') == 'langestrst01':
            return render(request, 'shiny_home.html', {
                'shinyapp_id': 'id_shinyapp2',
                'username': 'langestrst01',
                'shinyapp_dirname': 'movie_explorer',
                'shinyapp_name': 'Movie Explorer',
            })
        elif request.POST.get('username','') == 'ruser':
            return render(request, 'shiny_home.html', {
                'shinyapp_id': 'id_shinyapp1',
                'username': 'ruser',
                'shinyapp_dirname': 'hello',
                'shinyapp_name': 'Hello App',
            })
    return render(request, 'shiny_home.html')
