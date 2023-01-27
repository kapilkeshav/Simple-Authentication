from wtforms import (
    StringField,
    BooleanField,
    TextAreaField,
    PasswordField,
    DateField,
    IntegerField
)
from flask_wtf import FlaskForm
from wtforms import validators,ValidationError
from wtforms.validators import InputRequired,Length,Regexp,Email,EqualTo,Optional
from models import User
import email_validator
from flask_login import current_user

class Registration_form(FlaskForm):
    username=StringField(validators=[InputRequired(),Length(3,20,message="Please enter a valid username"),Regexp("^[A-Za-z][A-Za-z0-9_]*$",flags=0,message="Username can only have numbers, letters and _")])
    email = StringField(validators=[InputRequired(),Email(),Length(1,64)])
    pwd = PasswordField(validators=[InputRequired(),Length(8,30)])
    cpwd = PasswordField(validators=[InputRequired(),Length(8,30),EqualTo("pwd",message="Enter same Password")])
    
    def validate_email(self,email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Email Already registered.")
    
    def validate_uname(self,username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("Username alredy exists.")

class Login_form(FlaskForm):
    email = StringField(validators=[InputRequired(),Length(1,64)])
    pwd = PasswordField(validators=[InputRequired(),Length(8,30)])
    username = StringField(validators=[Optional()])