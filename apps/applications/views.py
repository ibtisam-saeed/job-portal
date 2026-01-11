from rest_framework import generics
from .models import Application
from .serializers import ApplicationCreationSerializer, ApplicationListSerializer


class ApplicationCreationView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationCreationSerializer

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)


class ApplicationSearchView(generics.ListAPIView):
    serializer_class = ApplicationListSerializer

    def get_queryset(self):
        return Application.objects.filter(
            applicant=self.request.user
        )
    