# Resume Download Instructions

## Google Drive Resume Setup

Your Google Drive link: https://drive.google.com/file/d/11tuThjdCpe5aDvRnwL2U-z_9GlD_jRKj/view?usp=drive_link

### Method 1: Direct Download (Recommended)
1. Change the Google Drive URL from:
   `https://drive.google.com/file/d/11tuThjdCpe5aDvRnwL2U-z_9GlD_jRKj/view?usp=drive_link`
   
   To:
   `https://drive.google.com/uc?export=download&id=11tuThjdCpe5aDvRnwL2U-z_9GlD_jRKj`

2. Open this direct download URL in your browser
3. Download the PDF file
4. Save it as "Altamash_Faraz_Resume.pdf" in the media/resumes/ folder

### Method 2: Manual Download
1. Open the original Google Drive link
2. Click "Download" button in Google Drive
3. Save the file as "Altamash_Faraz_Resume.pdf"
4. Copy it to: D:\Portfolio\django portfolio\media\resumes\

### Method 3: PowerShell Download (if public)
Run this command in PowerShell:
```powershell
Invoke-WebRequest -Uri "https://drive.google.com/uc?export=download&id=11tuThjdCpe5aDvRnwL2U-z_9GlD_jRKj" -OutFile "media\resumes\Altamash_Faraz_Resume.pdf"
```

### After downloading:
1. Run the Django server: `python manage.py runserver`
2. Go to http://127.0.0.1:8000/admin/
3. Add a new Resume entry with the uploaded PDF file
4. Set it as active to display on your portfolio