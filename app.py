import streamlit as st
from multipage import MultiPage
import form
import result
import global_var
from PIL import Image

st.set_page_config(page_title='Loan', page_icon=':tiger:', layout='wide')
img = Image.open('/Users/shirleywang/desktop/webapp/pic.jpg')

col1, mid, col2 = st.columns([1,5,25])
with col1:
    st.image(img,width = 120)
with col2:
    st.markdown('<h1 style="color: orange;">Loan Application Assistant</h1>', unsafe_allow_html=True)


app = MultiPage()

app.add_page('User Info', form.app)
app.add_page('Predicted Result', result.app)

if __name__ == '__main__':
    global_var._init()
    app.run()
