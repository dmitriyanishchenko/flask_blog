import wtforms
from wtforms.validators import DataRequired, Email, Length


class LoginForm:
    email = wtforms.StringField("Email: ", validators=[Email()])
    psw = wtforms.PasswordField("Пароль: ", validators=[DataRequired(), Length(min=4, max=100)])
    remember = wtforms.BooleanField("Запомнить", default=False)
    submit = wtforms.SubmitField("Войти")
