# Main application file for Student Management System

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# Initialize Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import models
from models import User, Student, Class, Grade, Attendance

# Import forms
from forms import LoginForm, RegistrationForm, StudentForm, ClassForm, GradeForm

# Import routes
from routes import *

# Login manager callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Main function
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
        
        # Create admin user (if not exists)
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', email='admin@example.com', password='admin123', role='admin')
            db.session.add(admin)
            db.session.commit()
        
        # Create sample classes (if not exists)
        if not Class.query.first():
            classes = [
                Class(name='Class 1A', description='First year, A section'),
                Class(name='Class 1B', description='First year, B section'),
                Class(name='Class 2A', description='Second year, A section'),
                Class(name='Class 2B', description='Second year, B section'),
                Class(name='Class 3A', description='Third year, A section')
            ]
            for cls in classes:
                db.session.add(cls)
            db.session.commit()
        
        # Create sample students (if not exists)
        if not Student.query.first():
            students = [
                Student(name='John Doe', gender='Male', age=15, student_id='S001', class_id=1, email='john@example.com', phone='1234567890'),
                Student(name='Jane Smith', gender='Female', age=14, student_id='S002', class_id=1, email='jane@example.com', phone='0987654321'),
                Student(name='Mike Johnson', gender='Male', age=15, student_id='S003', class_id=2, email='mike@example.com', phone='1122334455'),
                Student(name='Sarah Williams', gender='Female', age=14, student_id='S004', class_id=2, email='sarah@example.com', phone='5544332211'),
                Student(name='David Brown', gender='Male', age=16, student_id='S005', class_id=3, email='david@example.com', phone='9988776655')
            ]
            for student in students:
                db.session.add(student)
            db.session.commit()
    
    app.run(debug=True)