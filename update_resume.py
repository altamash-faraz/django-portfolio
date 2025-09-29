#!/usr/bin/env python
"""
Script to update resume in database
"""
import os
import django
import sys

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Resume

def update_resume():
    """Update or create resume record in database"""
    
    # Resume file details
    resume_file = 'resumes/altamash_faraz_resume.pdf'
    resume_title = 'Altamash Faraz - Software Developer Resume'
    resume_description = 'Computer Engineering Student with expertise in Python, Django, and web development. Experienced in full-stack development, database management, and modern web technologies.'
    
    # Check if file exists
    file_path = os.path.join('media', resume_file)
    if not os.path.exists(file_path):
        print(f"❌ Error: Resume file not found at {file_path}")
        return False
    
    # Deactivate all existing resumes
    Resume.objects.all().update(is_active=False)
    print("🔄 Deactivated all existing resumes")
    
    # Create or update the resume record
    resume, created = Resume.objects.get_or_create(
        pdf_file=resume_file,
        defaults={
            'title': resume_title,
            'description': resume_description,
            'is_active': True,
            'download_count': 0
        }
    )
    
    if created:
        print(f"✅ Created new resume record: {resume.title}")
    else:
        # Update existing record
        resume.title = resume_title
        resume.description = resume_description
        resume.is_active = True
        resume.save()
        print(f"✅ Updated existing resume record: {resume.title}")
    
    print(f"📄 Resume file: {resume.pdf_file}")
    print(f"📊 Download count: {resume.download_count}")
    print(f"🟢 Active status: {resume.is_active}")
    
    return True

if __name__ == '__main__':
    print("🚀 Updating resume in database...")
    
    try:
        success = update_resume()
        if success:
            print("\n🎉 Resume updated successfully!")
            print("Your website will now show the resume instead of 'Coming Soon' message.")
        else:
            print("\n❌ Failed to update resume.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Make sure you're running this from the project directory with the virtual environment activated.")