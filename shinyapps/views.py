from django.shortcuts import render

def shiny_page(request):
    return render(request, 'shiny_home.html')
