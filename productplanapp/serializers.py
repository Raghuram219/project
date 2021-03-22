from rest_framework import serializers
from .models import Products,Plan

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'

class PlanSerializer(serializers.ModelSerializer):
    products=ProductSerializer(many=True)
    class Meta:
        model=Plan
        fields=['plan','budget','products']
        # fields='__all__'
    
    