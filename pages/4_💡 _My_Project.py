import streamlit as st
from PIL import Image
# ---- LOAD ASSETS ----
img_project1 = Image.open("images/project1.jpg")
img_project2 = Image.open("images/project2.png")
img_project3 = Image.open("images/project3.png")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project1)
    with text_column:
        st.subheader("Building a Restaurant Website: An HTML, CSS, and JavaScript Guide")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project2)
    with text_column:
        st.subheader("Tasting the World: A Recipe, Food, and Drink Website")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project3)
    with text_column:
        st.subheader(" weather app that displays the current weather for a given location.")