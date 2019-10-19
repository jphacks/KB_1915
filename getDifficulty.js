//APIキー M1B7dStQw49nyso4bFPfkEFMGPasiWiYUY3asQOwTT8M
//https://gateway-tok.watsonplatform.net/natural-language-understanding/api


curl -X POST -u "apikey:M1B7dStQw49nyso4bFPfkEFMGPasiWiYUY3asQOwTT8M" \
"https://gateway-tok.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2018-11-16" \
--header "Content-Type: application/json" \
--data '{
  "language":"en",
  "text": "I ate an apple.",
  "features": {
    "syntax":{
      "tokens": {
        "lemma": true,
        "part_of_speech": true
      }
    }
  }
}'
