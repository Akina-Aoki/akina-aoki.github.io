from base64 import b64encode
from html import escape
from mimetypes import guess_type
from pathlib import Path

import streamlit as st


# =========================================================
# Project paths
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

PROFILE_IMAGE = PROJECT_ROOT / "assets" / "profile_pic.jpg"
ROADMAP_IMAGE = PROJECT_ROOT / "assets" / "roadmap.png"


# =========================================================
# External links
# =========================================================

GITHUB_URL = "https://github.com/Akina-Aoki"

# Add your real URLs when ready.
BLOG_URL = "https://hashnode.com/@Aira"
LINKEDIN_URL = "https://www.linkedin.com/in/aira-franco0965/"


# =========================================================
# Helper functions
# =========================================================

def image_to_data_uri(image_path: Path) -> str:
    """Convert a local image into a Base64 data URI."""

    mime_type = guess_type(image_path.name)[0] or "image/jpeg"
    encoded_image = b64encode(image_path.read_bytes()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded_image}"


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

st.html(
    f"""
    <style>

        /* -----------------------------------------------
           Main Streamlit page spacing
        ------------------------------------------------ */

        [data-testid="stMainBlockContainer"] {{
            width: 100%;
            max-width: 1200px;

            padding-top: 2rem;
            padding-right: 2.5rem;
            padding-bottom: 5rem;
            padding-left: 2.5rem;
        }}


        /* -----------------------------------------------
           Shared homepage layout
        ------------------------------------------------ */

        .aira-home {{
            width: min(100%, 1040px);
            margin: 0 auto;

            display: flex;
            flex-direction: column;
            gap: 32px;

            box-sizing: border-box;
        }}


        /* -----------------------------------------------
           Profile area
        ------------------------------------------------ */

        .aira-hero {{
            width: min(100%, 540px);
            margin: 0 auto;

            display: flex;
            flex-direction: column;
            gap: 14px;
        }}

        .aira-profile-card {{
            width: 100%;
            padding: 18px;
            overflow: hidden;
            box-sizing: border-box;

            background: #f8fafc;
            border: 1px solid rgba(148, 163, 184, 0.30);
            border-radius: 34px;

            box-shadow:
                0 25px 60px rgba(15, 23, 42, 0.14),
                0 5px 16px rgba(15, 23, 42, 0.07);
        }}

        .aira-profile-image {{
            display: block;
            width: 100%;
            aspect-ratio: 4 / 3;

            object-fit: cover;
            object-position: center 25%;

            border-radius: 25px;
        }}

        .aira-profile-content {{
            padding: 26px 12px 12px;
            color: #111827;
        }}

        .aira-profile-name {{
            margin: 0 0 12px;

            font-size: 2.2rem;
            font-weight: 800;
            line-height: 1.12;
            letter-spacing: -0.04em;
        }}

        .aira-profile-role {{
            max-width: 470px;
            margin: 0 0 15px;

            color: #334155;
            font-size: 1.08rem;
            font-weight: 650;
            line-height: 1.55;
        }}

        .aira-profile-summary {{
            max-width: 470px;
            margin: 0;

            color: #526174;
            font-size: 1rem;
            line-height: 1.7;
        }}

        .aira-profile-location {{
            display: inline-flex;
            align-items: center;
            gap: 7px;

            margin-top: 20px;
            padding: 9px 14px;

            color: #075985;
            background: #e0f2fe;
            border-radius: 999px;

            font-size: 0.88rem;
            font-weight: 750;
        }}


        /* -----------------------------------------------
           External link buttons
        ------------------------------------------------ */

        .aira-profile-links {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 11px;
        }}

        .aira-link-button {{
            width: 100%;
            min-height: 48px;
            padding: 0 17px;
            box-sizing: border-box;

            display: grid;
            grid-template-columns: 28px 1fr auto;
            align-items: center;
            gap: 10px;

            color: #172033;
            background: #ffffff;
            border: 1.5px solid #334155;
            border-radius: 14px;

            font-size: 0.98rem;
            font-weight: 700;
            text-decoration: none;

            transition:
                transform 160ms ease,
                box-shadow 160ms ease,
                background 160ms ease;
        }}

        .aira-link-button:hover {{
            color: #172033;
            background: #f8fafc;

            transform: translateY(-2px);

            box-shadow:
                0 10px 24px rgba(15, 23, 42, 0.10);
        }}

        .aira-link-icon {{
            font-size: 1.05rem;
            text-align: center;
        }}

        .aira-link-label {{
            text-align: center;
        }}

        .aira-link-arrow {{
            color: #64748b;
            font-size: 0.82rem;
            font-weight: 700;
        }}

        .aira-link-disabled {{
            color: #7b8797;
            background: #f1f5f9;
            border-color: #cbd5e1;
            cursor: not-allowed;
        }}

        .aira-link-disabled:hover {{
            background: #f1f5f9;
            transform: none;
            box-shadow: none;
        }}


        /* -----------------------------------------------
           Introduction card
        ------------------------------------------------ */

        .aira-introduction-card {{
            width: 100%;
            padding: 36px 40px;
            box-sizing: border-box;

            color: #303746;
            background: #ffffff;
            border: 1.5px solid #334155;
            border-radius: 30px;

            box-shadow:
                0 12px 30px rgba(15, 23, 42, 0.06);
        }}

        .aira-section-heading {{
            margin: 0 0 18px;

            display: flex;
            align-items: center;
            gap: 10px;

            color: #2e3442;
            font-size: 2rem;
            font-weight: 800;
            line-height: 1.2;
            letter-spacing: -0.03em;
        }}

        .aira-introduction-card p {{
            margin: 0 0 17px;

            font-size: 1rem;
            line-height: 1.78;
        }}

        .aira-introduction-card p:last-child {{
            margin-bottom: 0;
        }}


        /* -----------------------------------------------
           Roadmap image card
        ------------------------------------------------ */

        .aira-roadmap-card {{
            width: min(100%, 940px);
            margin: 0 auto;
            padding: 18px;
            box-sizing: border-box;

            color: #303746;
            background: #ffffff;
            border: 1.5px solid #334155;
            border-radius: 30px;

            box-shadow:
                0 12px 30px rgba(15, 23, 42, 0.07);
        }}

        .aira-roadmap-viewport {{
            width: 100%;
            overflow-x: auto;
            overflow-y: hidden;

            border-radius: 20px;

            scrollbar-width: thin;
            -webkit-overflow-scrolling: touch;
        }}

        .aira-roadmap-image {{
            display: block;
            width: 100%;
            height: auto;

            border-radius: 20px;
        }}

        .aira-mobile-hint {{
            display: none;
            margin: 13px 0 0;

            color: #64748b;
            font-size: 0.82rem;
            text-align: center;
        }}

        .aira-file-warning {{
            padding: 22px;

            color: #92400e;
            background: #fff7ed;
            border: 1px solid #fed7aa;
            border-radius: 16px;

            line-height: 1.6;
        }}


        /* -----------------------------------------------
           Tablet layout
        ------------------------------------------------ */

        @media (max-width: 900px) {{

            [data-testid="stMainBlockContainer"] {{
                padding-right: 1.5rem;
                padding-left: 1.5rem;
            }}

            .aira-home {{
                gap: 26px;
            }}

            .aira-introduction-card {{
                padding: 30px;
            }}

        }}


        /* -----------------------------------------------
           Phone layout
        ------------------------------------------------ */

        @media (max-width: 640px) {{

            [data-testid="stMainBlockContainer"] {{
                padding-top: 1rem;
                padding-right: 1rem;
                padding-bottom: 3rem;
                padding-left: 1rem;
            }}

            .aira-home {{
                gap: 22px;
            }}

            .aira-hero {{
                width: 100%;
            }}

            .aira-profile-card {{
                padding: 12px;
                border-radius: 27px;
            }}

            .aira-profile-image {{
                aspect-ratio: 4 / 5;
                object-position: center top;
                border-radius: 21px;
            }}

            .aira-profile-content {{
                padding: 20px 9px 10px;
            }}

            .aira-profile-name {{
                font-size: 1.75rem;
            }}

            .aira-profile-role {{
                font-size: 1rem;
            }}

            .aira-link-button {{
                min-height: 47px;
                border-radius: 13px;
            }}

            .aira-introduction-card {{
                padding: 24px 21px;
                border-radius: 23px;
            }}

            .aira-section-heading {{
                font-size: 1.55rem;
            }}

            .aira-introduction-card p {{
                font-size: 0.96rem;
                line-height: 1.72;
            }}

            .aira-roadmap-card {{
                padding: 12px;
                border-radius: 23px;
            }}

            /*
            The image remains large on mobile so the small text
            inside the competency map stays readable.
            */

            .aira-roadmap-image {{
                width: 820px;
                max-width: none;
            }}

            .aira-mobile-hint {{
                display: block;
            }}

        }}

    </style>


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
                        Hey, I’m Aira 👋
                    </h1>

                    <p class="aira-profile-role">
                        An aspiring data engineer who genuinely enjoys working
                        behind the scenes to make data and AI actually work.
                    </p>

                    <p class="aira-profile-summary">
                        I build data pipelines, explore modern data platforms,
                        and turn raw data into something reliable, structured,
                        and useful.
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