import streamlit as st
import glob

st.set_page_config(page_title="VIP VISHAL OFFICIAL", page_icon="👑", layout="centered")

st.markdown("""
<style>
.stApp { background: #0a0a0a; }
h1, h3 { text-align: center; }
</style>
""", unsafe_allow_html=True)

# Auto photo
photos = glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.png") + glob.glob("*.JPG")
profile_pic = None
for p in photos:
    if "IMG" in p or "WA" in p or "profile" in p.lower():
        profile_pic = p
        break
if not profile_pic and photos:
    profile_pic = photos[0]

if profile_pic:
    st.image(profile_pic, use_container_width=True)
else:
    st.warning("Photo ka naam IMG-20260826-WA0031.jpg rakho")

st.markdown("<h1>🦅 VIP VISHAL 👑 OFFICIAL</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #00ffcc;'>OFFLINE SERVER ONLINE</h3>", unsafe_allow_html=True)
st.write("---")
st.write("Welcome to my official website!")

st.link_button("📸 Instagram", "https://instagram.com/", use_container_width=True)
st.link_button("▶️ YouTube", "https://youtube.com/", use_container_width=True)
st.link_button("💬 WhatsApp", "https://wa.me/", use_container_width=True)
