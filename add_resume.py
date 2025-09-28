import os
import sys
import django

# Add the project directory to the Python path
sys.path.append('D:/Portfolio/django portfolio')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Setup Django
django.setup()

# Now import Django models
from main.models import Resume

# Create resume entry
resume = Resume.objects.create(
    title="Altamash Faraz - Resume",
    description="Computer Engineering Student | Python Developer | AI/ML Enthusiast",
    pdf_file="resumes/Altamash_Resume.pdf",
    is_active=True
)

print(f"Resume created successfully! ID: {resume.id}")
print(f"Title: {resume.title}")
print(f"File: {resume.pdf_file}")
print(f"Active: {resume.is_active}")