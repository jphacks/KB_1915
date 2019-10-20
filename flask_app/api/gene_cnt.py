def create_span(word, color):
  return f"<span class='tag-{color}'>{word}</span>"
  
def gene_cnt_main(res_json):
  content = ''
  for r in res_json:
    content += create_span(r["text"], r["part_of_speech"])
  return content