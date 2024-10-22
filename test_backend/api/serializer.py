from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import *
from rest_framework.utils.serializer_helpers import ReturnDict

class UnitGetSeriliazer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name',read_only=True)
    class Meta:
        model = Unit
        fields = '__all__'

class UnitPostSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class UnitTypeSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = UnitType
        fields = '__all__'

class ConsumerGetSeriliazer(serializers.ModelSerializer):
    unit = serializers.SlugRelatedField(slug_field='name',read_only=True)
    class Meta:
        model = Consumer
        fields = '__all__'

class ConsumerPostSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = '__all__'

class TreeSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    parent = serializers.ListField(child=RecursiveField())

    def get_parent(self, obj):
        if obj.parent is not None:
            return ReturnDict(self.to_representation(obj), serializer=self)
        else:
            return None

    class Meta:
        model = Unit
        fields = '__all__'