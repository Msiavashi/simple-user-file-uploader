from django.shortcuts import render
from .models import Template 
from .serializers import TemplateSerializer 
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from users.models import User
from rest_framework.renderers import JSONRenderer

# Create your views here.

class TemplateAPI(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        print(request.user)
        print(request.data)
        request.data['owner'] = User.objects.get(email=request.user).id
        file_serializer = TemplateSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        templates = Template.objects.filter(owner=User.objects.get(email=request.user))
        serialized = TemplateSerializer(templates, many=True)
        return Response(serialized.data)

class TemplateDelete(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, tid):
        print ("salam")
        Template.objects.get(pk=tid).delete()
        return Response(data="deleted", status=status.HTTP_200_OK)