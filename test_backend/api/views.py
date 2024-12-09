from django.shortcuts import render
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from .models  import *
from .serializer import *
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from treebeard.mp_tree import MP_NodeQuerySet



class TreeViewsSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitPostSeriliazer

    def get_tree_by_unit(self,unit:Unit):
        return {
            'id':unit.pk,
            'name': unit.name,
            # 'type':unit.type,
            'children': [self.get_tree_by_unit(child) for child in unit.children.all()]
        }
    @action(methods=['GET'],detail=False)
    def get_units_tree(self,request:Response):
        root = Unit.objects.get(parent=None)
        tree = self.get_tree_by_unit(root)
        return Response(tree,status=HTTP_200_OK)


# class UnitViewSet(viewsets.ModelViewSet):
#     queryset = Unit.objects.all()
#     serializer_class = TreeBeardSeriliale


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



