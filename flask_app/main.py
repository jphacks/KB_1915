from flask import request, redirect, render_template,jsonify, flash, abort
from flask_app import app, config
from flask_app.api import main, koubun, mojioko, gene_cnt
from flask_app.line_bot_handler import bot

@app.route('/')
def show_index():
  return render_template('index.html')

@app.route('/tomowarkar')
def tomowarkar():
  return config.URL
  
@app.route('/api')
def api():
  return main.text

@app.route('/restest', methods=['POST'])
def res_checko():
  data = request.get_json()
  contents = data['contents']
  dic = {
    'status': 'OK',
    'contents': contents
  }
  return jsonify(dic)

@app.route('/mojioko', methods=['POST'])
def mojioko_img():
    data = request.get_json()
    url_input = data['url']
    text = mojioko.mojioko_main(url_input)

    return text

@app.route('/koubun', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    response = koubun.koubun_main(text_input)

    return jsonify(response)

# @app.route('/api/v1', methods=['POST'])
# def api_v1():
#   data = request.get_json()
#   url_input = data['url']
#   text = mojioko.mojioko_main(url_input)
#   # return text
#   res = koubun.koubun_main(text)
#   # return jsonify(res)
#   cnt = gene_cnt.gene_cnt_main(res)
  
#   return render_template('index.html', cnt=cnt)