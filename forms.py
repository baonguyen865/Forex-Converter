from wtforms import StringField, FloatField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class ConverterForm(FlaskForm):
    base_currency = StringField("Converting From", validators=[InputRequired()])
    converted_currency = StringField("Converting To", validators=[InputRequired()])
    amount = FloatField("Amount", validators=[InputRequired()])