from django.shortcuts import render
from api.serializers import dnaSerializer, simiosXHumanosSerializer
from rest_framework import viewsets
from .models import *


class dnaViewSet(viewsets.ModelViewSet):
    queryset = dna.objects.all()
    serializer_class = dnaSerializer


class simiosXHumanosViewSet(viewsets.ModelViewSet):
    queryset = simiosXHumanos.objects.all()
    serializer_class = simiosXHumanosSerializer
