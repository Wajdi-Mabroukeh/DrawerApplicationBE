from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import WorkSpace


class WorkSpaceSerializer(ModelSerializer):
    image = serializers.ImageField(required=True)
    # shapes = serializers.CharField(required=False)
    title = serializers.CharField(required=True)

    class Meta:
        model = WorkSpace
        fields = '__all__'


class WorkSpaceMiniSerializer(ModelSerializer):

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = WorkSpace
        exclude = ['image']
