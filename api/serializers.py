from .models import *
from rest_framework import serializers


class dnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = dna
        fields = ['id', 'dna']


class simiosXHumanosSerializer(serializers.ModelSerializer):
    class Meta:
        model = simiosXHumanos
        fields = ['id', 'simios', 'humanos', 'ratio']



