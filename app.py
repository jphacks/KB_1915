from flask import Flask, render_template, url_for, jsonify, request
import koubun
import generate_html

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/koubun', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    response = koubun.koubun_main(text_input)

    # return jsonify(response)

    generate_html.g_html_main(response)

    return render_template('index.html')
    
# curl -X POST -H 'Content-Type:application/json' http://localhost:8000/koubun -d '{"text":"mario cart is the vest vehicle!!!", "password":"secret"}'