# Render Deployment Guide for Django Portfolio

## 🚀 Deployment Steps

### 1. DNS Configuration (Required First!)

Based on Render's instructions, update your DNS records at your domain registrar:

#### For altamashfaraz.me:
- **Type**: ANAME or ALIAS record
- **Name**: @ (root domain)
- **Value**: `altamashfaraz.onrender.com`

If ANAME/ALIAS not supported, use:
- **Type**: A record
- **Name**: @ 
- **Value**: `216.24.57.1`

#### For www.altamashfaraz.me:
- **Type**: CNAME record
- **Name**: www
- **Value**: `altamashfaraz.onrender.com`

### 2. Render Service Configuration

In your Render dashboard:
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn portfolio.wsgi:application`
- **Environment Variables**:
  - `DJANGO_SETTINGS_MODULE` = `portfolio.production_settings`
  - `PYTHON_VERSION` = `3.11.0`
  - `RENDER` = `True`

### 3. Custom Domain Setup

1. Go to your service settings in Render
2. Add custom domains:
   - `altamashfaraz.me`
   - `www.altamashfaraz.me`
3. Click "Verify" after DNS propagation

### 4. SSL Certificate

Render automatically provides free SSL certificates for custom domains.

### 5. Environment Variables (Optional)

For production features, add these in Render:
- `SECRET_KEY` - Generate a new one for production
- `EMAIL_HOST_USER` - For contact form emails
- `EMAIL_HOST_PASSWORD` - App password for Gmail
- `USE_HTTPS` = `True` - Enable HTTPS redirects

## 📁 Files Created for Deployment

- `render.yaml` - Render service configuration
- `build.sh` - Build script for deployment
- `portfolio/production_settings.py` - Production Django settings
- `Procfile` - Process file for web server
- `runtime.txt` - Python version specification

## 🌐 After Deployment

Your portfolio will be available at:
- https://altamashfaraz.me
- https://www.altamashfaraz.me
- https://altamashfaraz.onrender.com (Render subdomain)

## 🔧 Troubleshooting

- **502 Error**: Check build logs in Render dashboard
- **Static files not loading**: Ensure `collectstatic` runs in build script
- **Database issues**: Make sure migrations run successfully
- **Domain not working**: Verify DNS propagation (can take 24-48 hours)

## 📝 Next Steps

1. Update DNS records at your domain registrar
2. Push changes to GitHub
3. Wait for Render to deploy automatically
4. Verify domain ownership in Render
5. Test your live site at altamashfaraz.me