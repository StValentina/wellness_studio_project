from rest_framework import serializers

from services.models import Service
from studio_classes.models import StudioClass


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class StudioClassSerializer(serializers.ModelSerializer):
    service = serializers.StringRelatedField(source='studio_class_service')
    tags = serializers.StringRelatedField(many=True)
    instructor = serializers.SerializerMethodField()

    class Meta:
        model = StudioClass
        fields = ['class_title', 'class_description', 'level', 'service', 'tags', 'instructor']

    def get_instructor(self, obj):
        return obj.instructor.profile.get_full_name()