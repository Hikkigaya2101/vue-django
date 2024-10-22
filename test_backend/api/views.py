from django.shortcuts import render
from .models  import *
from .serializer import *
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from treebeard.mp_tree import MP_NodeQuerySet

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitPostSeriliazer

    def get_serializer_class(self):
         if self.request.method == 'GET':
             return UnitGetSeriliazer
         return UnitPostSeriliazer


class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerPostSeriliazer
    filter_backends = [filters.SearchFilter]
    search_fields = ['unit__id']

class UnitTypeViewSet(viewsets.ModelViewSet):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSeriliazer


