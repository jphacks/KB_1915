import requests
import json
import urllib

user = 'apikey'
psw = 'M1B7dStQw49nyso4bFPfkEFMGPasiWiYUY3asQOwTT8M'
url = 'https://gateway-tok.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2018-11-16'

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

    r = requests.post(url, data=params, headers=headers, auth=(user, psw)).json()
    return r

# print(koubun_main("Peter Piper picked a peck of pickled peppers.A peck of pickled peppers Peter Piper picked.If Peter Piper picked a peck of pickled peppers,Where’s the peck of pickled peppers Peter Piper picked?")["syntax"]["tokens"])
# 