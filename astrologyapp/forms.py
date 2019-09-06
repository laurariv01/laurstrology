from wtforms import Form, validators, StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import input_required, EqualTo,Email
from flask_wtf import FlaskForm 
from flask import Flask, render_template, flash, request 

class RequestForm(FlaskForm):
    email= StringField("Email Address", validators=[input_required()])
    first_name= StringField("First Name", validators=[input_required()])
    last_name=last_name= StringField("Last Name", validators=[input_required()])
    card_select= SelectField(u'Reading request choice', choices=[('35', '3 card reading'), ('50', '5 card reading')])
    comment= StringField('Comment', validators=[input_required()])
    submit = SubmitField()
    
class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    email = StringField("Email", validators=[input_required(), Email()])
    password=PasswordField("Password", validators=[input_required()])
    confirm_pass = PasswordField("Confirm Password", validators=[input_required(),EqualTo('password')])
    submit = SubmitField() 

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    password=PasswordField("Password", validators=[input_required()])
    submit = SubmitField() 
