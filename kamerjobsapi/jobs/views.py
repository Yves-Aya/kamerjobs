from django.shortcuts import render
from rest_framework import viewsets
from jobs.serializers import jobTitleSerializer,newJobSerializer
from jobs.models import jobTitle,newJob
from jobs.permissions import IsAdminUserOrReadOnly



class jobTitleViewSet(viewsets.ModelViewSet):
   queryset = jobTitle.objects.all() 
   serializer_class = jobTitleSerializer

class newJobViewSet(viewsets.ModelViewSet):
   queryset = newJob.objects.all() 
   serializer_class = newJobSerializer 
   permission_classes = [IsAdminUserOrReadOnly]

