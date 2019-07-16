from flask import Flask

app = Flask(__name__)
from mysite import routes
