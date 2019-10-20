def create_span(word, color):
  return f"<span class='tag-{color}'>{word} </span>"
  
# def gene_cnt_main(res_json):
#   content = ''
#   for r in res_json:
#     content += create_span(r["text"], r["part_of_speech"])
#   return content

def gene_cnt_main(res_json):
  content = ''
  for r in res_json:
    content += create_span(r["text"], r["part_of_speech"])
  html = f"""
  <!DOCTYPE html>
  <html>
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>KyoRits English</title>
      <link rel="stylesheet" type="text/css" href="../static/css/style.css">
    </head>
    <body>
      <div class="cnt">
        {content}
      </div>
      <script src="https://static.line-scdn.net/liff/edge/2.1/sdk.js"></script>
      <script src="liff-starter.js"></script>
    </body>
  </html>
  """
  with open('./flask_app/templates/liff.html', 'wb') as file:
    file.write(html.encode('utf-8'))

  return content