from django.urls import path
from . import views
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    url('^test/', csrf_exempt(views.XmlTest))
    ]
