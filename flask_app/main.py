from flask import request, redirect, url_for, render_template,jsonify, flash
from flask_app import app, config
from flask_app.api import main, koubun

@app.route('/')
def show_index():
  return render_template('index.html')

@app.route('/tomowarkar')
def tomowarkar():
  return config.URL
  
@app.route('/api')
def api():
  return main.text

@app.route('/koubun', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    response = koubun.koubun_main(text_input)

    return jsonify(response)