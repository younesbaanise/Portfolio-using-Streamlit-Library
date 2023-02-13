import streamlit as ml
from PIL import Image


ml.set_page_config(
    page_title = "portfolio | Younes Baanise"
)

# HEADER SECTION 
image = Image.open('images/picture.png')
ml.image(image, width=400)
ml.write("##")
with ml.container():
    ml.title("Hi,")
    ml.title("I'm younes,")
    ml.title("web developer")
