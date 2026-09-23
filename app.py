"""
Panel Kursanta — Streamlit
Uruchomienie:  pip install streamlit  &&  streamlit run app.py
"""
import html
import re
from datetime import datetime

import streamlit as st

# ─────────────────────────────── KONFIGURACJA ───────────────────────────────
st.set_page_config(
    page_title="Panel Kursanta",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

COURSES = {
    "Python": {
        "icon": "🐍",
        "grad": "linear-gradient(135deg,#3776AB 0%,#FFD43B 100%)",
        "accent": "#FFD43B",
        "tagline": "Od skryptów po AI i data science",
        "modules": 12,
        "hours": 48,
    },
    "Java": {
        "icon": "☕",
        "grad": "linear-gradient(135deg,#E76F00 0%,#5382A1 100%)",
        "accent": "#FF9A3C",
        "tagline": "Solidny backend i programowanie obiektowe",
        "modules": 14,
        "hours": 56,
    },
    "SQL": {
        "icon": "🗄️",
        "grad": "linear-gradient(135deg,#00B4DB 0%,#7F00FF 100%)",
        "accent": "#4FD1FF",
        "tagline": "Zapytania, relacje i analiza danych",
        "modules": 8,
        "hours": 32,
    },
}

LEVELS = {
    "początkujący": {"icon": "🌱", "pct": 33, "desc": "Startujesz od podstaw"},
    "średniozaawansowany": {"icon": "⚡", "pct": 66, "desc": "Masz już fundamenty"},
    "zaawansowany": {"icon": "🔥", "pct": 100, "desc": "Wchodzisz na wysoki poziom"},
}

EMAIL_RE = re.compile(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$")

# ─────────────────────────────── SIDEBAR ───────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div class="brand">
            <div class="brand-logo">🎓</div>
            <div>
                <div class="brand-title">CodeAcademy</div>
                <div class="brand-sub">panel kursanta</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="side-label">Kurs</div>', unsafe_allow_html=True)
    course = st.radio(
        "Kurs",
        list(COURSES.keys()),
        format_func=lambda c: f"{COURSES[c]['icon']}  {c}",
        label_visibility="collapsed",
    )
    c = COURSES[course]
    st.markdown(
        f"""
        <div class="course-card" style="background:{c['grad']}">
            <div class="course-card-icon">{c['icon']}</div>
            <div class="course-card-name">{course}</div>
            <div class="course-card-tag">{c['tagline']}</div>
            <div class="course-card-stats">
                <span>📚 {c['modules']} modułów</span>
                <span>⏱️ {c['hours']} h</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

ACCENT = COURSES[course]["accent"]
GRAD = COURSES[course]["grad"]

# ─────────────────────────────── STYLE ───────────────────────────────
st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Inter:wght@400;500;600&display=swap');

:root {{ --accent: {ACCENT}; }}

html, body, [class*="css"], .stMarkdown, input, label, button {{
    font-family: 'Inter', sans-serif !important;
}}

/* animowane tło */
.stApp {{
    background:
        radial-gradient(circle at 15% 20%, rgba(127,0,255,.28) 0%, transparent 40%),
        radial-gradient(circle at 85% 80%, rgba(0,180,219,.25) 0%, transparent 45%),
        radial-gradient(circle at 60% 10%, {ACCENT}22 0%, transparent 35%),
        #0b0d17;
    background-size: 200% 200%;
    animation: bgmove 18s ease-in-out infinite alternate;
    color: #e8eaf6;
}}
@keyframes bgmove {{ 0% {{background-position:0% 0%}} 100% {{background-position:100% 100%}} }}

#MainMenu, footer, header[data-testid="stHeader"] {{ background: transparent; }}
footer {{ visibility: hidden; }}

/* sidebar */
section[data-testid="stSidebar"] {{
    background: rgba(15,17,30,.85);
    backdrop-filter: blur(18px);
    border-right: 1px solid rgba(255,255,255,.07);
}}
.brand {{ display:flex; gap:.8rem; align-items:center; margin:.4rem 0 1.8rem; }}
.brand-logo {{
    width:48px; height:48px; border-radius:14px; display:grid; place-items:center;
    font-size:1.6rem; background:{GRAD}; box-shadow:0 8px 24px {ACCENT}55;
}}
.brand-title {{ font-family:'Space Grotesk'; font-weight:700; font-size:1.25rem; color:#fff; }}
.brand-sub {{ font-size:.75rem; letter-spacing:.14em; text-transform:uppercase; color:#8b90b0; }}
.side-label {{ font-size:.72rem; letter-spacing:.16em; text-transform:uppercase; color:#8b90b0; margin-bottom:.4rem; }}

section[data-testid="stSidebar"] div[role="radiogroup"] label {{
    background: rgba(255,255,255,.04);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 12px; padding: .7rem 1rem; margin-bottom: .45rem; width: 100%;
    transition: all .25s ease;
}}
section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
    transform: translateX(4px); border-color: var(--accent);
}}
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {{
    background: rgba(255,255,255,.1); border-color: var(--accent);
    box-shadow: 0 0 0 1px var(--accent), 0 6px 20px {ACCENT}33;
}}
section[data-testid="stSidebar"] div[role="radiogroup"] p {{ font-size:1.02rem; font-weight:500; }}

.course-card {{
    margin-top:1.4rem; border-radius:20px; padding:1.3rem; color:#fff;
    position:relative; overflow:hidden; box-shadow:0 14px 40px rgba(0,0,0,.45);
    animation: pop .5s cubic-bezier(.2,.9,.3,1.3);
}}
.course-card::after {{
    content:""; position:absolute; inset:0;
    background:linear-gradient(120deg,transparent 30%,rgba(255,255,255,.25) 50%,transparent 70%);
    transform:translateX(-100%); animation: shine 3.5s ease-in-out infinite;
}}
@keyframes shine {{ 60%,100% {{ transform:translateX(100%); }} }}
@keyframes pop {{ from {{ opacity:0; transform:scale(.92) translateY(10px); }} to {{ opacity:1; transform:none; }} }}
.course-card-icon {{ font-size:2.2rem; }}
.course-card-name {{ font-family:'Space Grotesk'; font-size:1.6rem; font-weight:700; text-shadow:0 2px 8px rgba(0,0,0,.3); }}
.course-card-tag {{ font-size:.85rem; opacity:.95; margin:.2rem 0 .9rem; }}
.course-card-stats {{ display:flex; gap:.5rem; flex-wrap:wrap; }}
.course-card-stats span {{
    background:rgba(0,0,0,.25); padding:.3rem .65rem; border-radius:999px; font-size:.78rem;
}}

/* hero */
.hero {{ padding: 1.2rem 0 1.6rem; animation: pop .6s ease; }}
.hero-kicker {{
    display:inline-block; padding:.35rem .9rem; border-radius:999px; font-size:.78rem;
    letter-spacing:.12em; text-transform:uppercase; color:var(--accent);
    background:{ACCENT}18; border:1px solid {ACCENT}55;
}}
.hero h1 {{
    font-family:'Space Grotesk' !important; font-size:3.2rem !important; font-weight:700 !important;
    line-height:1.05 !important; margin:.8rem 0 .4rem !important; padding:0 !important;
    background: linear-gradient(90deg,#fff 0%,var(--accent) 50%,#b388ff 100%);
    background-size:200% auto; -webkit-background-clip:text; background-clip:text;
    -webkit-text-fill-color:transparent; animation: textflow 6s linear infinite;
}}
@keyframes textflow {{ to {{ background-position:200% center; }} }}
.hero p {{ color:#a4a9c9; font-size:1.08rem; max-width:620px; }}

/* formularz = szklana karta */
div[data-testid="stForm"] {{
    background: rgba(255,255,255,.045);
    border: 1px solid rgba(255,255,255,.1);
    border-radius: 24px; padding: 2rem 2rem 1.4rem;
    backdrop-filter: blur(14px);
    box-shadow: 0 20px 60px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.08);
}}
.form-title {{ font-family:'Space Grotesk'; font-size:1.35rem; font-weight:700; color:#fff; margin-bottom:.2rem; }}
.form-sub {{ color:#8b90b0; font-size:.9rem; margin-bottom:1.2rem; }}

div[data-testid="stTextInput"] input {{
    background: rgba(0,0,0,.3) !important; border:1px solid rgba(255,255,255,.12) !important;
    border-radius:12px !important; color:#fff !important; padding:.75rem 1rem !important;
    transition: all .2s ease;
}}
div[data-testid="stTextInput"] input:focus {{
    border-color: var(--accent) !important; box-shadow: 0 0 0 3px {ACCENT}33 !important;
}}
div[data-testid="stTextInput"] label p, div[data-testid="stRadio"] > label p {{
    color:#cfd3ee !important; font-weight:600 !important;
}}

/* poziomy jako kafelki */
div[data-testid="stForm"] div[role="radiogroup"] {{ gap:.7rem; flex-wrap:wrap; }}
div[data-testid="stForm"] div[role="radiogroup"] label {{
    flex:1 1 180px; background: rgba(0,0,0,.25); border:1px solid rgba(255,255,255,.1);
    border-radius:14px; padding:.9rem 1rem; transition: all .25s ease; margin:0;
}}
div[data-testid="stForm"] div[role="radiogroup"] label:hover {{ transform: translateY(-3px); border-color: var(--accent); }}
div[data-testid="stForm"] div[role="radiogroup"] label:has(input:checked) {{
    background: {ACCENT}1f; border-color: var(--accent); box-shadow: 0 8px 24px {ACCENT}30;
}}

/* przycisk */
div[data-testid="stFormSubmitButton"] button {{
    width:100%; border:none !important; border-radius:14px !important; padding:.85rem !important;
    background:{GRAD} !important; color:#fff !important; font-weight:700 !important;
    font-size:1.05rem !important; letter-spacing:.03em; margin-top:.6rem;
    box-shadow: 0 10px 30px {ACCENT}44; transition: all .25s ease;
}}
div[data-testid="stFormSubmitButton"] button:hover {{
    transform: translateY(-2px) scale(1.01); box-shadow: 0 14px 40px {ACCENT}66;
}}

/* karta wyników */
.result {{
    border-radius:24px; padding:2px; background:{GRAD}; margin-top:1.8rem;
    animation: pop .55s cubic-bezier(.2,.9,.3,1.3); box-shadow: 0 20px 60px {ACCENT}33;
}}
.result-inner {{ background:#11131f; border-radius:22px; padding:1.8rem 2rem; }}
.result-head {{ display:flex; align-items:center; gap:1rem; margin-bottom:1.4rem; }}
.avatar {{
    width:64px; height:64px; border-radius:50%; background:{GRAD}; display:grid; place-items:center;
    font-family:'Space Grotesk'; font-weight:700; font-size:1.6rem; color:#fff;
    box-shadow:0 0 0 4px #11131f, 0 0 0 6px var(--accent);
}}
.result-title {{ font-family:'Space Grotesk'; font-size:1.5rem; font-weight:700; color:#fff; }}
.result-date {{ color:#8b90b0; font-size:.85rem; }}
.badge-ok {{
    margin-left:auto; background:#16a34a22; color:#4ade80; border:1px solid #4ade8055;
    padding:.35rem .8rem; border-radius:999px; font-size:.8rem; font-weight:600;
}}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:.9rem; }}
.cell {{
    background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.08);
    border-radius:16px; padding:1rem 1.1rem; transition: all .2s ease;
}}
.cell:hover {{ border-color: var(--accent); transform: translateY(-2px); }}
.cell-label {{ font-size:.72rem; letter-spacing:.14em; text-transform:uppercase; color:#8b90b0; }}
.cell-value {{ font-size:1.12rem; font-weight:600; color:#fff; margin-top:.3rem; word-break:break-all; }}
.progress-wrap {{ margin-top:1.4rem; }}
.progress-label {{ display:flex; justify-content:space-between; color:#a4a9c9; font-size:.85rem; margin-bottom:.4rem; }}
.progress {{ height:10px; background:rgba(255,255,255,.08); border-radius:999px; overflow:hidden; }}
.progress > div {{
    height:100%; background:{GRAD}; border-radius:999px;
    animation: grow 1.2s cubic-bezier(.2,.9,.3,1) forwards;
}}
@keyframes grow {{ from {{ width:0; }} }}

.empty {{
    margin-top:1.8rem; text-align:center; padding:2.2rem; border-radius:24px;
    border:1.5px dashed rgba(255,255,255,.14); color:#8b90b0;
}}
.empty-icon {{ font-size:2.4rem; animation: float 3s ease-in-out infinite; }}
@keyframes float {{ 50% {{ transform: translateY(-8px); }} }}

.stat {{
    background: rgba(255,255,255,.045); border:1px solid rgba(255,255,255,.1);
    border-radius:20px; padding:1.2rem 1.3rem; margin-bottom:.9rem; backdrop-filter: blur(14px);
}}
.stat-num {{ font-family:'Space Grotesk'; font-size:2rem; font-weight:700; color:var(--accent); }}
.stat-lbl {{ color:#a4a9c9; font-size:.88rem; }}
</style>
""",
    unsafe_allow_html=True,
)

# ─────────────────────────────── HERO ───────────────────────────────
st.markdown(
    f"""
    <div class="hero">
        <span class="hero-kicker">{COURSES[course]['icon']} Kurs {course}</span>
        <h1>Twój panel kursanta</h1>
        <p>Uzupełnij swoje dane, wybierz poziom i dołącz do kursu <b style="color:var(--accent)">{course}</b>.
        Twoja karta kursanta pojawi się od razu po zapisaniu.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────── GŁÓWNA CZĘŚĆ ───────────────────────────────
main_col, side_col = st.columns([2.2, 1], gap="large")

with main_col:
    with st.form("student_form", clear_on_submit=False):
        st.markdown(
            '<div class="form-title">📝 Dane kursanta</div>'
            '<div class="form-sub">Wszystkie pola są wymagane</div>',
            unsafe_allow_html=True,
        )
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Imię", placeholder="np. Anna")
        with col2:
            email = st.text_input("E-mail", placeholder="anna@example.com")

        level = st.radio(
            "Poziom",
            list(LEVELS.keys()),
            format_func=lambda l: f"{LEVELS[l]['icon']}  {l}",
            horizontal=True,
        )

        submitted = st.form_submit_button("🚀  Zapisz się na kurs")

    if submitted:
        errors = []
        if not name.strip():
            errors.append("Podaj imię.")
        if not EMAIL_RE.match(email.strip()):
            errors.append("Podaj poprawny adres e-mail.")
        if errors:
            for e in errors:
                st.error(e, icon="⚠️")
        else:
            st.session_state["student"] = {
                "name": html.escape(name.strip()),
                "email": html.escape(email.strip()),
                "course": course,
                "level": level,
                "time": datetime.now().strftime("%d.%m.%Y, %H:%M"),
            }
            st.balloons()
            st.toast(f"Witaj na pokładzie, {name.strip()}! 🎉")

    s = st.session_state.get("student")
    if s:
        cinfo, linfo = COURSES[s["course"]], LEVELS[s["level"]]
        initial = s["name"][0].upper()
        st.markdown(
            f"""
            <div class="result"><div class="result-inner">
                <div class="result-head">
                    <div class="avatar">{initial}</div>
                    <div>
                        <div class="result-title">Dane kursanta</div>
                        <div class="result-date">Zapisano: {s['time']}</div>
                    </div>
                    <span class="badge-ok">✔ aktywny</span>
                </div>
                <div class="grid">
                    <div class="cell"><div class="cell-label">👤 Imię</div><div class="cell-value">{s['name']}</div></div>
                    <div class="cell"><div class="cell-label">✉️ E-mail</div><div class="cell-value">{s['email']}</div></div>
                    <div class="cell"><div class="cell-label">{cinfo['icon']} Kurs</div><div class="cell-value">{s['course']}</div></div>
                    <div class="cell"><div class="cell-label">{linfo['icon']} Poziom</div><div class="cell-value">{s['level']}</div></div>
                </div>
                <div class="progress-wrap">
                    <div class="progress-label"><span>{linfo['desc']}</span><span>{linfo['pct']}%</span></div>
                    <div class="progress"><div style="width:{linfo['pct']}%"></div></div>
                </div>
            </div></div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="empty">
                <div class="empty-icon">✨</div>
                <div>Tu pojawi się Twoja karta kursanta po przesłaniu formularza.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

with side_col:
    ci = COURSES[course]
    for num, lbl in [
        (ci["modules"], "modułów w kursie"),
        (f"{ci['hours']} h", "materiału wideo i ćwiczeń"),
        ("24/7", "dostęp do platformy"),
    ]:
        st.markdown(
            f'<div class="stat"><div class="stat-num">{num}</div><div class="stat-lbl">{lbl}</div></div>',
            unsafe_allow_html=True,
        )
