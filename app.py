import streamlit as st
import google.generativeai as genai

# --- 1. AI Setup (यहाँ अपनी API Key डालें) ---
# अपनी फ्री API Key 'aistudio.google.com' से लें
genai.configure(api_key="AIzaSyDdliDBmDHDgbs00EzmuP6JAwLGUYXnr3g")
model = genai.GenerativeModel('gemini-pro')

# --- 2. UI Configuration ---
st.set_page_config(page_title="AI Multi-Tool Hub", layout="wide")

# मल्टी-लैंग्वेज ड्रॉपडाउन
lang = st.sidebar.selectbox("Language / ভাষা / ভাষা", ["English", "Hindi", "Bengali", "Assamese" "Hindlish"])

# --- 3. Sidebar: Payment & QR ---
st.sidebar.title("💰 Premium Access")
st.sidebar.image("image.png", caption="Scan & Pay to My-astroai@ptaxis")
st.sidebar.write("UPI ID: `My-astroai@ptaxis`")
st.sidebar.info("पेमेंट के बाद स्क्रीनशॉट भेजें।")

# --- 4. Main AI Interface ---
st.title("🚀 Smart AI Assistant")
user_query = st.text_area(f"Ask anything in {lang} / कुछ भी पूछें:")

if st.button("Generate Response"):
    if user_query:
        with st.spinner("AI सोच रहा है..."):
            # AI को निर्देश देना कि वह चुनी हुई भाषा में जवाब दे
            prompt = f"Answer the following question in {lang} language: {user_query}"
            response = model.generate_content(prompt)
            st.markdown("### AI Response:")
            st.write(response.text)
    else:
        st.warning("कृपया पहले कुछ लिखें!")

# --- 5. Future Options (Tabs) ---
tab1, tab2 = st.tabs(["📊 Business Plan", "💻 Custom Coding"])
with tab1:
    st.write("अपना बिजनेस आइडिया यहाँ लिखें, AI प्लान बना देगा।")
with tab2:
    st.write("कोडिंग प्रोजेक्ट्स के लिए यहाँ रिक्वेस्ट करें।")
  
