# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:02:45 2019

@author: mluci
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, Form, validators
from wtforms.validators import DataRequired

### log in form ###
class LoginForm(FlaskForm):
    
    email = PasswordField('Email', validators=[DataRequired()])
    submit = SubmitField('Sign In')
    
### sign up form ###
class RegistrationForm(Form):
    firstname = StringField('First Name', [validators.Length(min=2, max=45)])
    surname = StringField('Surname', [validators.Length(min=2, max=45)])
#    email = StringField('Email Address', [validators.Length(min=3, max=35)])
    email = StringField('Email Address', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Emails must match')
    ])
    confirm = StringField('Repeat Email')