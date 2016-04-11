from django.contrib.auth.views import logout
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.user_login, name='login'),
    url(r'^logout$', logout, {'next_page': '/'},name='logout'),
]