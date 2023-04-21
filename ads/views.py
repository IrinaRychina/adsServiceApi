from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Ad
from .serializers import AdSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter

class AdPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AdList(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['created_at']

class AdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
