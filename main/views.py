from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404, HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Contact, Resume
import json
import os

def index(request):
    """Main portfolio page view"""
    # Use hardcoded resume configuration for production reliability
    active_resume = {
        'title': 'Altamash Faraz - Resume',
        'description': 'Software Engineer & Full Stack Developer',
        'is_active': True,
        'google_drive_url': 'https://drive.google.com/file/d/1Yqr7FygGXA_b_lgEe0ytN920J_farEZ0/view?usp=sharing',
        'download_url': 'https://drive.google.com/uc?export=download&id=1Yqr7FygGXA_b_lgEe0ytN920J_farEZ0'
    }
    
    context = {
        'active_resume': active_resume
    }
    return render(request, 'main/index.html', context)

@require_http_methods(["GET", "POST"])
def contact(request):
    """Handle contact form submissions"""
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            # Validate required fields
            if not name or not email or not message:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Please fill in all required fields.'
                })
            
            # Save to database
            contact_submission = Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            
            return JsonResponse({
                'status': 'success',
                'message': f'Thank you {name}! Your message has been received. I will get back to you soon.'
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': 'Sorry, there was an error saving your message. Please try again.'
            })
    
    # For GET requests, redirect to home page
    return render(request, 'main/index.html')

def resume_view(request):
    """Display resume page with download option"""
    # Use hardcoded resume configuration for production reliability
    active_resume = {
        'title': 'Altamash Faraz - Resume',
        'description': 'Software Engineer & Full Stack Developer',
        'is_active': True,
        'google_drive_url': 'https://drive.google.com/file/d/1Yqr7FygGXA_b_lgEe0ytN920J_farEZ0/view?usp=sharing',
        'download_url': 'https://drive.google.com/uc?export=download&id=1Yqr7FygGXA_b_lgEe0ytN920J_farEZ0'
    }
    
    context = {
        'active_resume': active_resume,
        'all_resumes': [active_resume]  # For template compatibility
    }
    return render(request, 'main/resume.html', context)

def resume_download(request, resume_id=None):
    """Handle resume download and redirect to Google Drive"""
    # Redirect to Google Drive direct download URL
    google_drive_download_url = 'https://drive.google.com/uc?export=download&id=1Yqr7FygGXA_b_lgEe0ytN920J_farEZ0'
    return redirect(google_drive_download_url)

def resume_preview(request, resume_id=None):
    """Display resume in browser (preview mode) - redirect to Google Drive view"""
    # Redirect to Google Drive view URL
    google_drive_view_url = 'https://drive.google.com/file/d/1Yqr7FygGXA_b_lgEe0ytN920J_farEZ0/view?usp=sharing'
    return redirect(google_drive_view_url)
