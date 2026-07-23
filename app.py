import streamlit as st

st.set_page_config(
    page_title="Aira Franco | Data Engineer",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

home_page = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠",
    default=True,
)

resume_page = st.Page(
    "pages/resume.py",
    title="Resume",
    icon="📄",
)

projects_page = st.Page(
    "pages/projects.py",
    title="Projects",
    icon="🛠️",
)

selected_page = st.navigation(
    [
        home_page,
        resume_page,
        projects_page,
    ],
    position="sidebar",
    expanded=True,
)

selected_page.run()