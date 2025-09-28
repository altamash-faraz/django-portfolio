# Django Portfolio Website# Django Portfolio Website



A professional portfolio website built with Django, featuring resume downloads, contact form, and modern responsive design.A professional portfolio website built with Django, featuring resume downloads, contact form, and modern responsive design.



## 🌐 Live Website## 🌐 Live Website

- **Production**: [altamashfaraz.me](https://altamashfaraz.me)

- **Production**: [altamashfaraz.me](https://altamashfaraz.me)- **Backend**: Render + Namecheap CDN with PositiveSSL

- **Backend**: Render + Namecheap CDN with PositiveSSL

## ✨ Features

## ✨ Features

- � **Resume System**: Upload, manage, and track resume downloads

- 📄 **Resume System**: Upload, manage, and track resume downloads- 📧 **Contact Form**: Functional contact form with database storage  

- 📧 **Contact Form**: Functional contact form with database storage  - 🎨 **Modern Design**: Responsive portfolio with clean, professional styling

- 🎨 **Modern Design**: Responsive portfolio with clean, professional styling- 🔧 **Admin Panel**: Django admin interface for managing content

- 🔧 **Admin Panel**: Django admin interface for managing content- 🛡️ **Security**: CSRF protection and secure form handling

- 🛡️ **Security**: CSRF protection and secure form handling- ⚡ **Performance**: CDN optimization and efficient Django backend

- ⚡ **Performance**: CDN optimization and efficient Django backend

## 📱 Sections

## 📱 Sections

- **Home**: Introduction and hero section with resume download

- **Home**: Introduction and hero section with resume download- **About**: Personal background and education details

- **About**: Personal background and education details- **Skills**: Programming languages, frameworks, and technologies

- **Skills**: Programming languages, frameworks, and technologies- **Projects**: Featured portfolio projects with GitHub links

- **Projects**: Featured portfolio projects with GitHub links- **Resume**: Dedicated resume page with download tracking

- **Resume**: Dedicated resume page with download tracking- **Contact**: Working contact form with real-time validation

- **Contact**: Working contact form with real-time validation

## ️ Technology Stack

## 🛠️ Technology Stack

- **Backend**: Django 5.2.6, Python 3.13+

- **Backend**: Django 5.2.6, Python 3.13+- **Database**: SQLite3

- **Database**: SQLite3- **Frontend**: HTML5, CSS3, JavaScript (ES6+)

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)- **Hosting**: Render (backend) + Namecheap CDN (frontend)

- **Hosting**: Render (backend) + Namecheap CDN (frontend)- **SSL**: PositiveSSL via Namecheap (valid until Sep 2026)

- **SSL**: PositiveSSL via Namecheap (valid until Sep 2026)

## Installation & Setup

## 🚀 Local Development Setup

1. **Clone the repository**:

### 1. Clone the repository   ```bash

   git clone <repository-url>

```bash   cd django-portfolio

git clone https://github.com/altamash-faraz/django-portfolio.git   ```

cd django-portfolio

```2. **Create virtual environment**:

   ```bash

### 2. Create virtual environment   python -m venv venv

   source venv/bin/activate  # On Windows: venv\Scripts\activate

```bash   ```

python -m venv venv

```3. **Install dependencies**:

   ```bash

### 3. Activate virtual environment   pip install django

   ```

**Windows:**

```bash4. **Navigate to project directory**:

venv\Scripts\activate   ```bash

```   cd portfolio

   ```

**macOS/Linux:**

```bash5. **Run migrations**:

source venv/bin/activate   ```bash

```   python manage.py migrate

   ```

### 4. Install dependencies

6. **Create superuser** (optional):

```bash   ```bash

pip install -r requirements.txt   python manage.py createsuperuser

```   ```



### 5. Apply migrations7. **Collect static files**:

   ```bash

```bash   python manage.py collectstatic

python manage.py makemigrations   ```

python manage.py migrate

```8. **Run development server**:

   ```bash

### 6. Create superuser (optional)   python manage.py runserver

   ```

```bash

python manage.py createsuperuser9. **Access the website**:

```   - Portfolio: `http://127.0.0.1:8000/`

   - Admin Panel: `http://127.0.0.1:8000/admin/`

### 7. Run development server

## Project Structure

```bash

python manage.py runserver```

```django-portfolio/

├── portfolio/              # Django project directory

### 8. Access the application│   ├── manage.py          # Django management script

│   ├── portfolio/         # Project settings

- Portfolio: `http://127.0.0.1:8000/`│   ├── main/              # Main application

- Admin Panel: `http://127.0.0.1:8000/admin/`│   │   ├── models.py      # Contact model

│   │   ├── views.py       # View functions

## 🌐 Production Deployment (Namecheap + Render)│   │   ├── urls.py        # URL patterns

│   │   ├── admin.py       # Admin configuration

### Prerequisites│   │   └── templates/     # HTML templates

│   └── static/            # Static files (CSS, JS)

- Domain on Namecheap (altamashfaraz.me)├── venv/                  # Virtual environment

- PositiveSSL certificate through Namecheap├── .gitignore            # Git ignore file

- Namecheap CDN activated└── README.md             # This file

- Render account connected to GitHub```



### Deployment Steps## Contact Form



1. **Render Auto-Deploy**The contact form includes:

   - Code auto-deploys from GitHub to Render- Real-time form validation

   - App available at: `altamashfaraz.onrender.com`- AJAX submission (no page reload)

- Success/error message display

2. **Configure Namecheap CDN**- Database storage of all submissions

   - Login to Namecheap Dashboard- Admin interface for viewing messages

   - Go to Domain List → Manage altamashfaraz.me

   - Find CDN/SSL Section → Update Origin Server## Admin Panel

   - Set Origin URL: `altamashfaraz.onrender.com`

Access the Django admin panel to:

3. **Set Render Environment Variables**- View all contact form submissions

- Manage contact entries

```env- Monitor website activity

DJANGO_SETTINGS_MODULE=portfolio.production_settings- Perform administrative tasks

RENDER=True

USE_HTTPS=True## Contributing

NAMECHEAP_CDN=True

```1. Fork the repository

2. Create a feature branch

4. **Traffic Flow**3. Make your changes

4. Test thoroughly

```5. Submit a pull request

User → Namecheap CDN (PositiveSSL) → Render Django → Response

```## License



### Benefits of This SetupThis project is open source and available under the [MIT License](LICENSE).



- ✅ Keep existing SSL (valid until Sep 2026)## Author

- ✅ Namecheap CDN performance optimization

- ✅ Single dashboard management**Altamash Faraz**

- ✅ Cost effective (using existing services)- GitHub: [@altamash-faraz](https://github.com/altamash-faraz)

- ✅ Modern Django backend with resume system- LinkedIn: [altamashfaraz](https://www.linkedin.com/in/altamashfaraz/)

- Website: [altamashfaraz.me](https://altamashfaraz.me)

## 📁 Project Structure

---

```

django-portfolio/Built with ❤️ using Django and modern web technologies.

├── portfolio/                 # Django project settings
│   ├── settings.py           # Base settings
│   ├── production_settings.py # Production configuration
│   ├── urls.py              # Main URL patterns
│   └── wsgi.py              # WSGI configuration
├── main/                    # Main application
│   ├── models.py           # Contact & Resume models
│   ├── views.py            # View functions
│   ├── urls.py             # App URL patterns
│   ├── admin.py            # Admin configuration
│   └── templates/          # HTML templates
├── static/                 # Static files (CSS, JS, images)
├── media/                  # User uploads (resumes)
├── build.sh               # Render build script
├── render.yaml            # Render configuration
├── Procfile               # Process configuration
├── requirements.txt       # Python dependencies
└── manage.py             # Django management script
```

## 🎯 Key Features

### Resume System

- Upload resume files through admin panel
- Track download counts automatically
- Multiple resume versions support
- Secure file serving with proper headers

### Contact Form

- Real-time form validation
- CSRF protection
- Database storage of submissions
- Admin interface for viewing messages
- Email notifications (configurable)

### Admin Panel

- Manage resume uploads
- View contact form submissions
- Monitor download statistics
- User management and permissions

## 🔧 Configuration Files

### Render Configuration (`render.yaml`)

Defines build and runtime settings for Render deployment.

### Build Script (`build.sh`)

Handles dependency installation, static file collection, and database migrations.

### Production Settings (`production_settings.py`)

Optimized Django settings for production with CDN compatibility.

## 🐛 Troubleshooting

### Common Issues

1. **502 Errors**: Check Render app is running
2. **SSL Issues**: Verify Namecheap SSL settings
3. **CDN Problems**: Contact Namecheap support
4. **Django Errors**: Check Render build logs

### Local Development Issues

1. **Virtual Environment**: Ensure `venv` is activated
2. **Dependencies**: Run `pip install -r requirements.txt`
3. **Database**: Run migrations with `python manage.py migrate`
4. **Static Files**: Collect with `python manage.py collectstatic`

## 📞 Support

For deployment issues:
- **Render**: Check dashboard and build logs
- **Namecheap**: Use live chat support for CDN configuration
- **GitHub**: Repository issues for code-related problems

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Altamash Faraz**

- GitHub: [@altamash-faraz](https://github.com/altamash-faraz)
- LinkedIn: [altamashfaraz](https://www.linkedin.com/in/altamashfaraz/)
- Website: [altamashfaraz.me](https://altamashfaraz.me)

---

Built with ❤️ using Django and modern web technologies.