from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404, HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Contact, Resume
import json
import os

def index(request):
    """Main portfolio page view"""
    # Get active resume for display
    active_resume = Resume.objects.filter(is_active=True).first()
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
    active_resume = Resume.objects.filter(is_active=True).first()
    all_resumes = Resume.objects.all()
    
    context = {
        'active_resume': active_resume,
        'all_resumes': all_resumes
    }
    return render(request, 'main/resume.html', context)

def resume_download(request, resume_id=None):
    """Handle resume download and track download count"""
    try:
        if resume_id:
            resume = get_object_or_404(Resume, id=resume_id)
        else:
            # Get active resume if no specific ID provided
            resume = Resume.objects.filter(is_active=True).first()
            if not resume:
                raise Http404("No active resume found")
        
        # Increment download count
        resume.increment_download_count()
        
        # Prepare file response
        if resume.pdf_file and os.path.exists(resume.pdf_file.path):
            with open(resume.pdf_file.path, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="Altamash_Faraz_Resume.pdf"'
                return response
        else:
            raise Http404("Resume file not found")
            
    except Resume.DoesNotExist:
        raise Http404("Resume not found")
    except Exception as e:
        # Log error in production
        raise Http404("Error downloading resume")

def resume_preview(request, resume_id=None):
    """Display resume in browser (preview mode)"""
    try:
        if resume_id:
            resume = get_object_or_404(Resume, id=resume_id)
        else:
            # Get active resume if no specific ID provided
            resume = Resume.objects.filter(is_active=True).first()
            if not resume:
                raise Http404("No active resume found")
        
        # Serve file for preview (inline display)
        if resume.pdf_file and os.path.exists(resume.pdf_file.path):
            with open(resume.pdf_file.path, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'inline; filename="Altamash_Faraz_Resume.pdf"'
                return response
        else:
            raise Http404("Resume file not found")
            
    except Resume.DoesNotExist:
        raise Http404("Resume not found")
    except Exception as e:
        raise Http404("Error previewing resume")
