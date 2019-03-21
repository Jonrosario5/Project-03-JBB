from flask_wtf import FlaskForm as Form

from models import User
from models import Topic

from wtforms import StringField, PasswordField, TextAreaField, DateTimeField, BooleanField, SelectMultipleField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                               Length, EqualTo)
from wtforms.fields.html5 import DateTimeField



def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User with that name already exists.')


def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exists.')

class RegisterForm(Form):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message=("Username should be one word, letters, "
                         "numbers, and underscores only.")
            ),
            name_exists
        ])
    fullname = StringField(
        "Fullname",
        validators=[DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Passwords must match')
        ])
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()]
    )


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class TopicForm(Form):
    name = StringField('Name',validators=[DataRequired()])

class EventForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    details = StringField('Details', validators=[DataRequired()])

class User_Topics(Form):
    topics = SelectMultipleField('Topics', choices=[('JS','Javascript'),('PY','Python')])
    can_help = BooleanField('Can Help')
