from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from order.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer