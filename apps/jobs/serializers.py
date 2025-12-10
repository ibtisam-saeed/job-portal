from rest_framework import serializers
from .models import Job


class JobCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'employment_type', 'posted_date', 'deadline', 'status']
    
    def create(self, validated_data):
        job = Job.objects.create(**validated_data)
        return job