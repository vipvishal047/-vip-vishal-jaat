import streamlit as st
import time
import threading
import base64
from dataclasses import dataclass, field
from pathlib import Path
import database as db

st.set_page_config(
    page_title="VIP ¢нαυ∂ꀍαяу ѵ𝚒﹩ʰa̶ℓ ʝâαt",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# BACKGROUND IMAGE
# =========================

def add_background():
    image_path = Path(__file__).parent / "bg.jpg"

    if not image_path.exists():
        return

    encoded = base64.b64encode(
        image_path.read_bytes()
    ).decode("utf-8")

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(
                    rgba(0,0,12,0.72),
                    rgba(4,0,18,0.76)
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

add_background()

# =========================
# DARK NEON CSS
# =========================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Outfit:wght@300;400;500;600;700;800;900&display=swap'
);

* {
    font-family: 'Outfit', sans-serif !important;
}

.stApp {
    background-color: #050510 !important;
    color: #f4f7ff !important;
}

.main .block-container {
    background: rgba(4, 5, 18, 0.78) !important;
    border: 1px solid rgba(0, 229, 255, .28);
    border-radius: 26px;

    box-shadow:
        0 0 45px rgba(0, 229, 255, .08),
        inset 0 0 30px rgba(177, 0, 255, .04);

    backdrop-filter: blur(10px);
}

.main-header {
    background:
        linear-gradient(
            135deg,
            rgba(5,10,28,.94),
            rgba(25,3,40,.90)
        );

    border: 1px solid rgba(0,229,255,.45);
    border-radius: 24px;

    padding: 42px 25px;
    text-align: center;

    box-shadow:
        0 0 30px rgba(0,229,255,.18),
        0 0 55px rgba(255,0,190,.10);

    margin-bottom: 25px;
}

.main-header h1 {
    color: #72f7ff !important;

    font-family: 'Orbitron', sans-serif !important;

    font-size: 2.8rem;
    font-weight: 900;

    text-shadow:
        0 0 12px #00eaff,
        0 0 30px rgba(255,0,200,.55);
}

.main-header p {
    color: #ff66df !important;

    font-weight: 700;
    letter-spacing: 2px;

    text-shadow:
        0 0 10px rgba(255,0,200,.6);
}

.stTextInput>div>div>input,
.stTextArea>div>div>textarea,
.stNumberInput input {

    background: rgba(2,7,20,.92) !important;

    color: #eafcff !important;

    border: 1px solid rgba(0,229,255,.55) !important;

    border-radius: 12px !important;

    box-shadow:
        inset 0 0 12px rgba(0,229,255,.05);
}

.stTextInput>div>div>input:focus,
.stTextArea>div>div>textarea:focus {

    border-color: #ff35d1 !important;

    box-shadow:
        0 0 14px rgba(255,53,209,.35) !important;
}

label {
    color: #79efff !important;
    font-weight: 700 !important;
}

.stButton>button {

    background:
        linear-gradient(
            135deg,
            #00bfff,
            #7a00ff
        ) !important;

    color: white !important;

    border: 1px solid #68f8ff !important;

    border-radius: 13px !important;

    font-weight: 800 !important;

    box-shadow:
        0 0 18px rgba(0,229,255,.25),
        0 0 30px rgba(150,0,255,.18);

    transition: .2s ease;
}

.stButton>button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 0 24px rgba(0,229,255,.5),
        0 0 35px rgba(255,0,210,.3);
}

[data-testid="stMetric"] {

    background: rgba(4,8,24,.84);

    border: 1px solid rgba(0,229,255,.35);

    border-radius: 16px;

    padding: 14px;

    box-shadow:
        0 0 18px rgba(0,229,255,.09);
}

[data-testid="stMetricLabel"] {
    color: #b9a5ff !important;
}

[data-testid="stMetricValue"] {

    color: #72f7ff !important;

    text-shadow:
        0 0 12px rgba(0,229,255,.55);
}

.stTabs [data-baseweb="tab-list"] {

    background: rgba(4,5,18,.85);

    border: 1px solid rgba(126,0,255,.35);

    border-radius: 15px;

    padding: 6px;
}

.stTabs [data-baseweb="tab"] {

    color: #cbbdff !important;

    border-radius: 11px;

    font-weight: 700;
}

.stTabs [aria-selected="true"] {

    background:
        linear-gradient(
            135deg,
            #007fff,
            #9d00ff
        ) !important;

    color: white !important;

    box-shadow:
        0 0 18px rgba(157,0,255,.4);
}

.console-output {

    background: rgba(1,4,12,.95);

    border: 1px solid #00eaff;

    border-radius: 15px;

    padding: 18px;

    box-shadow:
        0 0 25px rgba(0,229,255,.12),
        inset 0 0 25px rgba(0,0,0,.45);
}

.console-line {

    background: rgba(8,16,35,.88);

    color: #bafaff;

    padding: 9px 11px;

    border-left: 3px solid #ff35d1;

    border-radius: 5px;

    margin-bottom: 7px;

    font-family: monospace !important;
}

.success-box {

    background: rgba(0,255,170,.08) !important;

    border: 1px solid #00ffb2;

    color: #54ffd0 !important;

    border-radius: 12px;

    box-shadow:
        0 0 18px rgba(0,255,178,.12);

}

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            rgba(3,5,18,.98),
            rgba(15,3,29,.98)
        ) !important;

    border-right:
        1px solid rgba(0,229,255,.28);
}

section[data-testid="stSidebar"] * {
    color: #e9e6ff !important;
}

hr {
    border-color:
        rgba(0,229,255,.25) !important;
}

</style>
""", unsafe_allow_html=True)


# =========================
# AUTOMATION STATE
# =========================

@dataclass
class AutomationState:
    running: bool = False
    message_count: int = 0
    logs: list = field(default_factory=list)


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "username" not in st.session_state:
    st.session_state.username = None

if "automation_state" not in st.session_state:
    st.session_state.automation_state = AutomationState()


# =========================
# LOGGING
# =========================

def log_message(message):

    state = st.session_state.automation_state

    state.logs.append(
        f"[{time.strftime('%H:%M:%S')}] {message}"
    )

    state.logs = state.logs[-100:]


# =========================
# DEMO AUTOMATION
# =========================

def start_demo_automation(user_id):

    state = st.session_state.automation_state

    if state.running:
        return

    state.running = True
    state.message_count = 0
    state.logs = []

    db.set_automation_running(
        user_id,
        True
    )

    def worker():

        try:

            for _ in range(10):

                if not state.running:
                    break

                state.message_count += 1

                state.logs.append(
                    f"[{time.strftime('%H:%M:%S')}] "
                    f"Demo task #{state.message_count} completed"
                )

                state.logs = state.logs[-100:]

                time.sleep(2)

        finally:

            state.running = False

            db.set_automation_running(
                user_id,
                False
            )

    threading.Thread(
        target=worker,
        daemon=True
    ).start()


def stop_automation(user_id):

    st.session_state.automation_state.running = False

    db.set_automation_running(
        user_id,
        False
    )

    log_message("Automation stopped.")


# =========================
# LOGIN PAGE
# =========================

def login_page():

    st.markdown("""
    <div class="main-header">

        <h1>
            🦅 VIP VISHAL OFFICIAL
        </h1>

        <p>
            DARK NEON SECURE SERVER
        </p>

    </div>
    """, unsafe_allow_html=True)


    login_tab, signup_tab = st.tabs(
        [
            "🔐 LOGIN",
            "👤 SIGN-UP"
        ]
    )


    with login_tab:

        username = st.text_input(
            "USERNAME",
            key="login_username"
        )

        password = st.text_input(
            "PASSWORD",
            key="login_password",
            type="password"
        )


        if st.button(
            "⚡ LOGIN",
            use_container_width=True
        ):

            if not username or not password:

                st.warning(
                    "Please enter both username and password."
                )

            else:

                user_id = db.verify_user(
                    username,
                    password
                )

                if user_id:

                    st.session_state.logged_in = True

                    st.session_state.user_id = user_id

                    st.session_state.username = username

                    st.success(
                        f"Welcome back, {username}!"
                    )

                    st.rerun()

                else:

                    st.error(
                        "Invalid username or password."
                    )


    with signup_tab:

        new_username = st.text_input(
            "CHOOSE USERNAME",
            key="signup_username"
        )

        new_password = st.text_input(
            "CHOOSE PASSWORD",
            key="signup_password",
            type="password"
        )

        confirm = st.text_input(
            "CONFIRM PASSWORD",
            key="confirm_password",
            type="password"
        )


        if st.button(
            "👑 CREATE ACCOUNT",
            use_container_width=True
        ):

            if not new_username or not new_password or not confirm:

                st.warning(
                    "Please fill all fields."
                )

            elif new_password != confirm:

                st.error(
                    "Passwords do not match."
                )

            else:

                success, message = db.create_user(
                    new_username,
                    new_password
                )

                if success:
                    st.success(message)
                else:
                    st.error(message)


# =========================
# MAIN DASHBOARD
# =========================

def main_app():

    state = st.session_state.automation_state


    st.markdown("""
    <div class="main-header">

        <h1>
            🤯 VIP VISHAL OFFICIAL
        </h1>

        <p>
            ✦ DARK NEON CONTROL PANEL ✦
        </p>

    </div>
    """, unsafe_allow_html=True)


    st.sidebar.markdown(
        "## 👤 USER DASHBOARD"
    )

    st.sidebar.write(
        f"**USERNAME:** {st.session_state.username}"
    )

    st.sidebar.write(
        f"**USER ID:** {st.session_state.user_id}"
    )


    st.sidebar.markdown(
        """
        <div class="success-box">
            👑 PREMIUM ACCESS
            <br>
            ⚡ VIP MEMBER
        </div>
        """,
        unsafe_allow_html=True
    )


    if st.sidebar.button(
        "🚪 LOGOUT",
        use_container_width=True
    ):

        stop_automation(
            st.session_state.user_id
        )

        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.session_state.username = None

        st.rerun()


    config = db.get_user_config(
        st.session_state.user_id
    )


    if not config:

        st.warning(
            "No configuration found."
        )

        return


    setup_tab, automation_tab = st.tabs(
        [
            "⚙️ E2EE SET-UP",
            "🚀 AUTOMATION"
        ]
    )


    with setup_tab:

        st.subheader(
            "⚡ E2EE SET-UP"
        )


        col1, col2 = st.columns(2)


        with col1:

            chat_id = st.text_input(
                "E2EE CONVERSATION ID",
                value=config.get(
                    "chat_id",
                    ""
                )
            )


            name_prefix = st.text_input(
                "NAME PREFIX",
                value=config.get(
                    "name_prefix",
                    ""
                )
            )


            delay = st.number_input(
                "DELAY (SECONDS)",
                min_value=1,
                max_value=300,
                value=int(
                    config.get(
                        "delay",
                        5
                    )
                )
            )


        with col2:

            messages = st.text_area(
                "MESSAGES",
                value=config.get(
                    "messages",
                    ""
                ),
                height=220,
                placeholder="One item per line"
            )


        st.info(
            "Security note: this version does not collect "
            "Facebook session cookies or automate unsolicited "
            "platform messaging."
        )


        if st.button(
            "💾 SAVE E2EE SETTINGS",
            use_container_width=True
        ):

            db.update_user_config(
                st.session_state.user_id,
                chat_id,
                name_prefix,
                delay,
                config.get(
                    "cookies",
                    ""
                ),
                messages
            )

            st.success(
                "Settings saved successfully."
            )

            st.rerun()


    with automation_tab:

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "⚡ TASKS COMPLETED",
                state.message_count
            )


        with col2:

            st.metric(
                "STATUS",
                "🟢 RUNNING"
                if state.running
                else
                "🔴 STOPPED"
            )


        with col3:

            value = config.get(
                "chat_id",
                ""
            )

            display_id = (
                value[:10] + "..."
                if len(value) > 10
                else value
            )

            st.metric(
                "🆔 CHAT ID",
                display_id or "NOT SET"
            )


        st.divider()


        c1, c2 = st.columns(2)


        with c1:

            if st.button(
                "▶️ START AUTOMATION",
                disabled=state.running,
                use_container_width=True
            ):

                start_demo_automation(
                    st.session_state.user_id
                )

                st.success(
                    "Automation started."
                )

                st.rerun()


        with c2:

            if st.button(
                "⏹️ STOP AUTOMATION",
                disabled=not state.running,
                use_container_width=True
            ):

                stop_automation(
                    st.session_state.user_id
                )

                st.warning(
                    "Automation stopped."
                )

                st.rerun()


        if state.logs:

            st.subheader(
                "📊 LIVE CONSOLE OUTPUT"
            )


            html = """
            <div class="console-output">
            """


            for line in state.logs[-30:]:

                html += f"""
                <div class="console-line">
                    {line}
                </div>
                """


            html += """
            </div>
            """


            st.markdown(
                html,
                unsafe_allow_html=True
            )


            if st.button(
                "🔄 REFRESH LOGS",
                use_container_width=True
            ):

                st.rerun()


# =========================
# APP START
# =========================

if not st.session_state.logged_in:
    login_page()
else:
    main_app()


# =========================
# FOOTER
# =========================

st.markdown(
    """
    <div style="
        text-align:center;
        margin-top:2rem;
        color:#72f7ff;
        font-weight:800;
        text-shadow:0 0 12px #00eaff;
    ">
        🦅 MADE IN INDIA 🇮🇳
        &nbsp; | &nbsp;
        VIP VISHAL OFFICIAL
        &nbsp; | &nbsp;
        ⚡ DARK NEON SYSTEM
    </div>
    """,
    unsafe_allow_html=True
)
Filename: Streamlit_app.py
Aur same folder mein bg.jpg hona chahiye.
