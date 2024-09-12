from rest_framework import serializers
from .models import *

class UnitGetSeriliazer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name',read_only=True)
    class Meta:
        model = Unit
        fields = '__all__'

class UnitPostSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Unit
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