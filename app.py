import streamlit as st
import google.generativeai as genai

# --- 1. AI SETUP ---
API_KEY = "AIzaSyDEgzucVgRbzDb83SUMVX5omqgPRhH22CU"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. PREMIUM LOOK & UI SETTINGS ---
st.set_page_config(page_title="MyastroAi Hub", page_icon="✨", layout="wide")

# Custom CSS for Royal Theme
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #000428, #004e92);
        color: white;
    }
    .main-header {
        font-size: 55px;
        font-weight: bold;
        color: #D4AF37; /* Royal Gold */
        text-align: center;
        text-shadow: 2px 2px 10px #000;
        margin-bottom: 10px;
    }
    .sub-header {
        color: #f1f1f1;
        text-align: center;
        font-style: italic;
    }
    .stButton>button {
        background-color: #D4AF37 !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 25px !important;
        border: none !important;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.4);
    }
    .stDownloadButton>button {
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 20px !important;
    }
    .card {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (Premium Sidebar) ---
st.sidebar.markdown("<h2 style='color:#D4AF37; text-align:center;'>👑 MyastroAi Hub</h2>", unsafe_allow_html=True)
lang = st.sidebar.selectbox("Bhasha chunein (Language)", ["Hindi", "English", "Bengali", "Assamese", "Bodo"])

st.sidebar.markdown("---")
st.sidebar.subheader("💎 Premium Payment")
st.sidebar.info("Direct UPI Payment")
st.sidebar.code("My-astroai@ptaxis", language=None)
st.sidebar.write("Scan karne ke liye keybord mic use karein.")

# --- 4. MAIN INTERFACE ---
st.markdown("<div class='main-header'>🌟 MyastroAi Hub 🌟</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Aapka AI Dost - Astro, Business aur Code ka Sathi</div>", unsafe_allow_html=True)
st.write("---")

# Instruction for Voice (Hindi/English Mix for Friendliness)
st.info("🎤 **Dost:** Bol kar baat karne ke liye apne Mobile Keyboard ke **Mic 🎙️** icon par click karein!")

# Tabs for Services
tab1, tab2, tab3 = st.tabs(["🔮 Future AI", "🚀 Business Hub", "💻 Coding Lab"])

with tab1:
    st.markdown("<div class='card'><h3>Astro Prediction & Voice Help</h3></div>", unsafe_allow_html=True)
    astro_input = st.text_area("Yahan sawal likhein ya mic se bole (e.g., Mera bhavishya kaisa hoga?)...", key="astro")
    
    if st.button("Get Astro Report 🔮"):
        if astro_input:
            with st.spinner("Sitara-mandal check ho raha hai..."):
                res = model.generate_content(f"Act as a friendly expert astrologer. Answer in {lang}: {astro_input}")
                st.markdown(f"#### 📜 Aapka Bhavishya:\n{res.text}")
                st.download_button("📥 Download Astro Report", data=res.text, file_name="Astro_Report.txt")
        else:
            st.warning("Pehle sawal toh puchiye dost!")

with tab2:
    st.markdown("<div class='card'><h3>Business & Marketing Strategy</h3></div>", unsafe_allow_html=True)
    biz_input = st.text_area("Business plan ya marketing ke liye bole...", key="biz")
    
    if st.button("Generate Business Plan 🚀"):
        if biz_input:
            with st.spinner("Master plan taiyar ho raha hai..."):
                res = model.generate_content(f"Create a business and marketing strategy in {lang} for: {biz_input}")
                st.write(res.text)
                st.download_button("📥 Download Business Plan", data=res.text, file_name="Business_Plan.txt")

with tab3:
    st.markdown("<div class='card'><h3>Coding & Technical System</h3></div>", unsafe_allow_html=True)
    code_input = st.text_area("Kaunsa code likhna hai? Mic se batayein...", key="code")
    
    if st.button("Generate Code 💻"):
        if code_input:
            with st.spinner("Coding in progress..."):
                res = model.generate_content(f"Write professional code for: {code_input}")
                st.code(res.text)
                st.download_button("📥 Download Source Code", data=res.text, file_name="code_file.py")

# --- 5. FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #D4AF37;'>Handcrafted with ❤️ for Dildar Hussain | © 2026 MyastroAi</p>", unsafe_allow_html=True)
