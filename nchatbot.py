import streamlit as st
import google.generativeai as genai

# Configure the API key
GOOGLE_API_KEY = "AIzaSyDcjePxmsbrfGEtjFJUn0bZIuJaIftU48o"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Generative Model
# model = genai.GenerativeModel('gemini-pro')
model = genai.GenerativeModel('gemini-1.5-flash')
# Function to get response from the model
def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit interface
st.set_page_config(page_title="Simple ChatBot", layout="centered")

st.title("✨ Simple ChatBot ✨")
st.write("Powered by Google Generative AI")

if "history" not in st.session_state:
    st.session_state["history"] = []

# Display chat history


# user_input = input("Enter your Prompt = ")
# output = get_chatbot_response(user_input)

# print(output)

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000)
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = get_chatbot_response(user_input)
            st.session_state.history.append((user_input, response))
        else:
            st.warning("Please Enter A Prompt")