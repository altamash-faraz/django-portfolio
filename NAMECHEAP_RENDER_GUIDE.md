# Namecheap + Render Deployment Guide

## 🌐 Your Current Setup
- **Domain Registrar**: Namecheap
- **SSL Certificate**: PositiveSSL via Namecheap (valid until Sep 14, 2026)
- **CDN**: Namecheap CDN with automatic SSL management
- **Domain**: altamashfaraz.me & www.altamashfaraz.me

## 🚀 Namecheap-Specific Deployment Steps

### Step 1: Deploy Django App to Render
1. Your code should auto-deploy from GitHub to Render
2. Note your Render app URL: `altamashfaraz.onrender.com`
3. Test that Django works at the Render URL

### Step 2: Configure Namecheap CDN Origin
Since you're using Namecheap's CDN with PositiveSSL:

1. **Login to Namecheap Dashboard**
2. **Go to Domain List** → Click "Manage" for altamashfaraz.me
3. **Find CDN/SSL Section** → Click "Manage" or "Settings"
4. **Update Origin Server/Backend**:
   - **Origin URL**: `altamashfaraz.onrender.com`
   - **Origin Port**: `443` (HTTPS) or `80` (HTTP)
   - **Protocol**: HTTP or HTTPS (Render supports both)

### Step 3: Namecheap DNS Configuration (If Needed)
If CDN isn't handling everything, update these DNS records:

**Advanced DNS in Namecheap:**
```
Type: CNAME
Host: @
Value: altamashfaraz.onrender.com
TTL: Automatic

Type: CNAME  
Host: www
Value: altamashfaraz.onrender.com
TTL: Automatic
```

**⚠️ Important**: Only do DNS changes if CDN origin update doesn't work.

### Step 4: Verify Namecheap SSL Settings
In your SSL management:
1. Ensure SSL certificate covers both:
   - `altamashfaraz.me`
   - `www.altamashfaraz.me`
2. SSL should be set to "Full" or "Flexible" mode
3. Keep "Auto SSL" enabled

## 🔧 Render Environment Variables
Add these in your Render dashboard:
```
DJANGO_SETTINGS_MODULE=portfolio.production_settings
RENDER=True  
USE_HTTPS=True
NAMECHEAP_CDN=True
```

## 🌐 Traffic Flow with Namecheap
```
User Request → Namecheap CDN (PositiveSSL) → Render Django App → Response
```

## 💡 Benefits of Namecheap + Render
- ✅ **Keep existing SSL** (no interruption until Sep 2026)
- ✅ **Namecheap CDN** performance optimization  
- ✅ **Single dashboard** management (domain + SSL + CDN)
- ✅ **Cost effective** (using existing services)
- ✅ **Django backend** with resume downloads
- ✅ **Automatic SSL renewal** through Namecheap

## 📞 Namecheap Support
If you need help finding CDN origin settings:
1. **Live Chat**: Available in Namecheap dashboard
2. **Search**: "CDN origin server" in their help docs
3. **Location**: Usually under Domain → Advanced → CDN or SSL/TLS

## ⚠️ Important Notes
- **Don't remove** the ALIAS/CNAME records CDN depends on
- **Test thoroughly** after origin server changes
- **Monitor both** Namecheap and Render dashboards
- **Keep CDN active** to maintain SSL automation

## 🔍 Troubleshooting
- **502 errors**: Check Render app is running
- **SSL issues**: Verify Namecheap SSL settings  
- **CDN not working**: Contact Namecheap support
- **Django errors**: Check Render build logs

This setup leverages your existing Namecheap investment while modernizing the backend!