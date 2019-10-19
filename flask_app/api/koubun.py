from flask_app import config
import requests
import json
import urllib

def set_req_params(text, keywordNum):
    params = {
        'features': {
            'keywords': {
                'limit': keywordNum,
            },
            'syntax': {
                'sentences': True,
                'tokens': {
                    'lemma': True,
                    'part_of_speech': True
                }
            }
        },
        'text': text
    }
    return json.dumps(params,indent=4)


def koubun_main(text):
    headers = {'Content-Type': 'application/json'}
    params = set_req_params(text, 1000)

    r = requests.post(config.KURL, data=params, headers=headers, auth=(config.KUSER, config.KPSW)).json()
    return r
