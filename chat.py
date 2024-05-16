import streamlit as st
import env
import hmac
import os

def main():
    if (os.environ['ENV'] != "local"):
        if not check_password():
	        st.stop()  # Do not continue if check_password is not True.
    st.title("Chatbot")
    prompt = st.text_area("Prompt")

    st.session_state['prompt'] = prompt

    submit_btn = st.button('Demander', on_click=on_transcribe_button_clicked)

    if 'result' in st.session_state:
        st.write("Réponse :")
        st.write(st.session_state['result'])

def on_transcribe_button_clicked():
    from main import app,run_app
    result = run_app(app,st.session_state.get('prompt'))
    st.session_state['result'] = result

main()