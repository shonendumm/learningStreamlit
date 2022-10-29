import streamlit as st
import form_basic
from form_advanced import advanced_input

st.write("Hello Soo Hian, let's learn to build streamlit apps together!")

st.title ("this is the app title")
st.header("this is the header")
st.markdown("this is the markdown")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')


form_basic.basic_input()
advanced_input()



