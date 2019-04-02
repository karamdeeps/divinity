from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello , World. you're at the polls index.")


def home(request):
    return render(request, 'home.html')
