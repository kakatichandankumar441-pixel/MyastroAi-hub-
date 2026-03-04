import streamlit as st
import google.generativeai as genai

# --- 1. AI SETUP ---
# अपनी API Key यहाँ डालें
API_KEY = "AIzaSyDdliDBmDHDgbs00EzmuP6JAwLGUYXnr3g" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# --- 2. PAGE SETTINGS ---
st.set_page_config(page_title="MyastroAi Hub", layout="wide")

# --- 3. SIDEBAR (UPI & Language) ---
st.sidebar.title("MyastroAi Hub")

# भाषा का चुनाव
lang = st.sidebar.selectbox("Language / ভাষা / भाषा", ["English", "Hindi", "Bengali", "Assamese", "Bodo","Hinglish"])

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Premium Payment")

# QR हटाकर सिर्फ UPI ID ऐड किया गया है
st.sidebar.info("Direct UPI Payment")
st.sidebar.code("My-astroai@ptaxis", language=None)
st.sidebar.write("पेमेंट करने के बाद यहाँ स्क्रीनशॉट अपलोड करें:")

# स्क्रीनशॉट अपलोड ऑप्शन
proof = st.sidebar.file_uploader("Upload Screenshot", type=['png', 'jpg', 'jpeg'])
if proof:
    st.sidebar.success("Verification in progress!")

# --- 4. MAIN INTERFACE ---
st.title("🌟 Welcome to MyastroAi Hub")
st.write("---")

# AI Chat Section
st.subheader(f"Ask AI in {lang}")
user_input = st.text_input("Type your question here...")

if st.button("Generate Result"):
    if user_input:
        with st.spinner("Processing..."):
            prompt = f"Answer in {lang}: {user_input}"
            response = model.generate_content(prompt)
            st.markdown(response.text)
    else:
        st.warning("Please enter something first!")
