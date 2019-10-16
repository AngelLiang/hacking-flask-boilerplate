from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length

# Set your classes here.


class RegisterForm(Form):
    """注册表单"""
    name = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )


class LoginForm(Form):
    """登录表单"""
    name = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])


class ForgotForm(Form):
    """忘记密码表单"""
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
