from django.urls import path
from .views import ApplicationCreationView


urlpatterns = [
    path('create/', ApplicationCreationView.as_view(), name='create-application')
]