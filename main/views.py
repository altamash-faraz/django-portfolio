from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Resume
import json
import os
import requests
from datetime import datetime, timedelta
import logging

# Set up logging
logger = logging.getLogger(__name__)

def get_github_projects(username='altamash-faraz'):
    """Fetch actual projects from GitHub repositories"""
    try:
        repos_url = f'https://api.github.com/users/{username}/repos'
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Portfolio-Website'
        }
        
        response = requests.get(repos_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            repos_data = response.json()
            
            # Filter and process repositories
            featured_projects = []
            
            # Define priority projects (manually curated for better presentation)
            priority_repos = [
                'votepro', 'CRUD', 'visiOCR', 'AI-Resume-Screening', 
                'hotel-booking-app', 'django-portfolio', 'portfolio-website'
            ]
            
            # Sort repos: priority first, then by stars, then by recent activity
            sorted_repos = []
            
            # Add priority repos first
            for priority in priority_repos:
                for repo in repos_data:
                    if repo['name'].lower() == priority.lower() and not repo['fork']:
                        sorted_repos.append(repo)
                        break
            
            # Add remaining non-fork repos sorted by stars
            remaining_repos = [r for r in repos_data if not r['fork'] 
                             and r['name'] not in [sr['name'] for sr in sorted_repos]]
            remaining_repos.sort(key=lambda x: x['stargazers_count'], reverse=True)
            
            # Combine and limit to top 6 projects
            all_repos = (sorted_repos + remaining_repos)[:6]
            
            for repo in all_repos:
                # Determine project category and tech stack based on repo
                category, tech_stack, demo_url = categorize_project(repo)
                
                project = {
                    'name': repo['name'],
                    'title': format_project_title(repo['name']),
                    'description': repo['description'] or f"A {repo['language'] or 'software'} project showcasing development skills.",
                    'category': category,
                    'tech_stack': tech_stack,
                    'github_url': repo['html_url'],
                    'demo_url': demo_url,
                    'stars': repo['stargazers_count'],
                    'language': repo['language'],
                    'updated_at': repo['updated_at'],
                    'created_at': repo['created_at']
                }
                featured_projects.append(project)
            
            return featured_projects
        
    except Exception as e:
        logger.error(f"Error fetching GitHub projects: {e}")
    
    # Return fallback projects if API fails
    return get_fallback_projects()

def categorize_project(repo):
    """Categorize project and determine tech stack based on repository data"""
    name = repo['name'].lower()
    language = repo['language'] or ''
    description = (repo['description'] or '').lower()
    
    # Determine demo URL based on known projects
    demo_urls = {
        'votepro': 'https://votepro.onrender.com/',
        'visiocr': 'https://visiocr-y4rx.onrender.com/',
        'ai-resume-screening': 'https://ai-resume-screen.streamlit.app/',
        'django-portfolio': 'https://altamashfaraz.onrender.com/',
    }
    demo_url = demo_urls.get(name, None)
    
    # Categorize based on project name and content
    if 'ai' in name or 'ml' in name or 'resume' in name or 'ocr' in name:
        category = 'AI/ML'
        if 'streamlit' in description:
            tech_stack = ['Streamlit', 'Python', 'Scikit-learn', 'Machine Learning']
        elif 'django' in description or language == 'Python':
            tech_stack = ['Django', 'Python', 'Tesseract OCR', 'OpenCV']
        else:
            tech_stack = ['Python', 'Machine Learning', 'Data Science']
    
    elif 'react' in description or 'typescript' in description or 'hotel' in name or 'booking' in name:
        category = 'Full Stack'
        tech_stack = ['React', 'TypeScript', 'Node.js', 'MongoDB']
    
    elif 'django' in description or language == 'Python':
        category = 'Web Application'
        if 'portfolio' in name:
            tech_stack = ['Django', 'Python', 'Bootstrap', 'PostgreSQL']
        else:
            tech_stack = ['Django', 'Python', 'REST API', 'Database']
    
    elif 'flask' in description or ('python' in description and 'web' in description):
        category = 'Web Application'
        if 'vote' in name:
            tech_stack = ['Flask', 'Python', 'PostgreSQL', 'Bootstrap']
        elif 'crud' in name:
            tech_stack = ['Flask', 'Python', 'MongoDB', 'REST API']
        else:
            tech_stack = ['Flask', 'Python', 'Web Development']
    
    elif language == 'JavaScript':
        category = 'Frontend'
        tech_stack = ['JavaScript', 'HTML', 'CSS', 'Web Development']
    
    elif language == 'Java':
        category = 'Backend'
        tech_stack = ['Java', 'Spring Boot', 'Backend Development']
    
    else:
        category = 'Software Development'
        tech_stack = [language] if language else ['Programming']
    
    return category, tech_stack, demo_url

def format_project_title(repo_name):
    """Format repository name into a presentable title"""
    title_mappings = {
        'votepro': 'VotePro',
        'visiocr': 'VisiOCR',
        'ai-resume-screening': 'AI Resume Screening',
        'hotel-booking-app': 'MernHolidays',
        'django-portfolio': 'Django Portfolio',
        'crud': 'CRUD Application'
    }
    
    if repo_name.lower() in title_mappings:
        return title_mappings[repo_name.lower()]
    
    # Default formatting: capitalize and replace hyphens/underscores
    return repo_name.replace('-', ' ').replace('_', ' ').title()

def get_fallback_projects():
    """Fallback projects when GitHub API is unavailable"""
    return [
        {
            'name': 'votepro',
            'title': 'VotePro',
            'description': 'Advanced polling application with email verification, real-time results, and secure voting mechanisms.',
            'category': 'Web Application',
            'tech_stack': ['Flask', 'Python', 'PostgreSQL', 'Bootstrap'],
            'github_url': 'https://github.com/altamash-faraz/votepro',
            'demo_url': 'https://votepro.onrender.com/',
            'stars': 0,
            'language': 'Python'
        },
        {
            'name': 'CRUD',
            'title': 'CRUD Application',
            'description': 'Enterprise-grade CRUD application with advanced MongoDB operations and analytics.',
            'category': 'Web Application',
            'tech_stack': ['Flask', 'Python', 'MongoDB', 'REST API'],
            'github_url': 'https://github.com/altamash-faraz/CRUD',
            'demo_url': None,
            'stars': 0,
            'language': 'Python'
        },
        {
            'name': 'visiOCR',
            'title': 'VisiOCR',
            'description': 'Intelligent OCR-powered visitor management system with 95%+ accuracy.',
            'category': 'AI/ML',
            'tech_stack': ['Django', 'Tesseract OCR', 'OpenCV', 'Python'],
            'github_url': 'https://github.com/altamash-faraz/visiOCR',
            'demo_url': 'https://visiocr-y4rx.onrender.com/',
            'stars': 0,
            'language': 'Python'
        }
    ]

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
    
    # Fetch real GitHub statistics and projects
    github_stats = get_github_stats()
    github_projects = get_github_projects()
    
    context = {
        'active_resume': active_resume,
        'github_stats': github_stats,
        'github_projects': github_projects
    }
    return render(request, 'main/index.html', context)

@require_http_methods(["GET", "POST"])
@csrf_protect
def contact(request):
    """Handle contact form submissions via email"""
    if request.method == 'POST':
        try:
            # Log the attempt
            logger.info("Contact form submission attempt")
            
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            message = request.POST.get('message', '').strip()
            
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
            
            # Prepare email content
            subject = f'Portfolio Contact Form - Message from {name}'
            email_message = f"""
New contact form submission from your portfolio:

Name: {name}
Email: {email}

Message:
{message}

---
This message was sent from your portfolio contact form.
Reply directly to {email} to respond to the sender.
            """.strip()
            
            # Send email
            try:
                logger.info(f"Attempting to send email - From: {settings.DEFAULT_FROM_EMAIL}, To: {settings.CONTACT_EMAIL}")
                
                send_mail(
                    subject=subject,
                    message=email_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                
                logger.info(f"Contact form email sent successfully from {email}")
                
                return JsonResponse({
                    'status': 'success',
                    'message': f'Thank you {name}! Your message has been sent. I will get back to you soon.'
                })
                
            except Exception as email_error:
                logger.error(f"Failed to send contact email: {str(email_error)}")
                logger.error(f"Email config - Backend: {settings.EMAIL_BACKEND}")
                logger.error(f"Email config - Host: {getattr(settings, 'EMAIL_HOST', 'Not set')}")
                logger.error(f"Email config - Port: {getattr(settings, 'EMAIL_PORT', 'Not set')}")
                logger.error(f"Email config - TLS: {getattr(settings, 'EMAIL_USE_TLS', 'Not set')}")
                logger.error(f"Email config - User: {getattr(settings, 'EMAIL_HOST_USER', 'Not set')}")
                logger.error(f"Email config - Password set: {'Yes' if getattr(settings, 'EMAIL_HOST_PASSWORD', '') else 'No'}")
                
                return JsonResponse({
                    'status': 'error',
                    'message': f'Sorry, there was an error sending your message. Please try again or contact me directly at {settings.CONTACT_EMAIL}'
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
