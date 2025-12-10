from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)

    EMPLOYMENT_TYPES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('temporary', 'Temporary'),
    )

    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPES)
    posted_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('closed', 'Closed'),
        ('draft', 'Draft'),
    )

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.title
