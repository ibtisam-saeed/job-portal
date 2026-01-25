from rest_framework import generics
from .models import Application
from .serializers import ApplicationCreationSerializer, ApplicationListSerializer, ApplicationByJobSerializer
from .permissions import CanCreateApplication


class ApplicationCreationView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationCreationSerializer
    permission_classes = [CanCreateApplication]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)


class ApplicationListView(generics.ListAPIView):
    serializer_class = ApplicationListSerializer

    def get_queryset(self):
        return Application.objects.filter(
            applicant=self.request.user
        )


class ApplicationByJobListView(generics.ListAPIView):
    serializer_class = ApplicationByJobSerializer

    def get_queryset(self):
        job_title = self.request.query_params.get('job_title')
        if job_title:
            return Application.objects.filter(
                job__title__iexact=job_title
            )