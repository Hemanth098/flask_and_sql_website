from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateField, MultipleFileField, \
    SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import collections
z = ('60 Seats', '100 Seats ', '120 Seats', '200 Seats', '350 Seats', '500 Seats')
slot=('9:00 am','12:00 pm','3:00pm','6:00pm','9:00pm')
state= list(z)
slot=list(slot)

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
class MarriageForm(FlaskForm):
    username = StringField('name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    number = StringField('Phone Number',validators=[DataRequired()])
    EventDate = DateField('Date Field',validators=[])
    Choose = SelectField('Choose No.of Seats',choices=state)
    ChooseTime = SelectField('Choose Time for Event', choices=slot)
    Anything = TextAreaField('Anything Else',validators=[])
    submit = SubmitField('Book The Slot')

class AdminForm(FlaskForm):

    EventDate = DateField('Date Field',validators=[])
    ChooseTime = SelectField('Choose Time for Event', choices=slot)
    submit = SubmitField('Search')