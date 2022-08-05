import streamlit as st
from github import Github

mainc = st.container()

with mainc:
  st.header('Image Classifiction')
  g = Github("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")
  x=[]
  repo = g.get_repo("kkumar47/Image_Testing")
  contents = repo.get_contents("Images")
  for content_file in contents:
    content_file = contents.pop(0)
    if content_file.type == "dir":
      contents.extend(repo.get_contents(content_file.path))    
      y = content_file.path[7:]
      x .append((y))
  st.write(x)  
   
  
