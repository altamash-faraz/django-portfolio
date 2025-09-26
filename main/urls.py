from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume_view, name='resume'),
    path('resume/download/', views.resume_download, name='resume_download'),
    path('resume/download/<int:resume_id>/', views.resume_download, name='resume_download_specific'),
    path('resume/preview/', views.resume_preview, name='resume_preview'),
    path('resume/preview/<int:resume_id>/', views.resume_preview, name='resume_preview_specific'),
]