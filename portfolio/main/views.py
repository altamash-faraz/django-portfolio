from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Contact
import json

def index(request):
    """Main portfolio page view"""
    return render(request, 'main/index.html')

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
