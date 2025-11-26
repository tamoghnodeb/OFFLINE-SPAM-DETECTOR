import streamlit as st
import datetime as datetime
import requests
import json
from callollama import callOLLAMA
from prompt import prompt

st.set_page_config(
    page_title= 'chatbot'
)

if "messages" not in st.session_state:#if no message is not entered
    st.session_state.messages = []
    st.session_state.messages.append(#after logging in it will display like this
            {
                "role" : "assisstant",
                "content" : "Drop your message. Let me check if it is spam or ham"
            }
        )

if "is_typing" not in st.session_state:#if user is typing something
    st.session_state.is_typing = False

st.title("OFFLINE SCAM DETECTION")
st.markdown("Welcome to AI SMS Scam Detection")

st.subheader("CHAT HERE")

for message in st.session_state.messages: #if there is any new message
    if message["role"] == "user":#if that is a new user
        st.info(message["content"])#it will show it as st.info #by default it will highlight the message in blue
    else:
        st.success(message["content"])#it will show it can be an assistant role #by default it will hightlight the message in green

if st.session_state.is_typing:
    st.markdown ("Bot is typing")
    st.warning ("Typing......")

st.markdown("-------")
st.subheader ("Your message :")

with st.form(key="chat_form",clear_on_submit= True):
    user_input = st.text_input(
        "Type Your Message",
        placeholder="Ask me anything......"
    )
    send_button = st.form_submit_button("send message", type="primary")

col1,col2 = st.columns([1,1])

with col1:
    clear_button = st.button("clear chat")#to clear the chatstreamlit run app.py
    
if send_button and user_input.strip():
    st.session_state.messages.append(
        {
            "role" : "user",
            "content" : user_input.strip()
        }
    )
    #Store full messsage (with prompt) to pass to LLM
    st.session_state.full_user_message = f"{prompt}<|>{user_input.strip()}"
    st.session_state.is_typing = True
    st.rerun()

if st.session_state.is_typing:
    full_user_message = st.session_state.full_user_message
    bot_response = callOLLAMA(full_user_message)#this function will connect to ollama
    st.session_state.messages.append(
        {
            "role" : "assistant",
            "content" : bot_response
        }
    )
    st.session_state.is_typing = False
    st.rerun()

st.markdown("\n\t\tMade by Tamoghno Deb")
