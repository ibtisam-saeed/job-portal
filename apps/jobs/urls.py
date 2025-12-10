from django.urls import path
from .views import JobCreationView


urlpatterns = [
    path('create/', JobCreationView.as_view(), name='create-job')
]
