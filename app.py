import streamlit as st
import google.generativeai as genai

# --- 1. AI SETUP (Directly using your new key) ---
# Is key ko maine update kar diya hai taaki aapko koi mehnat na karni pade
API_KEY = "AIzaSyDEgzucVgRbzDb83SUMVX5omqgPRhH22CU"

try:
    genai.configure(api_key=API_KEY)
    # Sabse latest aur fast model 'gemini-1.5-flash' ka istemal
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Setup mein thodi dikkat hai: {e}")

# --- 2. PAGE SETTINGS ---
st.set_page_config(page_title="MyastroAi Hub", layout="wide")

# --- 3. SIDEBAR (UPI & Language) ---
st.sidebar.title("MyastroAi Hub")
lang = st.sidebar.selectbox("Bhasha chunein (Language)", ["Hindi", "English", "Bengali", "Assamese", "Bodo"])

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Premium Payment")
st.sidebar.info("Direct UPI Payment karein")
# Aapka UPI ID yahan hai
st.sidebar.code("My-astroai@ptaxis", language=None)
st.sidebar.write("Payment ke baad screenshot zaroor rakhein.")

# --- 4. MAIN INTERFACE ---
st.title("🌟 Welcome to MyastroAi Hub")
st.write("---")

st.subheader(f"Ask AI in {lang}")
user_input = st.text_input("Apna sawal yahan likhein...")

if st.button("Generate Result"):
    if user_input:
        with st.spinner("MyastroAi soch raha hai..."):
            try:
                # AI ko instruction dena ki wo sahi bhasha mein jawab de
                prompt = f"Answer the following question in {lang} language: {user_input}"
                response = model.generate_content(prompt)
                st.markdown(f"### Jawab:\n{response.text}")
            except Exception as e:
                # Agar koi error aaye toh backup model try karega
                try:
                    backup_model = genai.GenerativeModel('gemini-pro')
                    response = backup_model.generate_content(f"Answer in {lang}: {user_input}")
                    st.markdown(response.text)
                except:
                    st.error("Maaf kijiyega, abhi AI connect nahi ho pa raha hai. Key check karein.")
    else:
        st.warning("Kripya pehle sawal likhein!")

# --- 5. FOOTER ---
st.markdown("---")
st.caption("Powered by MyastroAi Hub | Aapki kamai ka partner")
