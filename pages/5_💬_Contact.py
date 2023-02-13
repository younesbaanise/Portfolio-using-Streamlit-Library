import streamlit as st

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/main.css")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("let's connect soon!")
    st.subheader("My address email: baaniseyounes@gmail.com")
    st.subheader("github: https://github.com/younesbaanise")
    st.write("##")
    contact_form ='''
    <form>
     <input type="text" name="name" placeholder="enter your name" required>
     <input type="email" name="email"  placeholder="enter your email" required>
     <textarea name="message" placeholder="enter your message here" required></textarea>
     <button type="submit">submit</button>
</form>
    '''
left_column, right_column = st.columns(2)
with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
        st.empty()

