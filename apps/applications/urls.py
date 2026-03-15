from django.urls import path
from .views import ApplicationCreationView, ApplicationListView, ApplicationByApplicantListView


urlpatterns = [
    path('create/', ApplicationCreationView.as_view(), name='create-application'),
    path('search/', ApplicationListView.as_view(), name='search-application'),
    path('applications-by-applicant/', ApplicationByApplicantListView.as_view(), name='search-applications-by-applicant')
]