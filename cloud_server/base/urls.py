from django.urls import path
from . import views

app_name = 'base'

# URLConf
urlpatterns = [
    path('server', views.server, name='server'),
]