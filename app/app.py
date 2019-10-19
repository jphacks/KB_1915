from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策

@app.route('/')
def index_get():
    return render_template('index.html')

@app.route('/api/v1', methods=['POST'])
def post_json():
    json = request.get_json()  # POSTされたJSONを取得
    return jsonify(json)  # JSONをレスポンス
@app.route('/api/v1', methods=['GET'])
def get_json_from_dictionary():
    dic = {
        'foo': 'bar',
        'ほげ': 'ふが'
    }
    return jsonify(dic)  # JSONをレスポンス