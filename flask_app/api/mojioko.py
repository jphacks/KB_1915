from flask_app import config
import requests
import base64
import json

def mojioko_main(img_url):
    img_base64 = img_to_base64("flask_app/static/img/kb-1915.png")
    # img_base64 = img_url_to_base64(img_url)

    result = request_cloud_vison_api(img_base64)

    text_r = result["responses"][0]["fullTextAnnotation"]["text"]
    return text_r

# APIを呼び、認識結果をjson型で返す
def request_cloud_vison_api(image_base64):
    api_url = config.MURL + config.MKEY
    req_body = json.dumps({
        'requests': [{
            'image': {
                'content': image_base64.decode('utf-8') # jsonに変換するためにstring型に変換する
            },
            'features': [{
                'type': 'TEXT_DETECTION',
                'maxResults': 10,
            }]
        }]
    })
    res = requests.post(api_url, data=req_body)
    return res.json()

# 画像読み込み
def img_to_base64(filepath):
    with open(filepath, 'rb') as img:
        img_byte = img.read()
    return base64.b64encode(img_byte)

def img_url_to_base64(img_url):
    img_con = requests.get(img_url).content
    return base64.b64encode(img_con)