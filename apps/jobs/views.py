from rest_framework import generics
from .models import Job
from .serializers import JobCreationSerializer


class JobCreationView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobCreationSerializer

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)