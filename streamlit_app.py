import streamlit as st
import database as db

st.set_page_config(page_title="VIP VISHAL", page_icon="👑", layout="wide")
st.markdown("""
<style>.stApp { background: #eaf3ff; }</style>
<div style="text-align:center; padding:20px;">
<img src="https://raw.githubusercontent.com/vipvishal047/-vip-vishal-jaat/main/profile.jpg"
style="width:120px;height:120px;border-radius:50%;border:4px solid white;box-shadow:0 5px 15px rgba(0,0,0,0.3);object-fit:cover;">
<h1 style="color:#0077ff;">VIP VISHAL 👑</h1>
<p style="color:#005fcc;font-weight:700;">ADMIN APPROVAL SYSTEM</p>
</div>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.username = None

def login_page():
    st.markdown("### 🤍 professor - LOGIN")
    t1, t2 = st.tabs(["Login", "Sign-up"])
    with t1:
        u = st.text_input("USERNAME")
        p = st.text_input("PASSWORD", type="password")
        if st.button("LOGIN", use_container_width=True):
            res = db.verify_user(u, p)
            if res == "PENDING":
                st.warning("⏳ ADMIN NE ABHI APPROVE NAHI KIYA HAI. VISHAL SE CONTACT KARO")
            elif res:
                st.session_state.logged_in=True; st.session_state.user_id=res; st.session_state.username=u; st.rerun()
            else: st.error("INVALID LOGIN")
    with t2:
        nu = st.text_input("NEW USERNAME")
        np = st.text_input("NEW PASSWORD", type="password")
        if st.button("CREATE ACCOUNT", use_container_width=True):
            s,m = db.create_user(nu, np)
            if s: st.success(m)
            else: st.error(m)

def main_app():
    st.sidebar.write(f"USER: {st.session_state.username}")
    if st.sidebar.button("LOGOUT"):
        st.session_state.logged_in=False; st.rerun()

    # ADMIN PANEL - SIRF TERE LIYE
    if db.is_admin(st.session_state.user_id):
        st.markdown("### 👑 ADMIN PANEL - APPROVAL REQUESTS")
        pending = db.get_pending_users()
        if not pending:
            st.success("KOI PENDING REQUEST NAHI HAI")
        else:
            for uid, uname in pending:
                c1,c2,c3 = st.columns([2,1,1])
                c1.write(f"👤 {uname}")
                if c2.button("✅ APPROVE", key=f"ap_{uid}"):
                    db.approve_user(uid); st.success(f"{uname} APPROVED"); st.rerun()
                if c3.button("❌ REJECT", key=f"rj_{uid}"):
                    db.reject_user(uid); st.error(f"{uname} REJECTED"); st.rerun()
        st.divider()

    st.markdown("### 🤯 professor - E2EE SERVER")
    cfg = db.get_user_config(st.session_state.user_id)
    if cfg:
        chat_id = st.text_input("E2EE ID", value=cfg['chat_id'])
        name = st.text_input("HATERS NAME", value=cfg['name_prefix'])
        delay = st.number_input("DELAY", 1, 300, value=cfg['delay'])
        cookies = st.text_area("COOKIES", height=100)
        msgs = st.text_area("MESSAGES", value=cfg['messages'], height=200)
        if st.button("💾 SAVE", use_container_width=True):
            final_cookies = cookies if cookies.strip() else cfg['cookies']
            db.update_user_config(st.session_state.user_id, chat_id, name, delay, final_cookies, msgs)
            st.success("SAVED!")

if not st.session_state.logged_in: login_page()
else: main_app()
