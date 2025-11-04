from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.conf import settings
from .models import Resume
import json
import os
import logging

# Set up logging
logger = logging.getLogger(__name__)

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
@csrf_protect
def contact(request):
    """Handle contact form submissions - No email, just success message"""
    logger.info(f"Contact form accessed: {request.method}")
    
    if request.method == 'POST':
        try:
            # Log the attempt
            logger.info("Contact form submission attempt")
            
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            message = request.POST.get('message', '').strip()
            
            logger.info(f"Form data - Name: {name}, Email: {email}, Message length: {len(message)}")
            
            # Validate required fields
            if not name or not email or not message:
                logger.warning("Contact form submission failed: missing fields")
                return JsonResponse({
                    'status': 'error',
                    'message': 'Please fill in all required fields.'
                })
            
            # Basic email validation
            if '@' not in email or '.' not in email.split('@')[-1]:
                logger.warning(f"Contact form submission failed: invalid email {email}")
                return JsonResponse({
                    'status': 'error',
                    'message': 'Please enter a valid email address.'
                })
            
            # Log the contact form submission (instead of sending email)
            logger.info(f"Contact form submission received:")
            logger.info(f"Name: {name}")
            logger.info(f"Email: {email}")
            logger.info(f"Message: {message}")
            
            # Return success message without sending email
            return JsonResponse({
                'status': 'success',
                'message': f'Thank you {name}! Your message has been received. Please contact me directly at aarij.altamash2003@gmail.com for a quick response.'
            })
            
        except Exception as e:
            logger.error(f"Contact form submission error: {str(e)}")
            return JsonResponse({
                'status': 'error',
                'message': 'Sorry, there was an error processing your message. Please try again.'
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
