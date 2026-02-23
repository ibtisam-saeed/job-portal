from django.urls import path
from .views import ApplicationCreationView, ApplicationListView


urlpatterns = [
    path('create/', ApplicationCreationView.as_view(), name='create-application'),
    path('search/', ApplicationListView.as_view(), name='search-application')
]