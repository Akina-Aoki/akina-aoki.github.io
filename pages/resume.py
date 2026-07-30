from pathlib import Path
from textwrap import dedent
import base64

import streamlit as st


# =========================================================
# Project Paths & Assets
# =========================================================
PROJECT_ROOT = Path(__file__).resolve().parents[1]

PROFILE_IMAGE = PROJECT_ROOT / "assets" / "profile_pic.jpg"

RESUME_CANDIDATES = [
    PROJECT_ROOT / "assets" / "CV_Aira_Franco_en.pdf",
    PROJECT_ROOT / "assets" / "resume.pdf",
]

RESUME_FILE = next(
    (file for file in RESUME_CANDIDATES if file.exists()),
    RESUME_CANDIDATES[0],
)

TECH_STACK_IMAGE = (
    PROJECT_ROOT / "assets" / "de_tech_stack_pyramid.png"
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
    <h1 class="resume-name">Aira Franco</h1>
    <p class="resume-role">Aspiring Data Engineer</p>
    <div class="resume-summary">
        An aspiring data engineer experienced in architecting end-to-end
        data pipelines and platforms that transform raw data into reliable,
        tested, analytics-ready data for stakeholders. Experienced in
        designing pipelines, modelling data and enabling business
        decision-making through scalable data solutions. Adaptable to new
        tools, environments and domain-specific data ecosystems.
        <span class="work-authorization">
            Permanent work authorization in Sweden —
            no sponsorship required.
        </span>
    </div>
    <div class="link-mosaic">
        <a class="link-card youtube-card"
           href="https://www.youtube.com/@Aira_Data_Engineering"
           target="_blank"
           rel="noopener noreferrer"
           aria-label="Open Aira's YouTube channel">
            <span class="brand-mark youtube-mark">▶</span>
            <span class="link-copy">
                <span class="link-title">YouTube</span>
                <span class="link-description">Project demos</span>
            </span>
        </a>
        <a class="link-card linkedin-card"
           href="https://www.linkedin.com/in/aira-franco0965/"
           target="_blank"
           rel="noopener noreferrer"
           aria-label="Open Aira's LinkedIn profile">
            <span class="brand-mark linkedin-mark">in</span>
            <span class="link-copy">
                <span class="link-title">LinkedIn</span>
                <span class="link-description">Connect with me</span>
            </span>
        </a>
        <a class="link-card github-card"
           href="https://github.com/Akina-Aoki"
           target="_blank"
           rel="noopener noreferrer"
           aria-label="Open Aira's GitHub profile">
            <span class="brand-mark github-mark">&lt;/&gt;</span>
            <span class="link-copy">
                <span class="link-title">GitHub</span>
                <span class="link-description">View repositories</span>
            </span>
        </a>
        <a class="link-card blog-card"
           href="https://hashnode.com/@Aira"
           target="_blank"
           rel="noopener noreferrer"
           aria-label="Open Aira's projects blog">
            <span class="brand-mark blog-mark">▤</span>
            <span class="link-copy">
                <span class="link-title">Projects Blog</span>
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
    st.markdown(
        header_html,
        unsafe_allow_html=True,
    )


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
# Work History
# =========================================================
st.write("")
st.subheader("Work History")
st.write("---")


# Job 1
st.write("🚧 **Operations Assistant | Inditex**")
st.write("2020 – present")
st.write("Stockholm, Sweden")

st.write(
    """
    - Optimized inventory and logistics workflows across departments,
      improving product distribution efficiency under strict
      operational timelines.

    - Developed a strong understanding of stock movement, demand
      patterns and operational bottlenecks, directly informing my
      transition into data engineering for inventory and analytics
      systems.

    - **Skills:** Inventory Management, Retail Operations
    """
)

st.write("")


# Job 2
st.write("🚧 **English Language Teacher | Self-employed**")
st.write("2015 – 2019")
st.write("Sapporo, Japan")

st.write(
    """
    - Founded and operated an English tutoring business alongside
      university studies.

    - Delivered one-on-one and group lessons for children and adults,
      focusing on conversation, grammar and university exam readiness.

    - **Skills:** Language Teaching, Lesson Planning
    """
)

st.write("")


# Job 3
st.write("🚧 **Translator — Japanese ↔ English | Self-employed**")
st.write("2015 – 2019")
st.write("Sapporo, Japan")

st.write(
    """
    - Translated business and general documents between Japanese
      and English with precision and cultural sensitivity.

    - Managed timelines, priorities and delivery while working
      directly with clients to clarify requirements.

    - **Skills:** Translation, Client Communication
    """
)

st.write("")


# Job 4
st.write("🚧 **Hotel Receptionist | The Stay Sapporo Nagomi**")
st.write("2019")
st.write("Sapporo, Japan")

st.write(
    """
    - Handled front-office operations, guest relations and daily
      payment reconciliation to support efficient service.

    - **Skills:** Administration, Hospitality Service,
      Booking Systems
    """
)

st.write("")


# Job 5
st.write(
    "🚧 **Production Assistant | Krispy Kreme Doughnuts Japan**"
)
st.write("2018 – 2019")
st.write("Chitose, Japan")

st.write(
    """
    - Assisted with launching food-production workflows for the
      company's first store in the region.

    - Supported preparation, handling and production-flow
      coordination.

    - **Skills:** Food Production, Operational Coordination
    """
)

st.write("")


# Job 6
st.write("🚧 **Bartender | TK6 International Sports Bar**")
st.write("2016 – 2018")
st.write("Sapporo, Japan")

st.write(
    """
    - Managed daily bar operations, staff coordination and cost
      controls while studying at university.

    - **Skills:** Restaurant Operations, Team Coordination
    """
)

st.write("")


# Job 7
st.write("🚧 **Front Desk Assistant | Hilton**")
st.write("2016")
st.write("Sapporo, Japan")

st.write(
    """
    - Completed coursework and an internship involving reception
      duties and administrative coordination.

    - Helped maintain efficient internal processes and smooth
      day-to-day operations.

    - **Skills:** Hotel Operations, Administration
    """
)

st.write("")


# =========================================================
# Projects
# =========================================================
st.write("")
st.subheader("Projects")
st.write("---")


# Project 1
st.write(
    "🏆 **Data Platform for Retail Inventory & Sales**"
)

st.write(
    """
    *Docker | FastAPI | Kafka | Data Streaming | ETL | Pandas |
    Pydantic | PostgreSQL | Supabase | DuckDB | Evidence*
    """
)

st.write(
    """
    - Designed and implemented a data platform integrating APIs,
      streaming events and PostgreSQL to provide near real-time
      visibility into inventory and sales.

    - Enabled tracking of product performance and stock levels,
      supporting faster operational decisions and reducing the
      risk of stockouts.
    """
)

st.write("")


# Project 2
st.write(
    "🏆 **DataOps Pipeline: Validated ETL with PostgreSQL**"
)

st.write(
    "*SQL | DuckDB | Pandas | Pydantic | PostgreSQL | Evidence*"
)

st.write(
    """
    - Built a validated ETL pipeline that transforms raw CSV data
      into clean, analytics-ready datasets.

    - Applied data-quality rules with Pydantic and Pandas.

    - Loaded accepted and rejected records into PostgreSQL for
      transparency and reliable reporting.
    """
)

st.write("")


# Project 3
st.write("🏆 **YrkesCo Vocational School Database**")

st.write(
    "*Data Modelling | OLTP | PostgreSQL | Docker*"
)

st.write(
    """
    - Built a structured relational database for organizing and
      managing vocational-school data.

    - Applied normalization and data-integrity rules to keep the
      database accurate, consistent and suitable for daily operations.
    """
)

st.write("")


# Project 4
st.write(
    "🏆 **Sakila Database Exploratory Data Analysis**"
)

st.write(
    "*SQL | DuckDB | Pandas | Evidence*"
)

st.write(
    """
    - Explored and analyzed the Sakila dataset using SQL to identify
      trends, patterns and key insights.

    - Prepared clean, structured datasets for dashboards and reporting.
    """
)