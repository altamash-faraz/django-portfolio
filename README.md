# Django Portfolio Website

A professional portfolio website built with Django, featuring dynamic GitHub stats, resume downloads, contact form, and modern responsive design.

## 🌐 Live Website

- **Production**: [altamashfaraz.me](https://altamashfaraz.me)
- **Backend**: Render + Namecheap CDN with PositiveSSL

## ✨ Features

- 📄 **Resume System**: Upload, manage, and track resume downloads with Google Drive integration
- 🔗 **Dynamic GitHub Stats**: Real-time GitHub statistics with follower count, repositories, and activity
- 📧 **Contact Form**: Functional contact form with database storage  
- 🎨 **Modern Design**: Responsive portfolio with clean, professional styling
- 🎓 **Education Timeline**: Interactive education section with academic achievements
- 💼 **Project Showcase**: Featured projects with live demos and GitHub links
- 🔧 **Admin Panel**: Django admin interface for managing content
- 🛡️ **Security**: CSRF protection and secure form handling
- ⚡ **Performance**: CDN optimization and efficient Django backend

## 📱 Sections

- **Home**: Introduction and hero section with resume download
- **About**: Personal background and professional summary
- **Skills**: Comprehensive technical skills organized by categories
- **Education**: Academic timeline with institutions and achievements
- **Projects**: Featured portfolio projects (VotePro, VisiOCR, AI Resume Screening, etc.)
- **Resume**: Dedicated resume page with download tracking
- **GitHub**: Dynamic GitHub statistics and contributions
- **Contact**: Working contact form with real-time validation

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/altamash-faraz/django-portfolio.git
cd django-portfolio
```

### 2. Create virtual environment

```bash


python -m venv venv
```

### 3. Activate virtual environment

**Windows:**

```bash

venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create superuser (optional)
```bash
python manage.py createsuperuser
```

### 7. Collect static files
```bash
python manage.py collectstatic
```

### 8. Run development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the portfolio.

## 🛠️ Tech Stack

### Backend
- **Django 5.2.6**: Web framework
- **Python 3.x**: Programming language
- **SQLite**: Database (development)
- **PostgreSQL**: Database (production)

### Frontend
- **HTML5/CSS3**: Markup and styling
- **JavaScript**: Interactive functionality
- **Responsive Design**: Mobile-first approach
- **Font Awesome**: Icons
- **Google Fonts**: Typography

### Deployment
- **Render**: Backend hosting
- **Namecheap**: Domain and CDN
- **PositiveSSL**: SSL certificate
- **Whitenoise**: Static file serving

## 🎯 Key Features Explained

### Dynamic GitHub Stats

- Real-time fetching of GitHub user statistics
- Displays followers, following, repositories, and stars
- Automatic fallback system for API failures
- Smart caching for performance optimization

### Resume Management

- Google Drive integration for resume hosting
- Download tracking and analytics
- Admin panel for resume management
- Secure file serving

### Contact System

- Functional contact form with validation
- Database storage of messages
- Admin interface for message management
- CSRF protection

### Responsive Design

- Mobile-first approach
- Cross-browser compatibility
- Modern CSS Grid and Flexbox
- Interactive animations and transitions

## 🚀 Deployment

The site is deployed on Render with the following configuration:

1. **Build Command**: `./build.sh`
2. **Start Command**: `gunicorn portfolio.wsgi:application`
3. **Environment**: Python 3.x
4. **Database**: PostgreSQL (production)

## 📈 Performance

- **PageSpeed Score**: 95+ (Mobile & Desktop)
- **Loading Time**: < 2 seconds
- **CDN**: Namecheap CDN for static assets
- **SSL**: PositiveSSL certificate
- **Caching**: Browser and server-side caching

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Altamash Faraz**
- Website: [altamashfaraz.me](https://altamashfaraz.me)
- GitHub: [@altamash-faraz](https://github.com/altamash-faraz)
- Email: [contact@altamashfaraz.me](mailto:contact@altamashfaraz.me)

## 🎉 Acknowledgments

- Django community for the excellent framework
- GitHub API for providing developer statistics
- Render for reliable hosting platform
- Font Awesome for beautiful icons

---

Built with ❤️ using Django and modern web technologies.
