import uuid

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import Length, DataRequired
from flask_wtf.file import FileField, FileAllowed


class ProductForm(FlaskForm):
    product_name = StringField('Name:', validators=[DataRequired(), Length(min=1, max=50)])
    product_description = StringField('Description:', validators=[DataRequired(), Length(min=1, max=200)])
    product_price = FloatField('Price:', validators=[])
    product_img = FileField('Image:', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add product')


class ProductFilter(FlaskForm):
    product_price = FloatField('Find product for price', validators=[])
    submit = SubmitField('Find')


class SupermarketForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    location = StringField('Location:', validators=[DataRequired()])
    sup_img = FileField('Image:', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add supermarket')


class SupermarketFilter(FlaskForm):
    location = StringField('Find supermarkets for location', validators=[])
    submit = SubmitField('Find')
