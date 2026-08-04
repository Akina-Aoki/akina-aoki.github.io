from html import escape
import streamlit as st

from content.profile import MAIN_BLOG_URL
from content.projects import CAPSTONE_PROJECTS_URL, PROJECTS
from utils.constants import STYLES_PATH
from utils.helpers import load_css


def build_project_card(project: dict[str, object]) -> str:
    """Build the accessible anchor markup for one project card."""

    title = escape(str(project["title"]))
    category = escape(str(project["category"]))
    summary = escape(str(project["summary"]))
    url = escape(str(project["url"]), quote=True)
    accessible_label = escape(f"Read the {project['title']} project article", quote=True)
    technology_labels = "".join(
        f'<span class="aira-project-technology">{escape(str(technology))}</span>'
        for technology in project["technologies"]
    )

    return (
        f'<a class="aira-project-card" href="{url}" target="_blank" '
        f'rel="noopener noreferrer" aria-label="{accessible_label}">'
        f'<h2 class="aira-project-category">{category}</h2>'
        f'<h3 class="aira-project-title">{title}</h3>'
        f'<p class="aira-project-summary">{summary}</p>'
        f'<span class="aira-project-technologies">{technology_labels}</span>'
        "</a>"
    )


load_css(
    STYLES_PATH / "theme.css",
    STYLES_PATH / "projects.css",
)

projects_html = "".join(
    build_project_card(project)
    for project in PROJECTS
)
main_blog_url = escape(MAIN_BLOG_URL, quote=True)
capstone_projects_url = escape(
    CAPSTONE_PROJECTS_URL,
    quote=True,
)

st.html(
    f"""
    <main class="aira-projects">
        <h1>Projects &amp; Blogs</h1>
        <p>
            This page brings together my writing and Data Engineering coursework.
        </p>

        <section class="aira-main-blog">
            <h2 class="aira-main-blog-label">Main Blog</h2>
            <p>
                Visit my main Hashnode profile for my broader writing, learning
                notes, and project reflections.
            </p>
            <a class="aira-main-blog-link" href="{main_blog_url}"
               target="_blank" rel="noopener noreferrer">
                Visit my main blog ↗
            </a>
        </section>

        <section class="aira-capstone-projects"
                 aria-labelledby="capstone-projects-heading">
            <div class="aira-capstone-projects-header">
                <h2 id="capstone-projects-heading">
                    Data Engineering Capstone Projects
                </h2>
                <p>
                    Explore the capstone projects completed during my Data
                    Engineering programme. Each card opens the full project article.
                </p>
                <a class="aira-capstone-projects-link"
                   href="{capstone_projects_url}" target="_blank"
                   rel="noopener noreferrer">
                    View the complete capstone collection ↗
                </a>
            </div>
            <div class="aira-projects-grid">
                {projects_html}
            </div>
        </section>
    </main>
    """
)
