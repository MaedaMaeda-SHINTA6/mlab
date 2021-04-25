"""
create app
"""

from flask import Flask, session
from flask_bootstrap import Bootstrap
from flask_session import Session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24) #セッションキーを生成する
bootstrap = Bootstrap(app)

import project.controller
