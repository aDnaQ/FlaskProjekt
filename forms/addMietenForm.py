from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import TextAreaField
from wtforms.fields import SelectField


YEAR_CHOICES = (
    ("1990", "1990"),
    ("1995", "1995"),
    ("2000", "2000"),
    ("2005", "2005"),
    ("2010", "2010"),
    ("2015", "2015"),
    ("2020", "2020"),
    ("2022", "2022"),
)


class AddMietwagen(FlaskForm):
    Farbe = SelectField("Farbe")
    kmStand = TextAreaField("kmStand")
    Leistung = TextAreaField("Leistung")
    Erstzulasung = DateField("Erstzulassung")
    Kennzeichen = TextAreaField("Kennzeichen")
    Baujahr = SelectField("Baujahr", choices=YEAR_CHOICES, default='2022')