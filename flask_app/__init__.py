from flask import Flask

app = Flask(__name__)
app.config.from_object('flask_app.config')
app.config['JSON_AS_ASCII'] = False
import flask_app.main
