from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteKunden(FlaskForm):
    KundenID = HiddenField("KundenID")
