# imports
from html import escape

import streamlit as st

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
    f"""
    <main class="aira-home">

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
                        Curious and resilient.
                        \n

                    </p>

                    <p class="aira-profile-role">
                        I know what it means to be afraid and lost, 
                        but I possess the bravery to push through challenges, 
                        take calculated risks, be patient and start over when it counts.
                        \n
                    </p>

                    <p class="aira-profile-summary">
                        Growing up between the Philippines and Japan, and later
                        building a new life in Sweden, this huge life moves taught me how to adapt,
                        rebuild connections, learn new languages, and keep
                        moving forward even when the path is uncertain.
                        \n\n
                    </p>

                    <p class="aira-profile-role">
                    \n
                    </p>

                    <p class="aira-profile-summary">
                        Today, I am an aspiring data engineer and a mother of
                        two. I'm pursuing my long-held dream of working in tech, especially in data.
                        \n\n
                        What defines me is not that every step has been easy,
                        but that I continue to show up. I am willing to begin
                        as a beginner, ask questions, learn from setbacks, and
                        put in the work required to improve.
                        \n\n
                    </p>

                    <p class="aira-profile-role">
                    \n
                    </p>

                    <p class="aira-profile-summary">
                        That persistence now drives my ambition to build
                        reliable data foundations for analytics and AI. I bring
                        resilience, curiosity, attention to detail, and a
                        genuine interest in people to every challenge I take on.
                    </p>

                    
                    <p class="aira-profile-role">
                    \n
                    </p>

                    <div class="aira-profile-location">
                        📍 Based in Stockholm
                    </div>

                </div>

            </article>

            <nav
                class="aira-profile-links"
                aria-label="Aira Franco's professional links"
            >
                {links_html}
            </nav>

        </section>


        <!-- Personal introduction -->

        <section class="aira-introduction-card">

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


        <!-- Competency roadmap image -->

        {roadmap_html}

    </main>
    """
)
