from django.urls import path
from .views import ApplicantRegisterView

urlpatterns = [
    path('register/', ApplicantRegisterView.as_view(), name='applicant-register')
]
