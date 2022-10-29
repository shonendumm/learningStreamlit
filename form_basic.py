
import streamlit as st

def basic_input():
    checked = st.checkbox('yes')

    if checked == True:
        st.write("You checked true!")

    if st.button('Click'):
        st.write("You clicked!")

    gender = st.radio('Pick your gender',['Male','Female']) 

    if gender == 'Male':
        st.write('You are male')
    elif gender == 'Female':
        st.write('You are female')

    st.selectbox('Pick your food',['Meat','Fish'])
    st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
    st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
    st.slider('Pick a number', 0,50)