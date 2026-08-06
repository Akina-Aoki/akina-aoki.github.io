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
    url_path="",
    default=True,
)

skills_and_tech_stacks_page = st.Page(
    "pages/skills_and_tech_stacks.py",
    title="Skills & Tech Stacks",
    icon="🧰",
    url_path="skills-and-tech-stacks",
)

projects_page = st.Page(
    "pages/projects.py",
    title="Projects",
    icon="🛠️",
    url_path="projects",
)

personal_take_on_ai_page = st.Page(
    "pages/personal_take_on_ai.py",
    title="My Personal Take on AI",
    url_path="personal-take-on-ai",
)

selected_page = st.navigation(
    [
        home_page,
        skills_and_tech_stacks_page,
        projects_page,
        personal_take_on_ai_page,
    ],
    position="sidebar",
    expanded=True,
)

selected_page.run()
