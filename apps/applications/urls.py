from django.urls import path
from .views import ApplicationCreationView, ApplicationListView, ApplicationByJobListView


urlpatterns = [
    path('create/', ApplicationCreationView.as_view(), name='create-application'),
    path('search-by-user/', ApplicationListView.as_view(), name='search-application'),
    path('search-by-job-title/', ApplicationByJobListView.as_view(), name='applications-by-job-title')
]