# Django Portfolio Website

A professional portfolio website built with Django, featuring a modern design, contact form functionality, and admin panel for managing submissions.

## 🌐 Live Website


## Features

- 🎨 **Modern Design**: Responsive portfolio with clean, professional styling
- 📱 **Mobile Responsive**: Optimized for all device sizes
- 📧 **Contact Form**: Functional contact form with database storage
- 🔧 **Admin Panel**: Django admin interface for managing contact submissions
- 🛡️ **Security**: CSRF protection and secure form handling
- ⚡ **Performance**: Optimized static files and efficient Django backend

## Sections

- **Home**: Introduction and hero section
- **About**: Personal background and education details
- **Skills**: Programming languages, frameworks, and technologies
- **Projects**: Featured portfolio projects with GitHub links
- **GitHub Stats**: GitHub activity and statistics
- **Contact**: Working contact form with real-time validation

## 📱 Demo

![Portfolio Demo](https://img.shields.io/badge/Status-Live-brightgreen)

### Features Showcase:
- ✨ **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- 🎯 **Contact Form**: Submit messages directly from the website
- 📊 **GitHub Integration**: Live GitHub stats and project showcase
- 🔐 **Admin Panel**: Secure backend for managing submissions

## 🛠️ Technology Stack

- **Backend**: Django 5.2.6
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with modern design patterns
- **Python**: 3.13+

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd django-portfolio
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install django
   ```

4. **Navigate to project directory**:
   ```bash
   cd portfolio
   ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

8. **Run development server**:
   ```bash
   python manage.py runserver
   ```

9. **Access the website**:
   - Portfolio: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

## Project Structure

```
django-portfolio/
├── portfolio/              # Django project directory
│   ├── manage.py          # Django management script
│   ├── portfolio/         # Project settings
│   ├── main/              # Main application
│   │   ├── models.py      # Contact model
│   │   ├── views.py       # View functions
│   │   ├── urls.py        # URL patterns
│   │   ├── admin.py       # Admin configuration
│   │   └── templates/     # HTML templates
│   └── static/            # Static files (CSS, JS)
├── venv/                  # Virtual environment
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Contact Form

The contact form includes:
- Real-time form validation
- AJAX submission (no page reload)
- Success/error message display
- Database storage of all submissions
- Admin interface for viewing messages

## Admin Panel

Access the Django admin panel to:
- View all contact form submissions
- Manage contact entries
- Monitor website activity
- Perform administrative tasks

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Altamash Faraz**
- GitHub: [@altamash-faraz](https://github.com/altamash-faraz)
- LinkedIn: [altamashfaraz](https://www.linkedin.com/in/altamashfaraz/)
- Website: [altamashfaraz.me](https://altamashfaraz.me)

---

Built with ❤️ using Django and modern web technologies.
