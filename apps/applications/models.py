from django.db import models
from ..jobs.models import Job
from django.contrib.auth.models import User


class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='resumes/', blank=True)
    applied_date = models.DateField(auto_now_add=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Application #{self.application_id} - {self.applicant}"