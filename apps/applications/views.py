from rest_framework import generics
from .models import Application
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .serializers import ApplicationCreationSerializer, ApplicationListSerializer
from .permissions import CanCreateApplication


class ApplicationCreationView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationCreationSerializer
    permission_classes = [DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)


class ApplicationListView(generics.ListAPIView):
    serializer_class = ApplicationListSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Application.objects.all()
        query_params = self.request.query_params
        if user := query_params.get('user'):
            queryset = queryset.filter(applicant__username__iexact=user)
        if job_title := query_params.get('job'):
            queryset = queryset.filter(job__title__iexact=job_title)

        return queryset


class ApplicationByApplicantListView(generics.ListAPIView):
    serializer_class = ApplicationListSerializer

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)


class ApplicationByJobListView(generics.ListAPIView):
    serializer_class = ApplicationListSerializer

    def get_queryset(self):
        job_id = self.kwargs.get('job_id')
        return Application.objects.filter(job__job_id=job_id, applicant=self.request.user)
