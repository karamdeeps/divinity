from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from divinecircle.serializers import UserSerializer, GroupSerializer
from django.template.loader import get_template
from django.http import HttpResponse

from rest_framework_xml.parsers import XMLParser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Testing for xml parser
class XmlTest(APIView):
    parser_classes = XMLParser
    authentication_classes = []

    def post(self, request, format=None):
        print("ok-------------------")
        return Response('xs')
