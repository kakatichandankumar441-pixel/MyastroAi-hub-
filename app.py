import streamlit as st
import google.generativeai as genai

# --- 1. AI SETUP ---
# आपकी लेटेस्ट API Key यहाँ सेट कर दी है
API_KEY = "AIzaSyDEgzucVgRbzDb83SUMVX5omqgPRhH22CU"

try:
    genai.configure(api_key=API_KEY)
    # एरर फिक्स करने के लिए 'gemini-1.5-flash' का इस्तेमाल किया है
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Setup Error: {e}")

# --- 2. PAGE SETTINGS ---
st.set_page_config(page_title="MyastroAi Hub", layout="wide")

# --- 3. SIDEBAR (UPI & Language) ---
st.sidebar.title("MyastroAi Hub")
lang = st.sidebar.selectbox("Language / ভাষা / भाषा", ["Hindi", "English", "Bengali", "Assamese", "Bodo"])

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Premium Payment")
st.sidebar.info("Direct UPI Payment")
# आपका UPI ID यहाँ साफ़ दिखेगा
st.sidebar.code("My-astroai@ptaxis", language=None)
st.sidebar.write("पेमेंट के बाद स्क्रीनशॉट सुरक्षित रखें।")

# --- 4. MAIN INTERFACE ---
st.title("🌟 Welcome to MyastroAi Hub")
st.write("---")

st.subheader(f"Ask AI in {lang}")
user_input = st.text_input("अपना सवाल यहाँ लिखें...")

if st.button("Generate Result"):
    if user_input:
        with st.spinner("MyastroAi सोच रहा है..."):
            try:
                # AI को निर्देश देना
                prompt = f"Answer in {lang}: {user_input}"
                response = model.generate_content(prompt)
                st.markdown(f"### जवाब:\n{response.text}")
            except Exception as e:
                # अगर नया मॉडल फेल हो तो पुराना मॉडल ट्राई करेगा
                try:
                    backup_model = genai.GenerativeModel('gemini-pro')
                    response = backup_model.generate_content(f"Answer in {lang}: {user_input}")
                    st.markdown(response.text)
                except:
                    st.error("AI मॉडल कनेक्ट नहीं हो पा रहा है। कृपया कुछ देर बाद कोशिश करें।")
    else:
        st.warning("कृपया पहले कुछ लिखें!")

# --- 5. FOOTER ---
st.markdown("---")
st.caption("Powered by MyastroAi Hub")
