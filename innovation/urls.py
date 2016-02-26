from django.conf.urls import include, url
from django.contrib import admin

from homepage import views as home_views
from shinyapps import views as shiny_views

urlpatterns = [
    url(r'^$', home_views.home_page, name='home'),
    url(r'^shinyapps$', shiny_views.shiny_page, name='shiny_home'),
    url(r'^admin/', include(admin.site.urls)),
]
