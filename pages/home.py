from collections.abc import Mapping
from html import escape

import streamlit as st

from content.home import COMPETENCY_STAGES, TECH_STACK_LAYERS
from utils.constants import PROFILE_IMAGE, STYLES_PATH
from utils.helpers import image_to_data_uri, load_css


def render_competency_stage(stage: Mapping[str, object]) -> str:
    """Render one competency-map stage as accessible timeline HTML."""

    number = int(stage["number"])
    title = escape(str(stage["title"]))
    skills = "".join(
        f"<li>{escape(str(skill))}</li>" for skill in stage["skills"]
    )

    return f"""
        <li class="aira-timeline-item">
            <div class="aira-timeline-marker">{number}</div>
            <article class="aira-competency-stage">
                <h3>{title}</h3>
                <ul>{skills}</ul>
            </article>
        </li>
    """


def render_stack_layer(layer: Mapping[str, object]) -> str:
    """Render one tech-stack pyramid layer as accessible HTML."""

    level = int(layer["level"])
    title = escape(str(layer["title"]))
    technologies = "".join(
        f'<li class="aira-tech-chip">{escape(str(technology))}</li>'
        for technology in layer["technologies"]
    )

    return f"""
        <li class="aira-stack-layer">
            <article class="aira-stack-card">
                <div class="aira-stack-heading">
                    <span class="aira-stack-level">Level {level}</span>
                    <h3>{title}</h3>
                </div>
                <ul class="aira-tech-chip-list" aria-label="Technologies for {title}">
                    {technologies}
                </ul>
            </article>
        </li>
    """


# Preserve the existing profile-image failure behavior.
if not PROFILE_IMAGE.exists():
    st.error(
        "The profile picture could not be found. Make sure it is saved as "
        "`assets/profile_pic.jpg`."
    )
    st.stop()


profile_image_uri = image_to_data_uri(PROFILE_IMAGE)
competency_timeline_html = "".join(
    render_competency_stage(stage) for stage in COMPETENCY_STAGES
)
tech_stack_html = "".join(render_stack_layer(layer) for layer in TECH_STACK_LAYERS)

load_css(
    STYLES_PATH / "theme.css",
    STYLES_PATH / "home.css",
)

st.html(
    f"""
    <main class="aira-home">
        <section class="aira-layout-boundary aira-hero">
            <article class="aira-profile-card">
                <div class="aira-profile-image-frame">
                    <img
                        class="aira-profile-image"
                        src="{profile_image_uri}"
                        alt="Portrait of Aira Franco"
                    >
                </div>

                <div class="aira-profile-content">
                    <h1 class="aira-profile-name">Hello, I’m Aira 👋</h1>

                    <p class="aira-profile-role">
                        Curious and resilient.
                    </p>

                    <p class="aira-profile-role">
                        I know what it means to be afraid and lost, 
                        but I possess the bravery to push through challenges, 
                        take calculated risks, be patient and start over when it counts.
                    </p>

                    <p class="aira-profile-summary">
                        Growing up between the Philippines and Japan, and later
                        building a new life in Sweden, this huge life moves taught me how to adapt,
                        rebuild connections, learn new languages, and keep
                        moving forward even when the path is uncertain.
                    </p>

                    <p class="aira-profile-summary">
                        Today, I am an aspiring data engineer and a mother of
                        two. I'm pursuing my long-held dream of working in tech, especially in data.
                        <br><br>
                        What defines me is not that every step has been easy,
                        but that I continue to show up. I am willing to begin
                        as a beginner, ask questions, learn from setbacks, and
                        put in the work required to improve.
                    </p>

                    <p class="aira-profile-summary">
                        That persistence now drives my ambition to build
                        reliable data foundations for analytics and AI. I bring
                        resilience, curiosity, attention to detail, and a
                        genuine interest in people to every challenge I take on.
                    </p>

                    <div class="aira-profile-location">📍 Based in Stockholm</div>
                </div>
            </article>
        </section>

        <section class="aira-layout-boundary aira-introduction-card">
            <div class="aira-section-heading">
                <span>The person behind the pipelines</span>
                <span aria-hidden="true">⚙️</span>
            </div>

            <p>
                The data engineering ecosystem evolves incredibly fast, with
                new tools, platforms, and frameworks appearing all the time. 🚀
            </p>

            <p>
                But I believe strong data engineers should understand the
                foundations first: the operational and technical architectures,
                and the <em>whys</em> and <em>hows</em> behind how data is
                collected, stored, modelled, transformed, tested, and delivered
                at different scales.
            </p>

            <p>
                I enjoy being the person behind the scenes—the quiet superhero
                making sure applications, analytics, and machine learning
                models receive reliable, well-structured, and usable data. 🦸‍♀️
            </p>

            <p>
                AI may get the spotlight, but good data engineering is what
                keeps everything running in the background.
            </p>
        </section>

        <section class="aira-layout-boundary aira-competency-roadmap" aria-labelledby="competency-map-heading">
            <div class="aira-native-section-copy">
                <h2 id="competency-map-heading">Aira’s Data Engineering Competency Map</h2>
                <p>
                    This roadmap presents the foundations, practices, and systems
                    developed during Aira’s data-engineering studies and projects.
                </p>
            </div>
            <ol class="aira-timeline">
                {competency_timeline_html}
            </ol>
        </section>

        <section class="aira-layout-boundary aira-tech-stack" aria-labelledby="tech-stack-heading">
            <div class="aira-native-section-copy">
                <h2 id="tech-stack-heading">Data Engineering Tech Stack</h2>
                <p>
                    This stack moves through the layers used to build reliable
                    end-to-end data systems, from delivery experiences down to
                    core foundations.
                </p>
            </div>
            <ol class="aira-stack-list" aria-label="Data engineering tech stack layers">
                {tech_stack_html}
            </ol>
        </section>
    </main>
    """
)
