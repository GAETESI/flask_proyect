from flask import Flask
import re

app = Flask(__name__) 
app.secret_key = "secret"   

BASE_DATOS = "esquema_revistas"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NOMBRE_REGEX = re.compile(r'^[A-Z]{1}[a-zA-Z]+$')