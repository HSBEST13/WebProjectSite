from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired


class ComplaintForm(FlaskForm):
    name = StringField("Название", validators=[DataRequired()])
    address = StringField("Адрес", validators=[DataRequired()])
    description = TextAreaField("Описание", validators=[DataRequired()])
    add_in_vk = BooleanField("Добавить картинку в группу в вк")
    submit = SubmitField("Подать жалобу")
