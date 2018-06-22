# -*- coding: utf-8 -*-
import re
from flask_wtf import FlaskForm as FlaskForm
from wtforms import StringField, SelectField,\
    SubmitField, PasswordField
from wtforms.validators import Required, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User
from flask_login import current_user

