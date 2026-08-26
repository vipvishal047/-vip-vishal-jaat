import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="VIP ¢нαυ∂ꀍαяу ѵ𝚒﹩ʰa̶ℓ ʝâαt",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# BACKGROUND
# =========================

def set_background():
    image = Path(__file__).parent / "bg.jpg"

    if image.exists():
        encoded = base64.b64encode(
            image.read_bytes()
        ).decode()

        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image:
                    linear-gradient(
                        rgba(3, 3, 15, 0.78),
                        rgba(10, 0, 25, 0.82)
                    ),
                    url("data:image/jpeg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

set_background()

# =========================
# DARK NEON STYLE
# =========================

st.markdown(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=Orbitron:wght@600;700;800;900&display=swap'
    );

    * {
        font-family: 'Orbitron', sans-serif !important;
    }

    .main .block-container {
        background: rgba(4, 5, 18, 0.82);
        border: 1px solid rgba(0, 229, 255, 0.35);
        border-radius: 25px;
        padding: 35px;
        box-shadow:
            0 0 35px rgba(0, 229, 255, 0.12),
            0 0 50px rgba(180, 0, 255, 0.08);
    }

    .hero {
        text-align: center;
        padding: 45px 20px;
        border-radius: 25px;
        background:
            linear-gradient(
                135deg,
                rgba(0, 20, 40, 0.95),
                rgba(35, 0, 50, 0.95)
            );
        border: 1px solid #00eaff;
        box-shadow:
            0 0 25px rgba(0, 234, 255, 0.25),
            inset 0 0 25px rgba(255, 0, 200, 0.08);
    }

    .hero h1 {
        color: #6ffaff;
        font-size: 42px;
        text-shadow:
            0 0 10px #00eaff,
            0 0 25px #8b00ff;
    }

    .hero p {
        color: #ff5be7;
        font-size: 15px;
        letter-spacing: 3px;
    }

    .card {
        background: rgba(3, 10, 25, 0.90);
        border: 1px solid rgba(0, 234, 255, 0.30);
        border-radius: 18px;
        padding: 25px;
        margin-top: 20px;
        box-shadow: 0 0 20px rgba(0, 234, 255, 0.08);
    }

    .neon-title {
        color: #72f7ff;
        font-size: 22px;
        text-shadow: 0 0 10px #00eaff;
    }

    .stButton > button {
        background: linear-gradient(
            135deg,
            #009dff,
            #8500ff
        );
        color: white;
        border: 1px solid #5ffaff;
        border-radius: 12px;
        font-weight: 800;
        box-shadow: 0 0 18px rgba(0, 200, 255, 0.25);
    }

    .stButton > button:hover {
        box-shadow:
            0 0 25px rgba(0, 234, 255, 0.55);
        transform: translateY(-2px);
    }

    .stTextInput input,
    .stTextArea textarea {
        background: rgba(2, 8, 20, 0.95) !important;
        color: white !important;
        border: 1px solid rgba(0, 234, 255, 0.40) !important;
        border-radius: 10px !important;
    }

    label {
        color: #72f7ff !important;
        font-weight: 700 !important;
    }

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                rgba(2, 4, 15, 0.98),
                rgba(20, 0, 35, 0.98)
            );
        border-right: 1px solid rgba(0, 234, 255, 0.25);
    }

    .footer {
        text-align: center;
        color: #72f7ff;
        margin-top: 35px;
        padding: 20px;
        text-shadow: 0 0 10px #00eaff;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# HEADER
# =========================

st.markdown(
    """
    <div class="hero">
        <h1>🦅 VIP VISHAL</h1>
        <p>DARK NEON CONTROL PANEL</p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# SIDEBAR
# =========================

st.sidebar.markdown("## 🦅 VIP PANEL")

st.sidebar.write("⚡ SYSTEM: ONLINE")
st.sidebar.write("🟢 STATUS: ACTIVE")
st.sidebar.write("🔒 MODE: SECURE")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "MENU",
    [
        "🏠 Dashboard",
        "⚙️ Settings",
        "📊 Console"
    ]
)

# =========================
# DASHBOARD
# =========================

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="card">'
        '<div class="neon-title">⚡ DASHBOARD</div>'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "SYSTEM",
            "ONLINE"
        )

    with col2:
        st.metric(
            "STATUS",
            "ACTIVE"
        )

    with col3:
        st.metric(
            "MODE",
            "NEON"
        )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("🚀 Welcome")

    st.write(
        "Dark neon Streamlit dashboard successfully loaded."
    )

    st.info(
        "Background image ke liye bg.jpg isi folder mein rakho."
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

# =========================
# SETTINGS
# =========================

elif page == "⚙️ Settings":

    st.markdown(
        '<div class="card">'
        '<div class="neon-title">⚙️ SETTINGS</div>'
        '</div>',
        unsafe_allow_html=True
    )

    username = st.text_input(
        "USERNAME",
        placeholder="Enter username"
    )

    title = st.text_input(
        "PROFILE TITLE",
        value="VIP VISHAL"
    )

    description = st.text_area(
        "DESCRIPTION",
        value="Dark Neon Control Panel"
    )

    if st.button(
        "💾 SAVE SETTINGS",
        use_container_width=True
    ):
        st.success("Settings saved successfully.")

# =========================
# CONSOLE
# =========================

elif page == "📊 Console":

    st.markdown(
        '<div class="card">'
        '<div class="neon-title">📊 SYSTEM CONSOLE</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.code(
        "[ONLINE] System started\n"
        "[OK] Neon interface loaded\n"
        "[OK] Background checked\n"
        "[READY] Dashboard is running",
        language="text"
    )

    if st.button(
        "🔄 REFRESH",
        use_container_width=True
    ):
        st.rerun()

# =========================
# FOOTER
# =========================

st.markdown(
    """
    <div class="footer">
        🦅 VIP VISHAL OFFICIAL
        <br>
        ⚡ DARK NEON SYSTEM
        <br>
        🇮🇳 MADE IN INDIA
    </div>
    """,
    unsafe_allow_html=True
        )
