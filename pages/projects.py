from html import escape
import streamlit as st

from content.projects import PROJECTS, PROJECTS_BLOG_URL
from utils.constants import STYLES_PATH
from utils.helpers import load_css


def build_project_card(project: dict[str, object]) -> str:
    """Build the accessible anchor markup for one project card."""

    title = escape(str(project["title"]))
    category = escape(str(project["category"]))
    summary = escape(str(project["summary"]))
    icon = escape(str(project["icon"]))
    url = escape(str(project["url"]), quote=True)
    accessible_label = escape(f"Read the {project['title']} project article", quote=True)
    technology_labels = "".join(
        f'<span class="aira-project-technology">{escape(str(technology))}</span>'
        for technology in project["technologies"]
    )

    return (
        f'<a class="aira-project-card" href="{url}" target="_blank" '
        f'rel="noopener noreferrer" aria-label="{accessible_label}">'
        f'<span class="aira-project-icon" aria-hidden="true">{icon}</span>'
        f'<span class="aira-project-category">{category}</span>'
        f'<h2 class="aira-project-title">{title}</h2>'
        f'<p class="aira-project-summary">{summary}</p>'
        f'<span class="aira-project-technologies">{technology_labels}</span>'
        "</a>"
    )


load_css(STYLES_PATH / "projects.css")

projects_html = "".join(
    build_project_card(project)
    for project in PROJECTS
)
blog_url = escape(PROJECTS_BLOG_URL, quote=True)

st.html(
    f"""
    <main class="aira-projects">
        <h1>Data Engineering Projects</h1>
        <p>Each card links to an article describing the project and what I learned.</p>
        <p>
            <a class="aira-projects-journal" href="{blog_url}" target="_blank"
               rel="noopener noreferrer">
                Visit the Data Engineering Journal ↗
            </a>
        </p>
        <div class="aira-projects-grid">
            {projects_html}
        </div>
    </main>
    """
)