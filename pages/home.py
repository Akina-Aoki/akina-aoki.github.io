from html import escape
from pathlib import Path

import streamlit as st

from utils.constants import (
    PROFILE_IMAGE,
    ROADMAP_IMAGE,
    STYLES_PATH,
    TECH_STACK_IMAGE,
)
from utils.helpers import image_to_data_uri, load_css


def build_visual_card(
    image_path: Path,
    alt_text: str,
    modifier_class: str,
    mobile_hint: str | None = None,
) -> str:
    """Build a Home visual showcase card, including its missing-file state."""

    safe_alt_text = escape(alt_text, quote=True)
    safe_modifier_class = escape(modifier_class, quote=True)

    if image_path.exists():
        image_uri = escape(image_to_data_uri(image_path), quote=True)
        visual_html = f"""
            <div class="aira-visual-viewport" tabindex="0">
                <img
                    class="aira-visual-image"
                    src="{image_uri}"
                    alt="{safe_alt_text}"
                >
            </div>
        """
    else:
        safe_filename = escape(image_path.name)
        visual_html = f"""
            <div class="aira-file-warning" role="status" aria-live="polite">
                This visual could not be found. Add
                <strong>{safe_filename}</strong> inside the assets folder.
            </div>
        """

    hint_html = ""
    if mobile_hint and image_path.exists():
        hint_html = f'<p class="aira-mobile-hint">{escape(mobile_hint)}</p>'

    return f"""
        <section class="aira-layout-boundary aira-visual-card {safe_modifier_class}">
            {visual_html}
            {hint_html}
        </section>
    """


# Preserve the existing profile-image failure behavior.
if not PROFILE_IMAGE.exists():
    st.error(
        "The profile picture could not be found. Make sure it is saved as "
        "`assets/profile_pic.jpg`."
    )
    st.stop()


profile_image_uri = image_to_data_uri(PROFILE_IMAGE)

roadmap_html = build_visual_card(
    image_path=ROADMAP_IMAGE,
    alt_text="Aira Franco's data engineering competency map",
    modifier_class="aira-competency-card",
    mobile_hint="Swipe horizontally to explore the full map.",
)

tech_stack_html = build_visual_card(
    image_path=TECH_STACK_IMAGE,
    alt_text="Aira Franco Data Engineering Tech Stack Pyramid",
    modifier_class="aira-tech-stack-card",
    mobile_hint="Swipe horizontally to explore the full pyramid.",
)

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

        {roadmap_html}
        {tech_stack_html}
    </main>
    """
)
