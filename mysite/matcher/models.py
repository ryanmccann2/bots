from django.db import models

# Create your models here.
class User(models.Model):
    PROFILE_TYPE_CANDIDATE = 'candidate'
    PROFILE_TYPE_RECRUITER = 'recruiter'
    PROFILE_TYPE_CHOICES = [
        (PROFILE_TYPE_CANDIDATE, 'Candidate'),
        (PROFILE_TYPE_RECRUITER, 'Recruiter'),
    ]

    profile_type = models.CharField(max_length=20, choices=PROFILE_TYPE_CHOICES)
    identifier = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_bio = models.TextField(max_length=200, blank=True)
    zip_code = models.CharField(max_length=10)
    skills = models.TextField(max_length=50)
    years_of_experience = models.PositiveIntegerField()
    education = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    # Additional fields for recruiter profiles:
    company_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.identifier

# class Post(models.Model):
#     position_title = models.models.CharField(max_length=50)
#     type = 