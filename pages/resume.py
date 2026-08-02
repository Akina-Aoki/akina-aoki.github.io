from pathlib import Path
from textwrap import dedent
import base64

import streamlit as st


# =========================================================
# Project Paths & Assets
# =========================================================
from utils.constants import (
    PROFILE_IMAGE,
    RESUME_CANDIDATES,
    TECH_STACK_IMAGE,
)

RESUME_FILE = next(
    (file for file in RESUME_CANDIDATES if file.exists()),
    RESUME_CANDIDATES[0],
)


# =========================================================
# Page Styling
# =========================================================
resume_css = dedent(
    """
    <style>
    :root {
        --resume-bg: #061321;
        --resume-panel: #0b1d2d;
        --resume-panel-hover: #10283d;
        --resume-white: #f8fafc;
        --resume-muted: #aebdca;
        --resume-green: #64e6b3;
        --resume-border: rgba(100, 230, 179, 0.24);
        --youtube-coral: #f2573f;
        --linkedin-blue: #428eea;
        --blog-gold: #f6bd42;
    }

    /* Main page */
    .stApp {
        background: var(--resume-bg);
        color: var(--resume-white);
    }

    .block-container {
        max-width: 1420px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #081827;
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }

    [data-testid="stSidebar"] * {
        color: var(--resume-white);
    }

    /* Profile image */
    div[data-testid="stImage"] {
        width: 100%;
    }

    div[data-testid="stImage"] img {
        width: 100%;
        aspect-ratio: 4 / 4.7;
        object-fit: cover;
        object-position: center top;
        border: 1px solid var(--resume-border);
        border-radius: 24px;
        box-shadow: 0 24px 55px rgba(0, 0, 0, 0.34);
    }

    /* Name and introduction */
    .resume-name {
        margin: 0 !important;
        color: var(--resume-white) !important;
        font-family: Georgia, "Times New Roman", serif !important;
        font-size: clamp(4.2rem, 6.5vw, 6.2rem) !important;
        font-weight: 700 !important;
        line-height: 0.95 !important;
        letter-spacing: -0.045em !important;
    }

    .resume-role {
        margin: 0.9rem 0 1.7rem;
        color: var(--resume-green) !important;
        font-size: clamp(1.2rem, 1.8vw, 1.55rem);
        font-weight: 700;
    }

    .resume-summary {
        max-width: 880px;
        color: var(--resume-white);
        font-size: 1.05rem;
        line-height: 1.75;
    }

    .work-authorization {
        display: block;
        margin-top: 1.1rem;
        color: var(--resume-muted);
        font-size: 0.98rem;
        font-style: italic;
    }

    /* Contact panel below profile */
    .contact-panel {
        width: 100%;
        margin-top: 0.85rem;
        padding: 0 0.9rem;
        box-sizing: border-box;
        background: rgba(11, 29, 45, 0.88);
        border: 1px solid var(--resume-border);
        border-radius: 16px;
    }

    .contact-row {
        display: grid;
        grid-template-columns: 35px 1fr;
        align-items: center;
        gap: 0.75rem;
        min-height: 67px;
        padding: 0.55rem 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    }

    .contact-row:last-child {
        border-bottom: none;
    }

    .contact-line-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 32px;
        height: 32px;
        color: var(--resume-green);
        font-size: 1.2rem;
    }

    .contact-label {
        display: block;
        margin-bottom: 0.15rem;
        color: var(--resume-muted);
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.09em;
        text-transform: uppercase;
    }

    .contact-value,
    .contact-value:visited {
        display: block;
        color: var(--resume-white) !important;
        font-size: 0.92rem;
        line-height: 1.3;
        text-decoration: none;
        overflow-wrap: anywhere;
    }

    a.contact-value:hover {
        color: var(--resume-green) !important;
    }

    /* Download button below contact panel */
    div[data-testid="stDownloadButton"] {
        width: 100%;
        margin-top: 0.75rem;
    }

    div[data-testid="stDownloadButton"] button {
        width: 100%;
        min-height: 54px;
        color: #061321;
        background:
            linear-gradient(
                135deg,
                #64e6b3 0%,
                #7cecc1 100%
            );
        border: 1px solid var(--resume-green);
        border-radius: 13px;
        font-size: 0.98rem;
        font-weight: 800;
        box-shadow: 0 10px 24px rgba(100, 230, 179, 0.13);
        transition:
            transform 160ms ease,
            background 160ms ease,
            color 160ms ease;
    }

    div[data-testid="stDownloadButton"] button:hover {
        color: var(--resume-white);
        background: transparent;
        border-color: var(--resume-green);
        transform: translateY(-2px);
    }

    /* External link mosaic */
    .link-mosaic {
        display: grid;
        grid-template-columns: 1.55fr 1fr;
        gap: 0.85rem;
        margin-top: 2.3rem;
    }

    .link-card,
    .link-card:visited {
        position: relative;
        display: flex;
        align-items: center;
        gap: 1rem;
        min-height: 132px;
        padding: 1.25rem 1.4rem;
        box-sizing: border-box;
        overflow: hidden;
        border-radius: 17px;
        color: #ffffff !important;
        text-decoration: none !important;
        transition:
            transform 180ms ease,
            box-shadow 180ms ease,
            filter 180ms ease;
    }

    .link-card:hover {
        color: #ffffff !important;
        filter: brightness(1.05);
        box-shadow: 0 18px 38px rgba(0, 0, 0, 0.28);
        transform: translateY(-4px);
    }

    .link-card > * {
        position: relative;
        z-index: 2;
    }

    .brand-mark {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex: 0 0 58px;
        width: 58px;
        height: 58px;
        border-radius: 14px;
        font-size: 1.4rem;
        font-weight: 900;
    }

    .link-copy {
        display: block;
        min-width: 0;
    }

    .link-title {
        display: block;
        color: inherit;
        font-size: clamp(1.2rem, 2vw, 1.65rem);
        font-weight: 800;
        line-height: 1.15;
    }

    .link-description {
        display: block;
        margin-top: 0.35rem;
        color: inherit;
        font-size: 0.9rem;
        line-height: 1.3;
        opacity: 0.82;
    }

    /* YouTube card */
    .youtube-card {
        background:
            linear-gradient(
                135deg,
                #f2573f 0%,
                #ef5c45 55%,
                #f06b53 100%
            );
    }

    .youtube-mark {
        color: var(--youtube-coral);
        background: #ffffff;
        font-size: 1.45rem;
    }

    .youtube-card::before {
        content: "";
        position: absolute;
        top: 14px;
        left: 14px;
        width: 58px;
        height: 58px;
        opacity: 0.3;
        background-image:
            radial-gradient(
                circle,
                rgba(255, 255, 255, 0.9) 3px,
                transparent 4px
            );
        background-size: 17px 17px;
    }

    .youtube-card::after {
        content: "";
        position: absolute;
        right: -60px;
        bottom: -85px;
        width: 230px;
        height: 230px;
        border: 1px solid rgba(255, 255, 255, 0.32);
        border-radius: 50%;
        box-shadow:
            0 0 0 14px rgba(255, 255, 255, 0.08),
            0 0 0 28px rgba(255, 255, 255, 0.06);
    }

    /* LinkedIn card */
    .linkedin-card {
        background:
            linear-gradient(
                135deg,
                #438eea 0%,
                #54a1f1 100%
            );
    }

    .linkedin-mark {
        color: var(--linkedin-blue);
        background: #ffffff;
        font-family: Arial, sans-serif;
        font-size: 1.65rem;
    }

    .linkedin-card::after {
        content: "";
        position: absolute;
        right: 13px;
        top: 29px;
        width: 54px;
        height: 54px;
        opacity: 0.25;
        background-image:
            radial-gradient(
                circle,
                rgba(255, 255, 255, 0.95) 3px,
                transparent 4px
            );
        background-size: 15px 15px;
    }

    /* GitHub card */
    .github-card {
        background:
            linear-gradient(
                135deg,
                #1b2937 0%,
                #243649 100%
            );
        border: 1px solid rgba(255, 255, 255, 0.15);
    }

    .github-mark {
        color: #182635;
        background: #ffffff;
        font-family: Consolas, monospace;
        font-size: 1rem;
    }

    .github-card::before {
        content: "</>";
        position: absolute;
        left: 18px;
        top: 3px;
        color: rgba(174, 189, 202, 0.25);
        font-family: Consolas, monospace;
        font-size: 4.2rem;
        font-weight: 800;
        letter-spacing: -0.35em;
        transform: rotate(-5deg);
    }

    .github-card::after {
        content: "";
        position: absolute;
        right: 20px;
        top: 34px;
        width: 58px;
        height: 58px;
        opacity: 0.22;
        background-image:
            radial-gradient(
                circle,
                rgba(255, 255, 255, 0.8) 3px,
                transparent 4px
            );
        background-size: 16px 16px;
    }

    /* Projects Blog card */
    .blog-card,
    .blog-card:visited {
        color: #101820 !important;
        background:
            linear-gradient(
                135deg,
                #f7c64e 0%,
                #f5b83d 100%
            );
    }

    .blog-card:hover {
        color: #101820 !important;
    }

    .blog-mark {
        color: #101820;
        background: rgba(255, 255, 255, 0.92);
        font-size: 1.35rem;
    }

    .blog-card::before {
        content: "";
        position: absolute;
        inset: 0 auto 0 0;
        width: 72px;
        opacity: 0.24;
        background-image:
            linear-gradient(
                rgba(65, 48, 8, 0.38) 1px,
                transparent 1px
            ),
            linear-gradient(
                90deg,
                rgba(65, 48, 8, 0.38) 1px,
                transparent 1px
            );
        background-size: 14px 14px;
    }

    /* Section divider */
    .resume-section-divider {
        position: relative;
        width: 100%;
        height: 1px;
        margin: 3rem 0 2.5rem;
        background:
            linear-gradient(
                90deg,
                rgba(100, 230, 179, 0.95) 0%,
                rgba(100, 230, 179, 0.45) 60%,
                transparent 100%
            );
    }

    /* General résumé content */
    h1,
    h2,
    h3,
    p,
    li,
    [data-testid="stMarkdownContainer"] {
        color: var(--resume-white);
    }

    h2,
    h3 {
        font-family: Georgia, "Times New Roman", serif;
    }

    hr {
        border-color: rgba(255, 255, 255, 0.12);
    }

    /* Responsive layout */
    @media (max-width: 950px) {
        .resume-name {
            font-size: 4rem !important;
        }

        .link-card {
            min-height: 115px;
            padding: 1rem;
        }

        .brand-mark {
            flex-basis: 50px;
            width: 50px;
            height: 50px;
        }
    }

    @media (max-width: 768px) {
        .block-container {
            padding-top: 2rem;
        }

        .resume-name {
            margin-top: 1.5rem !important;
            font-size: 3.4rem !important;
        }

        .link-mosaic {
            grid-template-columns: 1fr 1fr;
            margin-top: 1.8rem;
        }

        .link-card:hover {
            transform: none;
        }

        .resume-section-divider {
            margin: 2.4rem 0 2rem;
        }
    }

    @media (max-width: 560px) {
        .link-mosaic {
            grid-template-columns: 1fr;
        }

        .link-card {
            min-height: 105px;
        }

        .resume-name {
            font-size: 3rem !important;
        }
    }
    </style>
    """
).strip()

st.markdown(
    resume_css,
    unsafe_allow_html=True,
)


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
    <style>
    .resume-summary .summary-paragraph {
        margin: 0 0 1rem;
        color: #f8fafc;
        font-size: inherit;
        line-height: inherit;
    }

    .resume-summary .summary-paragraph:last-of-type {
        margin-bottom: 0;
    }
    </style>

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
education_css = dedent(
    """
    <style>
    .education-card {
        position: relative;
        width: 100%;
        margin: 0 0 3rem;
        overflow: hidden;
        color: #101820;
        background:
            linear-gradient(
                135deg,
                #f7c44f 0%,
                #ffc95a 55%,
                #f4b93d 100%
            );
        border: 1px solid rgba(255, 224, 146, 0.65);
        border-radius: 20px;
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.2);
    }

    .education-card::after {
        content: "";
        position: absolute;
        top: -35px;
        right: -35px;
        width: 120px;
        height: 120px;
        border: 2px solid rgba(16, 24, 32, 0.14);
        border-radius: 50%;
        box-shadow:
            0 0 0 13px rgba(16, 24, 32, 0.05),
            0 0 0 26px rgba(16, 24, 32, 0.035);
    }

    .education-card-header {
        position: relative;
        z-index: 2;
        display: flex;
        align-items: center;
        padding: 1.4rem 1.6rem;
        border-bottom: 2px dashed rgba(16, 24, 32, 0.48);
    }

    .education-heading {
        color: #101820 !important;
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(1.9rem, 3vw, 2.5rem);
        font-weight: 700;
        line-height: 1.1;
    }

    .education-body {
        position: relative;
        z-index: 2;
        padding: 0 1.6rem;
    }

    .education-entry {
        display: grid;
        grid-template-columns: 58px minmax(0, 1fr) auto;
        align-items: center;
        gap: 1.15rem;
        min-height: 138px;
        padding: 1.15rem 0;
        border-bottom: 1px solid rgba(16, 24, 32, 0.28);
    }

    .education-entry:last-child {
        border-bottom: none;
    }

    .education-number {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 52px;
        height: 52px;
        color: #f8fafc !important;
        background: #0b1d2d;
        border-radius: 14px;
        font-size: 0.9rem;
        font-weight: 800;
        letter-spacing: 0.04em;
        box-shadow: 0 8px 18px rgba(6, 19, 33, 0.18);
    }

    .education-information {
        min-width: 0;
    }

    .education-program {
        display: block;
        margin-bottom: 0.4rem;
        color: #101820 !important;
        font-size: 1.4rem;
        font-weight: 800;
        line-height: 1.25;
    }

    .education-school {
        display: block;
        color: #101820 !important;
        font-size: 1.08rem;
        font-weight: 700;
        line-height: 1.4;
    }

    .education-location {
        display: block;
        margin-top: 0.2rem;
        color: rgba(16, 24, 32, 0.74) !important;
        font-size: 0.95rem;
        line-height: 1.35;
    }

    .education-meta {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        gap: 0.55rem;
        min-width: 190px;
    }

    .education-date {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.55rem 0.8rem;
        color: #f8fafc !important;
        background: #0b1d2d;
        border-radius: 999px;
        font-size: 0.86rem;
        font-weight: 750;
        white-space: nowrap;
    }

    .education-type {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.42rem 0.7rem;
        color: #101820 !important;
        background: rgba(255, 255, 255, 0.5);
        border: 1px solid rgba(16, 24, 32, 0.18);
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 800;
        white-space: nowrap;
    }

    @media (max-width: 700px) {
        .education-card-header {
            padding: 1.25rem;
        }

        .education-body {
            padding: 0 1.25rem;
        }

        .education-entry {
            grid-template-columns: 52px minmax(0, 1fr);
            gap: 0.9rem;
            min-height: auto;
            padding: 1.3rem 0;
        }

        .education-number {
            width: 46px;
            height: 46px;
        }

        .education-meta {
            grid-column: 2;
            align-items: flex-start;
            min-width: 0;
        }
    }

    @media (max-width: 460px) {
        .education-card-header,
        .education-body {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .education-heading {
            font-size: 1.75rem;
        }

        .education-entry {
            grid-template-columns: 1fr;
        }

        .education-number,
        .education-meta {
            grid-column: 1;
        }

        .education-meta {
            flex-direction: row;
            flex-wrap: wrap;
        }

        .education-program {
            font-size: 1.25rem;
        }

        .education-school {
            font-size: 1rem;
        }
    }
    </style>
    """
).strip()

st.markdown(
    education_css,
    unsafe_allow_html=True,
)


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
    tech_stack_base64 = base64.b64encode(
        TECH_STACK_IMAGE.read_bytes()
    ).decode("utf-8")

    tech_stack_html = f"""
    <style>
    .tech-stack-card {{
        width: 100%;
        max-width: 1050px;
        margin: 1rem auto 3.25rem;
        padding: 1rem;
        box-sizing: border-box;
        background:
            linear-gradient(
                145deg,
                #0b1d2d 0%,
                #071521 100%
            );
        border: 1px solid rgba(100, 230, 179, 0.32);
        border-radius: 22px;
        box-shadow:
            0 22px 50px rgba(0, 0, 0, 0.28),
            0 0 30px rgba(100, 230, 179, 0.04);
    }}

    .tech-stack-image {{
        display: block;
        width: 100%;
        max-width: 100%;
        height: auto;
        margin: 0;
        padding: 0;
        object-fit: contain;
        object-position: center;
        border-radius: 14px;
    }}

    @media (max-width: 768px) {{
        .tech-stack-card {{
            margin-top: 0.5rem;
            margin-bottom: 2.5rem;
            padding: 0.5rem;
            border-radius: 16px;
        }}

        .tech-stack-image {{
            border-radius: 11px;
        }}
    }}
    </style>

    <div class="tech-stack-card">
        <img
            class="tech-stack-image"
            src="data:image/png;base64,{tech_stack_base64}"
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
from html import escape


work_history = [
    {
        "period": "2020 – Present",
        "role": "Operations Assistant",
        "company": "Inditex (Zara)",
        "location": "Stockholm, Sweden",
        "icon": "👕",
        "tone": "gray",
        "achievements": [
            (
                "Optimized inventory and logistics workflows across "
                "departments, improving product distribution efficiency "
                "under strict operational timelines."
            ),
            (
                "Developed a strong understanding of stock movement, "
                "demand patterns and operational bottlenecks, directly "
                "informing my transition into data engineering."
            ),
        ],
        "skills": [
            "Inventory Management",
            "Retail Operations",
            "Logistics",
            "Time Management",
        ],
    },
    {
        "period": "2019",
        "role": "Hotel Receptionist",
        "company": "The Stay Sapporo Nagomi",
        "location": "Sapporo, Japan",
        "icon": "🛎️",
        "tone": "pink",
        "achievements": [
            (
                "Handled front-office operations, guest relations and "
                "daily payment reconciliation to support efficient service."
            ),
            (
                "Managed hotel inventories for company supplies. "
                "Inspected housekeeping's work after cleaning to maintain "
                "hotel cleanliness standards."
            ),
        ],
        "skills": [
            "Administration",
            "Hospitality Service",
            "Booking Systems",
        ],
    },
    {
        "period": "2018 – 2019",
        "role": "Production Assistant",
        "company": "Krispy Kreme Doughnuts Japan",
        "location": "Chitose, Japan",
        "icon": "🍩",
        "tone": "blue",
        "achievements": [
            (
                "Assisted with launching food-production workflows for "
                "the company's first store in the region."
            ),
            (
                "Supported preparation and worked as part of the "
                "production crew for the food products."
            ),
        ],
        "skills": [
            "Food Production",
            "Operational Coordination",
        ],
    },
    {
        "period": "2016 – 2018",
        "role": "Bartender",
        "company": "TK6 International Sports Bar",
        "location": "Sapporo, Japan",
        "icon": "🍸",
        "tone": "olive",
        "achievements": [
            (
                "Managed daily bar operations, staff coordination, "
                "daily cash reconciliation and cost controls while "
                "studying at university."
            ),
        ],
        "skills": [
            "Restaurant Operations",
            "Team Coordination",
            "Interpersonal Communication",
        ],
    },
    {
        "period": "2016",
        "role": "Front Desk Assistant",
        "company": "Hilton",
        "location": "Niseko, Japan",
        "icon": "🛎️",
        "tone": "gray",
        "achievements": [
            (
                "Completed coursework and an internship involving "
                "reception duties and administrative coordination."
            ),
            (
                "Helped maintain efficient internal processes and "
                "smooth day-to-day operations."
            ),
        ],
        "skills": [
            "Hotel Operations",
            "Administration",
        ],
    },
    {
        "period": "2015 – 2019",
        "role": "English Language Teacher",
        "company": "Self-employed",
        "location": "Sapporo, Japan",
        "icon": "🎓",
        "tone": "cream",
        "achievements": [
            (
                "Founded and operated an English tutoring business "
                "alongside university studies."
            ),
            (
                "Delivered one-on-one and group lessons for children "
                "and adults, focusing on conversation, grammar and "
                "university exam readiness."
            ),
        ],
        "skills": [
            "Language Teaching",
            "Lesson Planning",
            "Language Level Assessment",
        ],
    },
    {
        "period": "2015 – 2019",
        "role": "Translator — Japanese ↔ English",
        "company": "Self-employed",
        "location": "Sapporo, Japan",
        "icon": "文",
        "tone": "pink",
        "achievements": [
            (
                "Translated business and general documents between "
                "Japanese and English with precision and cultural "
                "sensitivity."
            ),
            (
                "Managed timelines, priorities and delivery while "
                "working directly with clients to clarify requirements."
            ),
        ],
        "skills": [
            "Translation",
            "Client Communication",
        ],
    },
]


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
    for index, job in enumerate(work_history)
)


work_history_html = """
<style>
    /* =====================================================
       Work History colour palette
       ===================================================== */
    .work-history-roadmap {
        --wh-background: #28254F;
        --wh-card-gray: #506695;
        --wh-card-blue: #5271C0;
        --wh-card-navy: #283B60;
        --wh-card-sky: #95B2F8;
        --wh-card-lavender: #B5C0F3;

        --wh-text-light: #F7F8FF;
        --wh-text-dark: #28254F;
        --wh-line: #95B2F8;
        --wh-accent: #B5C0F3;

        box-sizing: border-box;
        width: 100%;
        margin: 2rem auto;
        padding: 3rem 2.25rem 3.5rem;
        overflow: hidden;

        color: var(--wh-text-light);
        background: var(--wh-background);
        border: 1px solid rgba(149, 178, 248, 0.3);
        border-radius: 30px;

        font-family:
            Inter,
            ui-sans-serif,
            system-ui,
            -apple-system,
            BlinkMacSystemFont,
            "Segoe UI",
            sans-serif;
    }

    .work-history-roadmap *,
    .work-history-roadmap *::before,
    .work-history-roadmap *::after {
        box-sizing: border-box;
    }

    /* =====================================================
       Heading
       ===================================================== */
    .wh-heading-area {
        margin-bottom: 3rem;
        text-align: center;
    }

    .wh-heading {
        margin: 0;
        color: var(--wh-text-light) !important;
        font-size: clamp(2rem, 5vw, 3.5rem);
        font-weight: 800;
        line-height: 1.05;
        letter-spacing: -0.045em;
    }

    .wh-instruction {
        margin: 0.85rem 0 0;
        color: var(--wh-card-lavender) !important;
        font-size: 0.95rem;
        font-weight: 650;
    }

    .wh-heading-decoration {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.45rem;
        margin-top: 1rem;
    }

    .wh-heading-decoration::before,
    .wh-heading-decoration::after {
        width: 46px;
        height: 4px;
        content: "";
        background: var(--wh-card-blue);
        border-radius: 999px;
    }

    .wh-heading-decoration span {
        width: 9px;
        height: 9px;
        background: var(--wh-card-sky);
        border-radius: 50%;
    }

    /* =====================================================
       Timeline
       ===================================================== */
    .wh-timeline {
        position: relative;
        width: 100%;
        max-width: 1100px;
        margin: 0 auto;
    }

    .wh-timeline::before {
        position: absolute;
        z-index: 0;
        top: 54px;
        bottom: 54px;
        left: 50%;

        width: 3px;
        content: "";
        transform: translateX(-50%);

        background: var(--wh-line);
        border-radius: 999px;
    }

    .wh-item {
        position: relative;
        z-index: 1;

        display: grid;
        grid-template-columns:
            minmax(0, 1fr)
            76px
            minmax(0, 1fr);
        align-items: start;

        width: 100%;
        margin-bottom: 2.25rem;
    }

    .wh-item:last-child {
        margin-bottom: 0;
    }

    .wh-left .wh-card {
        grid-column: 1;
    }

    .wh-right .wh-card {
        grid-column: 3;
    }

    /* =====================================================
       Milestones and connectors
       ===================================================== */
    .wh-milestone {
        position: relative;
        z-index: 4;

        display: grid;
        grid-row: 1;
        grid-column: 2;
        place-items: center;
        align-self: start;
        justify-self: center;

        width: 34px;
        height: 34px;
        margin-top: 46px;

        background: var(--wh-background);
        border: 4px solid var(--wh-background);
        border-radius: 50%;
        box-shadow: 0 0 0 2px var(--wh-line);
    }

    .wh-milestone span {
        width: 13px;
        height: 13px;
        background: var(--wh-card-blue);
        border-radius: 50%;
    }

    .wh-item:nth-child(even) .wh-milestone span {
        background: var(--wh-card-lavender);
    }

    .wh-left .wh-card::after,
    .wh-right .wh-card::after {
        position: absolute;
        top: 62px;

        width: 39px;
        content: "";

        border-top: 2px dashed var(--wh-line);
    }

    .wh-left .wh-card::after {
        right: -39px;
    }

    .wh-right .wh-card::after {
        left: -39px;
    }

    /* =====================================================
       Experience cards
       ===================================================== */
    .wh-card {
        position: relative;
        min-width: 0;
        padding: 1.45rem;

        border: 2px solid var(--wh-line);
        border-radius: 24px;
        box-shadow:
            0 9px 0 rgba(149, 178, 248, 0.13),
            0 20px 35px rgba(0, 0, 0, 0.22);

        transition:
            transform 180ms ease,
            box-shadow 180ms ease;
    }

    .wh-card[open] {
        box-shadow:
            0 10px 0 rgba(149, 178, 248, 0.17),
            0 24px 42px rgba(0, 0, 0, 0.32);
    }

    .wh-tone-gray {
        color: var(--wh-text-light);
        background: var(--wh-card-gray);
    }

    .wh-tone-pink {
        color: var(--wh-text-dark);
        background: var(--wh-card-lavender);
    }

    .wh-tone-blue {
        color: var(--wh-text-light);
        background: var(--wh-card-blue);
    }

    .wh-tone-olive {
        color: var(--wh-text-light);
        background: var(--wh-card-navy);
    }

    .wh-tone-cream {
        color: var(--wh-text-dark);
        background: var(--wh-card-sky);
    }

    /* =====================================================
       Interactive summary
       ===================================================== */
    .wh-summary {
        display: block;
        position: relative;

        margin: 0;
        padding: 0;

        list-style: none;
        cursor: pointer;
        border-radius: inherit;
    }

    .wh-summary::-webkit-details-marker {
        display: none;
    }

    .wh-summary::marker {
        content: "";
    }

    .wh-summary:focus-visible {
        outline: 3px solid var(--wh-card-lavender);
        outline-offset: 7px;
    }

    /* =====================================================
       Card header
       ===================================================== */
    .wh-card-header {
        position: relative;

        display: grid;
        grid-template-columns: 74px minmax(0, 1fr);
        gap: 1rem;
        align-items: start;

        padding-right: 0;
        padding-bottom: 3.65rem;
    }

    .wh-icon {
        display: grid;
        place-items: center;

        width: 74px;
        height: 74px;

        color: var(--wh-text-dark);
        background: var(--wh-card-lavender);
        border: 2px dashed var(--wh-card-navy);
        border-radius: 50%;

        font-size: 1.8rem;
        font-weight: 800;
        line-height: 1;
    }

    .wh-title-group {
        min-width: 0;
    }

    .wh-period {
        display: inline-flex;
        align-items: center;
        min-height: 30px;
        margin-bottom: 0.65rem;
        padding: 0.3rem 0.85rem;

        color: var(--wh-text-light);
        background: var(--wh-card-navy);
        border-radius: 999px;

        font-size: 0.84rem;
        font-weight: 800;
        line-height: 1;
        white-space: nowrap;
    }

    .wh-tone-gray .wh-period,
    .wh-tone-blue .wh-period,
    .wh-tone-olive .wh-period {
        color: var(--wh-text-dark);
        background: var(--wh-card-sky);
    }

    .wh-role {
        margin: 0;

        color: inherit !important;
        font-size: clamp(1.05rem, 1.7vw, 1.28rem);
        font-weight: 800;
        line-height: 1.27;
        letter-spacing: -0.018em;
        overflow-wrap: anywhere;
    }

    .wh-role-divider {
        opacity: 0.58;
    }

    .wh-location {
        display: flex;
        align-items: center;
        gap: 0.45rem;

        margin: 0.65rem 0 0;

        color: inherit !important;
        font-size: 0.92rem;
        font-weight: 600;
        line-height: 1.4;
        opacity: 0.92;
    }

    .wh-location span {
        color: var(--wh-card-lavender);
        font-size: 0.67rem;
    }

    .wh-tone-pink .wh-location span,
    .wh-tone-cream .wh-location span {
        color: var(--wh-card-blue);
    }

    /* =====================================================
       View details / Hide details control
       ===================================================== */
    .wh-toggle {
        position: absolute;
        right: 0;
        bottom: 0;
        left: 0;

        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.7rem;

        width: 100%;
        min-height: 44px;
        padding: 0.6rem 1rem;

        color: var(--wh-text-light);
        background: var(--wh-card-navy);
        border: 1.5px solid var(--wh-line);
        border-radius: 12px;

        font-size: 0.86rem;
        font-weight: 800;
        line-height: 1;
        letter-spacing: 0.01em;

        transition:
            color 180ms ease,
            background-color 180ms ease,
            transform 180ms ease;
    }

    .wh-toggle::before {
        content: "View details";
    }

    .wh-toggle::after {
        display: inline-block;
        margin-top: -0.2rem;

        content: "⌄";

        font-size: 1.8rem;
        font-weight: 900;
        line-height: 0.55;

        transition: transform 180ms ease;
    }

    .wh-card[open] .wh-toggle::before {
        content: "Hide details";
    }

    .wh-card[open] .wh-toggle::after {
        transform: rotate(180deg);
    }

    .wh-tone-gray .wh-toggle,
    .wh-tone-blue .wh-toggle,
    .wh-tone-olive .wh-toggle {
        color: var(--wh-text-dark);
        background: var(--wh-card-sky);
    }

    /* =====================================================
       Expanded content
       ===================================================== */
    .wh-card-content {
        animation: wh-open-card 220ms ease-out;
    }

    @keyframes wh-open-card {
        from {
            opacity: 0;
            transform: translateY(-7px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .wh-divider {
        width: 100%;
        margin: 1.15rem 0;
        border-top: 2px dashed currentColor;
        opacity: 0.52;
    }

    .wh-achievements {
        display: grid;
        gap: 0.72rem;

        margin: 0;
        padding: 0;

        list-style: none;
    }

    .wh-achievements li {
        position: relative;
        margin: 0;
        padding-left: 1rem;

        color: inherit !important;
        font-size: 0.95rem;
        font-weight: 520;
        line-height: 1.55;
    }

    .wh-achievements li::before {
        position: absolute;
        top: 0;
        left: 0;

        content: "›";
        font-weight: 900;
    }

    .wh-skills {
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
    }

    .wh-skill {
        display: inline-flex;
        align-items: center;
        min-height: 34px;
        padding: 0.42rem 0.8rem;

        color: var(--wh-text-dark);
        background: var(--wh-card-lavender);
        border: 1.5px solid var(--wh-card-navy);
        border-radius: 999px;

        font-size: 0.78rem;
        font-weight: 750;
        line-height: 1.2;
    }

    /* =====================================================
       Hover and reduced motion
       ===================================================== */
    @media (hover: hover) {
        .wh-summary:hover .wh-toggle {
            color: var(--wh-text-dark);
            background: var(--wh-card-sky);
            transform: translateY(-2px);
        }
    }

    @media (prefers-reduced-motion: reduce) {
        .wh-card,
        .wh-toggle,
        .wh-toggle::after,
        .wh-card-content {
            animation: none;
            transition: none;
        }
    }

    /* =====================================================
       Tablet
       ===================================================== */
    @media (max-width: 900px) {
        .work-history-roadmap {
            padding-right: 1.4rem;
            padding-left: 1.4rem;
        }

        .wh-item {
            grid-template-columns:
                minmax(0, 1fr)
                62px
                minmax(0, 1fr);
        }

        .wh-card {
            padding: 1.15rem;
            border-radius: 20px;
        }

        .wh-card-header {
            grid-template-columns: 58px minmax(0, 1fr);
            gap: 0.8rem;
        }

        .wh-icon {
            width: 58px;
            height: 58px;
            font-size: 1.4rem;
        }

        .wh-left .wh-card::after,
        .wh-right .wh-card::after {
            width: 31px;
        }

        .wh-left .wh-card::after {
            right: -31px;
        }

        .wh-right .wh-card::after {
            left: -31px;
        }
    }

    /* =====================================================
       Mobile
       ===================================================== */
    @media (max-width: 700px) {
        .work-history-roadmap {
            margin: 1rem auto;
            padding: 2.2rem 1rem 2.5rem;
            border-radius: 22px;
        }

        .wh-heading-area {
            margin-bottom: 2.25rem;
        }

        .wh-heading {
            font-size: 2.25rem;
        }

        .wh-instruction {
            font-size: 0.86rem;
        }

        .wh-timeline::before {
            top: 50px;
            bottom: 50px;
            left: 17px;
        }

        .wh-item {
            grid-template-columns: 34px minmax(0, 1fr);
            column-gap: 0.85rem;
            margin-bottom: 1.5rem;
        }

        .wh-left .wh-card,
        .wh-right .wh-card {
            grid-column: 2;
        }

        .wh-milestone {
            grid-row: 1;
            grid-column: 1;

            width: 28px;
            height: 28px;
            margin-top: 43px;
        }

        .wh-milestone span {
            width: 10px;
            height: 10px;
        }

        .wh-left .wh-card::after,
        .wh-right .wh-card::after {
            top: 56px;
            right: auto;
            left: -18px;
            width: 18px;
        }

        .wh-card {
            padding: 1.1rem;
        }

        .wh-card-header {
            grid-template-columns: 52px minmax(0, 1fr);
            gap: 0.75rem;
            padding-bottom: 3.5rem;
        }

        .wh-icon {
            width: 52px;
            height: 52px;
            font-size: 1.25rem;
        }

        .wh-period {
            min-height: 27px;
            margin-bottom: 0.5rem;
            padding: 0.28rem 0.68rem;
            font-size: 0.73rem;
        }

        .wh-role {
            font-size: 1rem;
        }

        .wh-location,
        .wh-achievements li {
            font-size: 0.86rem;
        }

        .wh-toggle {
            min-height: 42px;
            font-size: 0.8rem;
        }

        .wh-toggle::after {
            font-size: 1.65rem;
        }

        .wh-skill {
            min-height: 31px;
            padding: 0.36rem 0.68rem;
            font-size: 0.72rem;
        }
    }

    @media (max-width: 420px) {
        .work-history-roadmap {
            padding-right: 0.7rem;
            padding-left: 0.7rem;
        }

        .wh-item {
            grid-template-columns: 30px minmax(0, 1fr);
            column-gap: 0.65rem;
        }

        .wh-timeline::before {
            left: 15px;
        }

        .wh-card {
            padding: 0.95rem;
            border-radius: 18px;
        }

        .wh-card-header {
            grid-template-columns: 1fr;
        }

        .wh-icon {
            width: 46px;
            height: 46px;
        }

        .wh-left .wh-card::after,
        .wh-right .wh-card::after {
            left: -14px;
            width: 14px;
        }
    }
</style>

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
