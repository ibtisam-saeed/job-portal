from django.urls import path
from .views import ApplicationCreationView, ApplicationSearchView


urlpatterns = [
    path('create/', ApplicationCreationView.as_view(), name='create-application'),
    path('search/', ApplicationSearchView.as_view(), name='search-application')
]