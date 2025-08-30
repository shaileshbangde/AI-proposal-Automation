import streamlit as st
import openai

st.title('AI Proposal Generator')
input_text = st.text_area('Enter client requirements:')
if st.button('Generate Proposal'):
    st.write('Generated proposal based on:', input_text)