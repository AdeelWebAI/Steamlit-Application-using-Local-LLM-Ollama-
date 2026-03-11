import streamlit as st

import ollama

desired_model = "llama3.2:3b"

st.title("Web Application made using Streamlit using locally installed LLM (Ollama)")

def generate_response(questionToAsk):
    try:
        response = ollama.chat(model=desired_model, messages=[{
        "role":"user",
        "content":questionToAsk
        },])
        st.info(response['message']['content'])
    except Exception as e:
        return f"Sorry ! {e}"

with st.form("My_form"):
    text = st.text_area("Enter text","")
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)