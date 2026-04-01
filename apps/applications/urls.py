from django.urls import path
from .views import ApplicationCreationView, ApplicationListView, ApplicationByApplicantListView, ApplicationByJobListView


urlpatterns = [
    path('create/', ApplicationCreationView.as_view(), name='create-application'),
    path('search/', ApplicationListView.as_view(), name='search-application'),
    path('applications-by-applicant/', ApplicationByApplicantListView.as_view(), name='search-applications-by-applicant'),
    path('applications-by-job/<int:job_id>/', ApplicationByJobListView.as_view(), name='search-applications-by-job'),
]