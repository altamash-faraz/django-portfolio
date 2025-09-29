from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404, HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Contact, Resume
import json
import os
import requests
from datetime import datetime, timedelta

def get_github_stats(username='altamash-faraz'):
    """Fetch real GitHub statistics for the user"""
    try:
        # GitHub API endpoints
        user_url = f'https://api.github.com/users/{username}'
        repos_url = f'https://api.github.com/users/{username}/repos'
        events_url = f'https://api.github.com/users/{username}/events'
        
        # Set up headers for better rate limiting
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Portfolio-Website'
        }
        
        # Fetch user data
        user_response = requests.get(user_url, headers=headers, timeout=5)
        repos_response = requests.get(repos_url, headers=headers, timeout=5)
        
        if user_response.status_code == 200 and repos_response.status_code == 200:
            user_data = user_response.json()
            repos_data = repos_response.json()
            
            # Calculate contributions (approximate from recent activity)
            contributions = 0
            try:
                events_response = requests.get(events_url, headers=headers, timeout=5)
                if events_response.status_code == 200:
                    events = events_response.json()
                    # Count recent push events as contributions
                    one_year_ago = datetime.now() - timedelta(days=365)
                    for event in events[:100]:  # Limit to recent events
                        event_date = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                        if event_date > one_year_ago and event['type'] in ['PushEvent', 'CreateEvent', 'IssuesEvent']:
                            contributions += 1
            except:
                contributions = user_data.get('public_repos', 0) * 5  # Fallback estimate
            
            # Calculate recent repositories (last 6 months)
            recent_repos = 0
            try:
                six_months_ago = datetime.now() - timedelta(days=180)
                for repo in repos_data:
                    if repo['created_at']:
                        repo_date = datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                        if repo_date > six_months_ago:
                            recent_repos += 1
            except:
                recent_repos = min(6, len(repos_data))  # Fallback
            
            return {
                'followers': user_data.get('followers', 0),
                'following': user_data.get('following', 0),
                'public_repos': user_data.get('public_repos', 0),
                'contributions': max(contributions, 50),  # Minimum reasonable number
                'recent_repos': recent_repos,
                'total_stars': sum(repo.get('stargazers_count', 0) for repo in repos_data),
                'profile_url': user_data.get('html_url', f'https://github.com/{username}'),
                'bio': user_data.get('bio', ''),
                'location': user_data.get('location', ''),
                'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M')
            }
        else:
            # Fallback data if API fails
            return get_fallback_github_stats()
            
    except Exception as e:
        # Return fallback data if any error occurs
        print(f"GitHub API Error: {e}")
        return get_fallback_github_stats()

def get_fallback_github_stats():
    """Fallback GitHub stats when API is unavailable"""
    return {
        'followers': 15,
        'following': 22,
        'public_repos': 9,
        'contributions': 150,
        'recent_repos': 6,
        'total_stars': 3,
        'profile_url': 'https://github.com/altamash-faraz',
        'bio': 'Computer Engineering Student',
        'location': 'Dhule, Maharashtra, India',
        'last_updated': 'Cached Data'
    }

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
    
    # Fetch real GitHub statistics
    github_stats = get_github_stats()
    
    context = {
        'active_resume': active_resume,
        'github_stats': github_stats
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
