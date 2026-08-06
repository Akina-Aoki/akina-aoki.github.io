from html import escape

import streamlit as st

from content.personal_take_on_ai import ESSAY_PARAGRAPHS, ESSAY_TITLE, PAGE_TITLE
from utils.constants import STYLES_PATH
from utils.helpers import load_css


load_css(
    STYLES_PATH / "theme.css",
    STYLES_PATH / "personal_take_on_ai.css",
)

paragraphs = "\n".join(
    f'<p class="essay-paragraph{(" essay-conclusion" if index == len(ESSAY_PARAGRAPHS) - 1 else "")}">{escape(paragraph)}</p>'
    for index, paragraph in enumerate(ESSAY_PARAGRAPHS)
)

article_html = f"""
<main class="personal-take-main">
    <article class="personal-take-article">
        <header class="personal-take-header">
            <h1>{escape(PAGE_TITLE)}</h1>
            <h2>{escape(ESSAY_TITLE)}</h2>
        </header>
        {paragraphs}
    </article>
</main>
"""

st.html(article_html)
