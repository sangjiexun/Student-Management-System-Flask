# Configuration settings for Student Management System

class Config:
    # Secret key for Flask application
    SECRET_KEY = 'your-secret-key'
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///student.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Flask-Login configuration
    LOGIN_DISABLED = False
    
    # Flask-WTF configuration
    WTF_CSRF_ENABLED = True
    
    # Application settings
    APP_NAME = 'Student Management System'
    DEBUG = True