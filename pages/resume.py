# imports
from html import escape
from textwrap import dedent

import streamlit as st


# =========================================================
# Project Paths & Assets
# =========================================================
from content.resume import WORK_HISTORY
from utils.constants import (
    PROFILE_IMAGE,
    RESUME_CANDIDATES,
    STYLES_PATH,
    TECH_STACK_IMAGE,
)

from utils.helpers import image_to_data_uri, load_css

RESUME_FILE = next(
    (file for file in RESUME_CANDIDATES if file.exists()),
    RESUME_CANDIDATES[0],
)


# =========================================================
# Page Styling
# =========================================================
load_css(STYLES_PATH / "resume.css")


# =========================================================
# Header Content
# =========================================================
contact_html = dedent(
    """
    <div class="contact-panel">
        <div class="contact-row">
            <span class="contact-line-icon">✉</span>
            <div>
                <span class="contact-label">Email</span>
                <a class="contact-value"
                   href="mailto:adelosofranco@gmail.com">
                    adelosofranco@gmail.com
                </a>
            </div>
        </div>
        <div class="contact-row">
            <span class="contact-line-icon">☎</span>
            <div>
                <span class="contact-label">Phone</span>
                <a class="contact-value"
                   href="tel:+46705666295">
                    +46 70 566 6295
                </a>
            </div>
        </div>
        <div class="contact-row">
            <span class="contact-line-icon">⌖</span>
            <div>
                <span class="contact-label">Location</span>
                <span class="contact-value">
                    Vällingby, Stockholm, Sweden
                </span>
            </div>
        </div>
    </div>
    """
).strip()


header_html = dedent(
    """

    <h1 class="resume-name">Aira Franco</h1>

    <p class="resume-role">
        Aspiring Data Engineer
    </p>

    <div class="resume-summary">
        <p class="summary-paragraph">
            I am an aspiring data engineer who enjoys working behind
            the scenes to make complex data processes run smoothly.
            What I enjoy most is seeing messy data become something
            useful that people can trust.
        </p>

        <p class="summary-paragraph">
            I have practical experience architecting end-to-end data
            pipelines and platforms that transform raw data into
            reliable, tested, analytics-ready data. I have also worked
            with pipeline design, data modelling, and scalable solutions
            that support business decisions. I adapt quickly to new
            tools, environments, and domain-specific data ecosystems.
        </p>

        <p class="summary-paragraph">
            Before moving into data engineering, I worked in
            hospitality, high-volume retail operations, and
            English-language teaching. Those roles strengthened my
            customer focus, communication, adaptability, and attention
            to detail—from creating welcoming experiences and tailoring
            lessons to individual learners to maintaining accuracy in
            fast-moving operational workflows.
        </p>

        <p class="summary-paragraph">
        I am naturally operations-minded and find satisfaction in creating workflows that produce clear, dependable results. 
        I now bring that same mindset to data engineering—building trustworthy, well-structured data foundations 
        that support better decisions and make analytics and AI systems more reliable.
        </p>

        <span class="work-authorization">
            Permanent work authorization in Sweden —
            no sponsorship required.
        </span>
    </div>

    <div class="link-mosaic">
        <a
            class="link-card youtube-card"
            href="https://www.youtube.com/@Aira_Data_Engineering"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Open Aira's YouTube channel"
        >
            <span class="brand-mark youtube-mark">▶</span>

            <span class="link-copy">
                <span class="link-title">YouTube</span>
                <span class="link-description">
                    Project demos
                </span>
            </span>
        </a>

        <a
            class="link-card linkedin-card"
            href="https://www.linkedin.com/in/aira-franco0965/"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Open Aira's LinkedIn profile"
        >
            <span class="brand-mark linkedin-mark">in</span>

            <span class="link-copy">
                <span class="link-title">LinkedIn</span>
                <span class="link-description">
                    Connect with me
                </span>
            </span>
        </a>

        <a
            class="link-card github-card"
            href="https://github.com/Akina-Aoki"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Open Aira's GitHub profile"
        >
            <span class="brand-mark github-mark">
                &lt;/&gt;
            </span>

            <span class="link-copy">
                <span class="link-title">GitHub</span>
                <span class="link-description">
                    View repositories
                </span>
            </span>
        </a>

        <a
            class="link-card blog-card"
            href="https://hashnode.com/@Aira"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Open Aira's projects blog"
        >
            <span class="brand-mark blog-mark">▤</span>

            <span class="link-copy">
                <span class="link-title">
                    Projects Blog
                </span>

                <span class="link-description">
                    Build notes &amp; stories
                </span>
            </span>
        </a>
    </div>
    """
).strip()

# =========================================================
# Two-Column Header Layout
# =========================================================
profile_column, content_column = st.columns(
    [1, 2.15],
    gap="large",
)

with profile_column:
    if PROFILE_IMAGE.exists():
        st.image(
            str(PROFILE_IMAGE),
            use_container_width=True,
        )
    else:
        st.warning(
            "Profile picture not found. "
            "Place it in `assets/profile_pic.jpg`."
        )

    st.markdown(
        contact_html,
        unsafe_allow_html=True,
    )

    if RESUME_FILE.exists():
        pdf_bytes = RESUME_FILE.read_bytes()

        st.download_button(
            label="⬇  Download Resume",
            data=pdf_bytes,
            file_name="CV_Aira_Franco_en.pdf",
            mime="application/pdf",
        )
    else:
        st.download_button(
            label="⬇  Download Resume",
            data="Currently unavailable",
            file_name="resume_placeholder.txt",
            disabled=True,
            help=(
                "Add CV_Aira_Franco_en.pdf or resume.pdf "
                "to the assets folder."
            ),
        )

with content_column:
    st.html(header_html)


# =========================================================
# Divider Before Main Resume Content
# =========================================================
st.markdown(
    '<div class="resume-section-divider"></div>',
    unsafe_allow_html=True,
)


# =========================================================
# Education & Profile
# =========================================================

education_html = dedent(
    """
    <div class="education-card">
        <div class="education-card-header">
            <span class="education-heading">
                Education &amp; Profile
            </span>
        </div>
        <div class="education-body">
            <div class="education-entry">
                <span class="education-number">01</span>
                <div class="education-information">
                    <span class="education-program">
                        Data Engineering
                    </span>
                    <span class="education-school">
                        Stockholms Tekniska Institut
                    </span>
                    <span class="education-location">
                        Stockholm, Sweden
                    </span>
                </div>
                <div class="education-meta">
                    <span class="education-date">
                        Sep 2025 — May 2027
                    </span>
                    <span class="education-type">
                        YH Programme
                    </span>
                </div>
            </div>
            <div class="education-entry">
                <span class="education-number">02</span>
                <div class="education-information">
                    <span class="education-program">
                        English Literature
                    </span>
                    <span class="education-school">
                        Hokusei Gakuen University
                    </span>
                    <span class="education-location">
                        Sapporo, Japan
                    </span>
                </div>
                <div class="education-meta">
                    <span class="education-date">
                        Apr 2015 — Mar 2017
                    </span>
                    <span class="education-type">
                        Associate's Degree
                    </span>
                </div>
            </div>
        </div>
    </div>
    """
).strip()

st.markdown(
    education_html,
    unsafe_allow_html=True,
)

# =========================================================
# Technical Skills — Tech Stack Pyramid
# =========================================================
if TECH_STACK_IMAGE.exists():
    tech_stack_image_uri = image_to_data_uri(TECH_STACK_IMAGE)

    tech_stack_html = f"""

    <div class="tech-stack-card">
        <img
            class="tech-stack-image"
            src="{tech_stack_image_uri}"
            alt="Aira Franco Data Engineering Tech Stack Pyramid"
        >
    </div>
    """

    st.html(tech_stack_html)

else:
    st.warning(
        "Tech-stack image not found. Add "
        "`de_tech_stack_pyramid.png` to the assets folder."
    )


# =========================================================
# Work History Roadmap
# =========================================================
def build_work_history_card(job, index):
    side = "left" if index % 2 == 0 else "right"

    # Keep the current position expanded when the page loads.
    open_attribute = "open" if index == 0 else ""

    achievements_html = "".join(
        f"<li>{escape(achievement)}</li>"
        for achievement in job["achievements"]
    )

    skills_html = "".join(
        f'<span class="wh-skill">{escape(skill)}</span>'
        for skill in job["skills"]
    )

    return f"""
        <article class="wh-item wh-{side}">
            <details
                class="wh-card wh-tone-{escape(job['tone'])}"
                {open_attribute}
            >
                <summary class="wh-summary">
                    <div class="wh-card-header">
                        <div class="wh-icon" aria-hidden="true">
                            {escape(job['icon'])}
                        </div>

                        <div class="wh-title-group">
                            <span class="wh-period">
                                {escape(job['period'])}
                            </span>

                            <h3 class="wh-role">
                                {escape(job['role'])}
                                <span class="wh-role-divider">|</span>
                                {escape(job['company'])}
                            </h3>

                            <p class="wh-location">
                                <span aria-hidden="true">●</span>
                                {escape(job['location'])}
                            </p>
                        </div>

                        <span
                            class="wh-toggle"
                            aria-hidden="true"
                        ></span>
                    </div>
                </summary>

                <div class="wh-card-content">
                    <div class="wh-divider"></div>

                    <ul class="wh-achievements">
                        {achievements_html}
                    </ul>

                    <div class="wh-divider"></div>

                    <div class="wh-skills">
                        {skills_html}
                    </div>
                </div>
            </details>

            <div class="wh-milestone" aria-hidden="true">
                <span></span>
            </div>
        </article>
    """


work_history_cards = "".join(
    build_work_history_card(job, index)
    for index, job in enumerate(WORK_HISTORY)
)


work_history_html = """

<section
    class="work-history-roadmap"
    aria-labelledby="work-history-heading"
>
    <div class="wh-heading-area">
        <h2 id="work-history-heading" class="wh-heading">
            Work History
        </h2>

        <p class="wh-instruction">
            Select a role to view its responsibilities and skills.
        </p>

        <div class="wh-heading-decoration" aria-hidden="true">
            <span></span>
        </div>
    </div>

    <div class="wh-timeline">
""" + work_history_cards + """
    </div>
</section>
"""

st.html(work_history_html)
