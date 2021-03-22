from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlanSerializer,ProductSerializer
from.models import Plan,Products

class Plan(viewsets.ModelViewSet):
    serializer_class=PlanSerializer
    queryset=Plan.objects.all()

class Products(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Products.objects.all()