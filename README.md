Offline SMS Spam/Ham Detection (Streamlit + Local LLM)
A privacy-focused AI SMS Spam/Ham Detection system built using Streamlit and a locally hosted LLM (Ollama + Phi-3).
This project classifies any text message into HAM (normal) or SPAM (scam/promotional) — completely offline, with zero cloud usage.
________________________________________
🚀 Features
•	🔐 100% Offline Processing — No external APIs, no data leaks.
•	🤖 LLM-powered Classification using Phi-3 running on Ollama.
•	💬 Interactive Chat UI made with Streamlit.
•	⏳ Typing Indicator for a chatbot-like experience.
•	📩 High-accuracy Spam Detection using real SMS examples in prompt.
•	📱 Accessible on other devices via local network URL.
________________________________________
🧠 How It Works
1.	User submits a message.
2.	The message (with prompt) is sent to Ollama running locally.
3.	The LLM returns a single label: HAM or SPAM.
4.	Streamlit displays the result in a chat interface.
________________________________________
📂 Project Structure
📁 offline-spam-detector
│
├── app.py           # Main Streamlit app UI + logic
├── callollama.py    # Handles local LLM API requests
├── prompt.py        # Prompt instructions for classification
└── README.md        # Documentation
________________________________________
⚙️ Installation & Setup
1. Install Ollama
Download from: https://ollama.com
2. Pull the Phi-3 model
ollama pull phi3
3. Install Python dependencies
pip install streamlit requests
4. Run the Streamlit app
streamlit run app.py
________________________________________
🌐 Access the App on Other Devices (Same Network)
If Streamlit is running on your system, your app can also be accessed from other devices connected to the same WiFi or LAN.
Your network URL is:
http://10.3.179.65:8501
Open this link on:
•	Your phone
•	Another laptop
•	Any device on the same network
Requirements:
•	Streamlit must be running on the host system
•	All devices must be connected to the same local network
________________________________________
🧪 Example Classification
Message	Output
"Claim your FREE reward now! Click the link!"	SPAM
"Can we meet at 5 PM today?"	HAM
"Your subscription will renew for ₹199. Reply STOP to cancel."	SPAM
"Don't forget tomorrow’s class test."	HAM
________________________________________
📝 Prompt Logic (Summary)
The LLM is guided with:
•	Definitions of SPAM vs HAM
•	10 labeled real SMS examples
•	Strict instruction to output only "HAM" or "SPAM"
This ensures consistent and accurate classification.
________________________________________
💡 Customization
You can modify:
•	The model (phi3, llama3, etc.)
•	The styling of the Streamlit interface
•	The dataset/prompt examples for better classification
________________________________________
👨‍💻 Developer
Made by Tamoghno Deb
Offline AI & LLM Developer ❤️

