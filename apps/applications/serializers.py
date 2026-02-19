from rest_framework import serializers
from .models import Application


class ApplicationCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'job',
            'resume',
            'applied_date',
        ]
    
    def create(self, validated_data):
        application = Application.objects.create(**validated_data)
        return application


class ApplicationListSerializer(serializers.ModelSerializer):
    applicant_name = serializers.CharField(source='applicant')
    job_title = serializers.CharField(source='job.title')
    class Meta:
        model = Application
        fields = [
            'job_title',
            'applicant_name',
            'status',
            'applied_date'
        ]
