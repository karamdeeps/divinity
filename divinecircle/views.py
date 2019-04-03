from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from divinecircle.serializers import UserSerializer, GroupSerializer
from django.template.loader import get_template
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
