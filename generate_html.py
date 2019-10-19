

def create_span(word, color):
    return f"<span class='tag-{color}'>{word} </span>"

def g_html_main(r):
  content = ''
  for word_info in r["syntax"]["tokens"]:
    content += create_span(word_info["text"], word_info["part_of_speech"])

  # htmlへのcontent埋め込みと、html作成
  html = f"""
  <!DOCTYPE html>
  <html lang="ja">
  <head>
  <meta charset="utf-8">
  </head>
  <body>
  <div class="output">
  {content}
  </div>
  </body>
  </html>
  """

  with open('templates/index.html', 'wb') as file:
      file.write(html.encode('utf-8'))
