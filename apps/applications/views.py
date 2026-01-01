from rest_framework import generics
from .models import Application
from .serializers import ApplicationCreationSerializer


class ApplicationCreationView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationCreationSerializer

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
    