from django.urls import path
from . import views

app_name = 'base'

# URLConf
urlpatterns = [
    path('', views.landing, name='landing'),
    path('home', views.home, name='home'),
    path('questionaire', views.questionaire, name='questionaire'),
]