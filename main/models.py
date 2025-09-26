from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    
    class Meta:
        ordering = ['-submitted_at']

class Resume(models.Model):
    title = models.CharField(max_length=200, default="My Resume")
    description = models.TextField(blank=True, help_text="Brief description of the resume")
    pdf_file = models.FileField(upload_to='resumes/', help_text="Upload your resume in PDF format")
    is_active = models.BooleanField(default=True, help_text="Set as active resume to display on portfolio")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    download_count = models.PositiveIntegerField(default=0, help_text="Number of times downloaded")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"
    
    def increment_download_count(self):
        """Increment download count when resume is downloaded"""
        self.download_count += 1
        self.save(update_fields=['download_count'])
