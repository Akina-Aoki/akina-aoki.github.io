from base64 import b64encode
from pathlib import Path

import streamlit as st


# ---------------------------------------------------------
# File paths
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROFILE_IMAGE = PROJECT_ROOT / "assets" / "profile_pic.jpg"


def image_to_base64(image_path: Path) -> str:
    """Convert a local image into a Base64 string for the HTML profile card."""
    return b64encode(image_path.read_bytes()).decode("utf-8")


# ---------------------------------------------------------
# Profile card
# ---------------------------------------------------------

if PROFILE_IMAGE.exists():
    encoded_image = image_to_base64(PROFILE_IMAGE)

    st.html(
        f"""
        <style>
            .aira-profile-wrapper {{
                display: flex;
                justify-content: center;
                width: 100%;
                padding: 1rem 0 3rem 0;
            }}

            .aira-profile-card {{
                width: min(100%, 390px);
                padding: 16px;
                overflow: hidden;
                box-sizing: border-box;

                background: rgba(248, 250, 252, 0.96);
                border: 1px solid rgba(148, 163, 184, 0.25);
                border-radius: 32px;

                box-shadow:
                    0 24px 55px rgba(15, 23, 42, 0.14),
                    0 5px 15px rgba(15, 23, 42, 0.08);
            }}

            .aira-profile-image {{
                display: block;
                width: 100%;
                height: 410px;

                object-fit: cover;
                object-position: center top;

                border-radius: 24px;
            }}

            .aira-profile-content {{
                padding: 22px 10px 10px 10px;
                color: #111827;
            }}

            .aira-profile-name {{
                margin: 0 0 10px 0;

                font-size: 2rem;
                font-weight: 800;
                line-height: 1.15;
                letter-spacing: -0.03em;
            }}

            .aira-profile-role {{
                margin: 0 0 14px 0;

                color: #334155;
                font-size: 1.04rem;
                font-weight: 600;
                line-height: 1.5;
            }}

            .aira-profile-summary {{
                margin: 0;

                color: #475569;
                font-size: 0.96rem;
                line-height: 1.65;
            }}

            .aira-profile-location {{
                display: inline-flex;
                align-items: center;
                gap: 6px;

                margin-top: 18px;
                padding: 8px 13px;

                color: #075985;
                background: #e0f2fe;
                border-radius: 999px;

                font-size: 0.86rem;
                font-weight: 700;
            }}

            @media (max-width: 640px) {{
                .aira-profile-wrapper {{
                    padding-top: 0.5rem;
                    padding-bottom: 2rem;
                }}

                .aira-profile-card {{
                    width: 100%;
                    padding: 12px;
                    border-radius: 26px;
                }}

                .aira-profile-image {{
                    height: auto;
                    aspect-ratio: 4 / 5;
                    border-radius: 20px;
                }}

                .aira-profile-content {{
                    padding: 18px 8px 8px 8px;
                }}

                .aira-profile-name {{
                    font-size: 1.7rem;
                }}
            }}
        </style>

        <div class="aira-profile-wrapper">
            <article class="aira-profile-card">

                <img
                    class="aira-profile-image"
                    src="data:image/jpeg;base64,{encoded_image}"
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
        </div>
        """
    )

else:
    st.error(
        "Profile picture not found. Make sure the file is saved as "
        "`assets/profile_pic.jpg`."
    )


# ---------------------------------------------------------
# Personal introduction
# ---------------------------------------------------------

st.markdown("## The person behind the pipelines ⚙️")

st.write(
    """
    The data engineering ecosystem evolves incredibly fast, with new tools,
    platforms, and frameworks appearing all the time. 🚀

    But I believe strong data engineers should understand the foundations first:
    the operational and technical architectures, and the *whys* and *hows*
    behind how data is collected, stored, modelled, transformed, tested, and
    delivered at different scales.

    I enjoy being the person behind the scenes—the quiet superhero making sure
    applications, analytics, and machine learning models receive reliable,
    well-structured, and usable data. 🦸‍♀️

    AI may get the spotlight, but good data engineering is what keeps everything
    running in the background.
    """
)


# ---------------------------------------------------------
# Technical background
# ---------------------------------------------------------

st.markdown("## 🛠️ What I work with")

st.write(
    """
    Data engineering tools change so quickly that there is always something new
    to learn. I enjoy learning new technologies, but I also think it is important
    to understand the basics first: how data moves, where it is stored, how it is
    transformed, and why we choose one solution over another. 🧠

    I mainly use **Python** 🐍 to build applications and data pipelines, and
    **SQL** to explore, clean, transform, and model data.

    I have worked with both transactional and analytical databases, including
    **PostgreSQL, Supabase, TimescaleDB, Snowflake, and Databricks**. 🗄️

    Most of my experience so far has been with **batch data**, where I have built
    ETL and ELT workflows, data warehouse layers, dimensional models, and data
    quality tests.

    I am now also learning more about **real-time data**, using tools such as
    **Kafka** to understand how data can be processed as it arrives. ⚡

    In my projects, I have worked with **Docker, Airflow, dbt, Amazon S3,
    Snowflake, Databricks, Terraform, Git, GitHub Actions, and Power BI**.

    I also enjoy documenting my work and explaining the full process—not only
    showing the final result. 📝

    I do not want to use tools just because they are popular. I want to understand
    what problem they solve, how the tools work together, and when a simpler
    solution might actually be better. 🔍

    And of course, I am always learning. That is exactly why data engineering is
    so much fun! ✨
    """
)