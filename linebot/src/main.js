'use strict'

const express = require('express');
const line = require('@line/bot-sdk');
const serverless = require('serverless-http');
const request = require('request');
const axios = require('axios')
// const fs = require('fs');
// const fileType = require('file-type');
const toDataURL = require("toDataURL");


const app = express();

const config = {
    channelSecret: '6d0d6f41f477ba2a88db6575716c3bca',
    channelAccessToken: 'hhFEbmbRuL9L6vtIj6A6wYweV9HXyLek8Kck7oUOxoERVY96QGvQAqAoUBvITgU8Dwg2b5uQZgxFQh+0JY4UDjpW9pS8wccWRqAf+SrqjqOkcy378T1Trk9i4CzdIWHEhyPBo+9Eyf/f2YZJ5lfFtAdB04t89/1O/w1cDnyilFU='
};

const router = express.Router(); //ルーティング用に追加
router.get('/', (req, res) => {
  res.send('<h1>HELLO</h1><p>what!!</p>')
});

router.post('/webhook', line.middleware(config), (req, res) => {
    Promise.all(req.body.events.map(handleEvent)).then((result) => res.json(result));
});



const client = new line.Client(config);
async function handleEvent(event) {
    if(event.message.type == 'image'){
      if(event.message.contentProvider.type == 'line'){
        //base64に変換
        const dataURL = await (async () => new Promise((resolve, reject) => {
          request.get(`https://api.line.me/v2/bot/message/${event.message.id}/content`, {
            encoding: null,
            headers: {
              Authorization: `Bearer ${config.channelAccessToken}`
            },
          }, (error, response, body) => {
            try{
              const buffer = new Buffer.from(body)
              const arrayBuffer = Uint8Array.from(buffer).buffer
              const unit8array = new Uint8Array(arrayBuffer)
              const dataURL = toDataURL.toDataURL(unit8array)
              resolve(dataURL)
            }catch(e){
              reject(e)
            }
          })
        }))()
        

        //単語リストを返す
        //テスト用データ（本来はAPIを呼び出し、以下のようなJSONデータが得られる）
        const apiResponse = {
          contents: "Yet better thus , and known to be contemn 'd , Than still contemn " +
          "'d and flatter 'd . To be worst , The lowest and most dejected " +
          'thing offortune , Stands still inesperance , lives not infear : ' +
          'The lamentable change is fromthe best ; The worst returns ' +
          'tolaughter . Welcome , then , Thou unsubstantial air that l ' +
          'embrace ! The wretch that thou hast blown untothe worst Owes ' +
          'nothing tothy blasts . But who comes here ? Enter GLOUCESTER , ' +
          'led byan Old Man My father , poorly led ? World , world , Oworld ' +
          '! But that thy strange mutations make us hate thee , Life would ' +
          'not yield to age .',
          koubun: [
            {
              word: "to",
              "word-jp": "〜へ",
              tag: "tag-PART",
              prop: 1,
            },
            {
              word: "be",
              "word-jp": "なる",
              tag: "tag-AUX",
              prop: 1,
            },
            {
              word: "worst",
              "word-jp": "最悪な",
              tag: "tag-ADJ",
              prop: 8,
            },
            {
              word: "the",
              "word-jp": "その",
              tag: "tag-DET",
              prop: 1,
            },
            {
              word: "lowest",
              "word-jp": "最低の",
              tag: "tag-ADJ",
              prop: 8,
            },
            {
              word: "and",
              "word-jp": "そして",
              tag: "tag-CCONJ",
              prop: 2,
            },
            {
              word: "most",
              "word-jp": "最も",
              tag: "tag-ADV",
              prop: 7,
            },
            {
              word: "dejected",
              "word-jp": "落胆した",
              tag: "tag-ADJ",
              prop: 7,
            },
            {
              word: "thing",
              "word-jp": "もの",
              tag: "tag-NOUN",
              prop: 5,
            },
            {
              word: "of",
              "word-jp": "の", 
              tag: "rag-ADP",
              prop: 2,
            },
            {
              word: "fortune",
              "word-jp": "幸運",
              tag: "tag-NOUN",
              prop: 8,
            },
            {
              word: ",",
              "word-jp": "",
              tag: "tag-PUNCT",
              prop: 1,
            }
          ]
        }

        const keywords = apiResponse.koubun.filter(({prop}) => 3 <= prop && prop <= 7).reduce((acc, {word, ["word-jp"]:wordJP}, i) => acc + `\n${i+1}. ${word}  ${wordJP}`, "")
        
        //返信
        return client.replyMessage(event.replyToken, [{
          type: 'text',
          text: '[重要単語一覧]\n' + keywords
        },{
          type: 'text',
          text: '[全文]\n' + apiResponse.contents,
        },{
          type: 'text',
          text: '品詞を確認する \nline://app/1653356140-RbV4rVmO'
        }])
      }
    }
    return client.replyMessage(event.replyToken, {
        type: 'text',
        text: '画像ではありません',
      })
}

app.use('/.netlify/functions/main', router); //ルーティング追加
module.exports = app; //追加
module.exports.handler = serverless(app); //追加