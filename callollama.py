import requests
import json

def callOLLAMA (user_message):
    #try:
        url = "https://offline-spam-detector.streamlit.app/"
        payload = {
            "model" : "phi3",
            "prompt" : user_message,
            "stream" : False
        }
        response = requests.post(
            url,
            headers = {"content-Type":"application/json"},
            data = json.dumps(payload),
            timeout = 120
        )
        if response.status_code == 200:
            result = response.json()
            bot_response = result.get("response","Sorry, I am unable to help you")
            return bot_response.strip()

        
