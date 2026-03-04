import streamlit as st
import google.generativeai as genai

# --- 1. AI SETUP ---
# अपनी नई (बिना वार्निंग वाली) API Key यहाँ डालें
API_KEY = "AIzaSyDEgzucVgRbzDb83SUMVX5omqgPRhH22CU" 

try:
    genai.configure(api_key=API_KEY)
    # Sabse stable model istemal kar rahe hain
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Setup Error: {e}")

# --- 2. THEME & BRANDING ---
st.set_page_config(page_title="MyastroAi Hub", page_icon="🌟", layout="wide")
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #000428, #004e92); color: white; }
    .main-title { font-size: 55px; color: #D4AF37; text-align: center; font-weight: bold; }
    .payment-card { background: white; color: black; padding: 20px; border-radius: 15px; text-align: center; border: 3px solid #D4AF37; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
st.sidebar.markdown("<h2 style='color:#D4AF37; text-align:center;'>🌟 MyastroAi Hub</h2>", unsafe_allow_html=True)
st.sidebar.info(f"Owner: Chandan Kumar Kakati") #
lang = st.sidebar.selectbox("Bhasha / Language", ["Hindi", "English", "Bengali", "Assamese", "Bodo"]) #

# --- 4. MAIN INTERFACE ---
st.markdown("<div class='main-title'>MyastroAi Hub</div>", unsafe_allow_html=True)
st.write("---")

tab1, tab2, tab3 = st.tabs(["🔮 AI Services", "💳 Payment Center", "📸 Upload Screenshot"])

with tab1:
    st.subheader("Puchiye apna sawal (Astro/Business):")
    st.info("🎤 **Dost Chandan:** Mic use karke sawal bole!") #
    u_input = st.text_area("Yahan likhein ya bole:", key="main_in")
    if st.button("Generate Answer"):
        if u_input:
            with st.spinner("AI is thinking..."):
                try:
                    res = model.generate_content(f"Answer in {lang}: {u_input}")
                    st.write(res.text)
                    st.download_button("📥 Download Result", data=res.text, file_name="MyastroAi_Report.txt") #
                except Exception as e:
                    st.error("AI connect nahi ho raha. Kripya apni API Key check karein.")
        else:
            st.warning("Pehle kuch likhein!")

with tab2:
    st.markdown("<div class='payment-card'>", unsafe_allow_html=True)
    st.subheader("💰 Payment Options")
    # Aapka QR Code
    st.image("https://raw.githubusercontent.com/kakatichandankumar441-pixel/MyastroAi-hub-/main/image.png", width=250)
    upi_id = "My-astroai@ptaxis" #
    pay_url = f"upi://pay?pa={upi_id}&pn=MyastroAi%20Hub&cu=INR"
    st.markdown(f'<a href="{pay_url}" style="background-color:#004e92; color:white; padding:10px 20px; border-radius:25px; text-decoration:none;">Direct UPI Pay 📲</a>', unsafe_allow_html=True)
    st.markdown(f"<p style='color:black; margin-top:10px;'>UPI ID: <b>{upi_id}</b></p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.subheader("📤 Payment Screenshot Proof") #
    st.write("Payment ke baad screenshot upload karein:")
    proof = st.file_uploader("Choose Screenshot Image", type=['png', 'jpg', 'jpeg'])
    if proof:
        st.image(proof, caption="Screenshot Received!", use_container_width=True)
        st.success("Dost Chandan, screenshot mil gaya hai!") #

# --- 5. FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #D4AF37;'>© 2026 MyastroAi Hub | Trusted by Chandan Kumar Kakati</p>", unsafe_allow_html=True) #
