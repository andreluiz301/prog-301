# importações
from flask import Flask, jsonify, request, session, render_template, redirect
# https://stackoverflow.com/questions/70383004/modulenotfounderror-no-module-named-flaskext
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os
import datetime

from flask_cors import CORS, cross_origin  # permitir back receber json do front

# configurações
app = Flask(__name__)

CORS(app)  

# https://flask-cors.readthedocs.io/en/latest/api.html

# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'table.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # remover warnings
db = SQLAlchemy(app)

# https://flask-jwt-extended.readthedocs.io/en/stable/

# importações de JWT
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from datetime import timedelta

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10) #hours=1)
jwt = JWTManager(app)
