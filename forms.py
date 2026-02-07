# Form definitions for Student Management System

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, TextAreaField, DateField, FloatField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from models import Class

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=100)])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=50)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=100)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=100)])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[InputRequired()])
    age = IntegerField('Age', validators=[InputRequired()])
    student_id = StringField('Student ID', validators=[InputRequired(), Length(max=20)])
    class_id = SelectField('Class', coerce=int, validators=[InputRequired()])
    email = StringField('Email', validators=[Email(), Length(max=120)])
    phone = StringField('Phone', validators=[Length(max=20)])
    submit = SubmitField('Submit')
    
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.class_id.choices = [(cls.id, cls.name) for cls in Class.query.all()]

class ClassForm(FlaskForm):
    name = StringField('Class Name', validators=[InputRequired(), Length(max=50)])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')

class GradeForm(FlaskForm):
    student_id = SelectField('Student', coerce=int, validators=[InputRequired()])
    subject = StringField('Subject', validators=[InputRequired(), Length(max=50)])
    score = FloatField('Score', validators=[InputRequired()])
    term = SelectField('Term', choices=[('First', 'First'), ('Second', 'Second')], validators=[InputRequired()])
    year = IntegerField('Year', validators=[InputRequired()])
    submit = SubmitField('Submit')
    
    def __init__(self, *args, **kwargs):
        super(GradeForm, self).__init__(*args, **kwargs)
        from models import Student
        self.student_id.choices = [(student.id, f'{student.name} ({student.student_id})') for student in Student.query.all()]