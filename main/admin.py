from django.contrib import admin
from .models import Contact, Resume

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email')
    readonly_fields = ('submitted_at',)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'download_count', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at', 'download_count')
    fields = ('title', 'description', 'pdf_file', 'is_active', 'created_at', 'updated_at', 'download_count')
    
    def save_model(self, request, obj, form, change):
        # Ensure only one active resume at a time
        if obj.is_active:
            Resume.objects.filter(is_active=True).update(is_active=False)
        super().save_model(request, obj, form, change)
