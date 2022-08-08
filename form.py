from ftplib import error_reply
from logging import error
from msilib.schema import Error
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from  wtforms import Form, BooleanField, StringField,  validators,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length,Email, DataRequired, ValidationError
from sqlalchemy.dialects.postgresql import UUID


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class CustomerForm(FlaskForm):
    name = StringField('name',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    d_o_b=StringField('d_o_b',[DataRequired()])
    phone_number=StringField('Phone_number',[DataRequired()])
    NYSC=StringField('NYSC',[DataRequired()])
    BVN=StringField('BVN',[validators.length(11) ])
    submit = SubmitField('Sign Up')
    def validate_username(self, name):
        user = user.query.filter_by(name=name.data).first()
        if user:
            raise ValidationError('That name is taken. Please choose a different one.')
    def validate_email(self, email):
        user = user.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
    def validate_d_o_b(self, d_o_b):
        user = user.query.filter_by(d_o_b=d_o_b.data).first()
        if user:
            raise ValidationError('That d_o_b is Incorrect. Please choose a different one.')
  
    def validate_BVN(self, BVN):
        user = user.query.filter_by(BVN=BVN.data).first()
        if user:
            raise ValidationError('That BVN is Incorrect. Please choose a different one.')
    
    def validate_Submit(self, Submit):
        form = CustomerForm()
        if form.validate_on_submit():
            nysc=form.NYSC.data, email=form.email.data



    @app.route('/CustomerForm')
    def user(CustomerForm):
         return CustomerForm

   
              
    
       
def profiles(Self_employment ):
        if  Self_employment:
            raise Exception("Not Employed")
            profiles_query = profiles.query.filter_by(type=self_employment).first()
            return profiles_query.point

  
   

def BNPL_products(NYSC):
    if "yes":
        raise ValidationError('That this should be handled by Payfi)')
    



