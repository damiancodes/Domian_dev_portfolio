# portfolio/models.py
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    availability = models.CharField(max_length=50, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year_start = models.IntegerField()
    year_end = models.IntegerField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.title


class Skill(models.Model):
    SKILL_TYPES = (
        ('design', 'Design'),
        ('coding', 'Coding'),
        ('tool', 'Tool'),
    )
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(default=0)  # 0-100
    skill_type = models.CharField(max_length=10, choices=SKILL_TYPES)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    category = models.CharField(max_length=50)
    url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    date_created = models.DateField()

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    PLATFORM_CHOICES = (
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('dev', 'Dev.to'),
        ('other', 'Other'),
    )
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()

    def __str__(self):
        return self.platform


