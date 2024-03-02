from django.shortcuts import render
from .serializer import FrutaSerializer, QuesoSerializer
from .models import Fruta, Queso
from rest_framework import viewsets
# Create your views here.

class FrutaViewsets(viewsets.ModelViewSet):
    queryset=Fruta.objects.all()
    serializer_class=FrutaSerializer
    
class QuesoViewsets(viewsets.ModelViewSet):
    queryset=Queso.objects.all()
    serializer_class=QuesoSerializer