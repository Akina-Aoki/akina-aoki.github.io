# imports
from html import escape

import streamlit as st


# =========================================================
# Project paths
# =========================================================

from utils.constants import PROFILE_IMAGE, ROADMAP_IMAGE, STYLES_PATH
from utils.helpers import image_to_data_uri, load_css

# =========================================================
# External links
# =========================================================

GITHUB_URL = "https://github.com/Akina-Aoki"

BLOG_URL = "https://hashnode.com/@Aira"
LINKEDIN_URL = "https://www.linkedin.com/in/aira-franco0965/"


# =========================================================
# Helper functions
# =========================================================

def create_link_button(
    label: str,
    icon: str,
    url: str,
) -> str:
    """Create an enabled or disabled portfolio link button."""

    clean_url = url.strip()

    if clean_url:
        safe_url = escape(clean_url, quote=True)
        safe_label = escape(label)

        return f"""
        <a
            class="aira-link-button"
            href="{safe_url}"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="{safe_label}"
        >
            <span class="aira-link-icon">{icon}</span>
            <span class="aira-link-label">{safe_label}</span>
            <span class="aira-link-arrow">↗</span>
        </a>
        """

    return f"""
    <div
        class="aira-link-button aira-link-disabled"
        title="Add the URL inside home.py"
    >
        <span class="aira-link-icon">{icon}</span>
        <span class="aira-link-label">{escape(label)}</span>
        <span class="aira-link-arrow">Soon</span>
    </div>
    """


# =========================================================
# Validate profile image
# =========================================================

if not PROFILE_IMAGE.exists():
    st.error(
        "The profile picture could not be found. Make sure it is saved as "
        "`assets/profile_pic.jpg`."
    )
    st.stop()


profile_image_uri = image_to_data_uri(PROFILE_IMAGE)


# =========================================================
# External link buttons
# =========================================================

links_html = "".join(
    [
        create_link_button(
            label="GitHub Projects",
            icon="💻",
            url=GITHUB_URL,
        ),
        create_link_button(
            label="Data Engineering Blog",
            icon="✍️",
            url=BLOG_URL,
        ),
        create_link_button(
            label="LinkedIn",
            icon="💼",
            url=LINKEDIN_URL,
        ),
    ]
)


# =========================================================
# Roadmap section
# =========================================================

if ROADMAP_IMAGE.exists():
    roadmap_image_uri = image_to_data_uri(ROADMAP_IMAGE)

    roadmap_html = f"""
    <section class="aira-roadmap-card">

        <div class="aira-roadmap-viewport">
            <img
                class="aira-roadmap-image"
                src="{roadmap_image_uri}"
                alt="Aira Franco's data engineering competency map"
            >
        </div>

        <p class="aira-mobile-hint">
            Swipe horizontally to explore the full map.
        </p>

    </section>
    """

else:
    roadmap_html = """
    <section class="aira-roadmap-card">

        <div class="aira-file-warning">
            The roadmap image could not be found. Add
            <strong>roadmap.png</strong> inside the assets folder.
        </div>

    </section>
    """


# =========================================================
# Complete homepage
# =========================================================

load_css(STYLES_PATH / "home.css")

st.html(
    f"""<main class="aira-home">


        <!-- Profile and links -->

        <section class="aira-hero">

            <article class="aira-profile-card">

                <img
                    class="aira-profile-image"
                    src="{profile_image_uri}"
                    alt="Portrait of Aira Franco"
                >

                <div class="aira-profile-content">

                    <h1 class="aira-profile-name">
                        Hello, I’m Aira 👋
                    </h1>

                    <p class="aira-profile-role">
                        Courageous and curios.
                        I have never been afraid to take a calculated risk or start again.
                        \n  
                    </p>
@@ -658,26 +240,26 @@ st.html(
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


        <!-- Competency roadmap image -->

        {roadmap_html}


    </main>
    """
)