from html import escape

import streamlit as st

from content.personal_take_on_ai import ESSAY_PARAGRAPHS, ESSAY_TITLE, PAGE_TITLE
from utils.constants import (
    POST_LITERATE_IMAGE_1,
    POST_LITERATE_IMAGE_2,
    STYLES_PATH,
)
from utils.helpers import image_to_data_uri, load_css


load_css(
    STYLES_PATH / "theme.css",
    STYLES_PATH / "personal_take_on_ai.css",
)

image_details = (
    (
        POST_LITERATE_IMAGE_1,
        "Data engineering in a post-literate world — part one",
    ),
    (
        POST_LITERATE_IMAGE_2,
        "Data engineering in a post-literate world — part two",
    ),
)

missing_images = [path for path, _ in image_details if not path.exists()]
for missing_image in missing_images:
    st.warning(f"Image not found: `assets/{missing_image.name}`.")

images_html = "\n".join(
    (
        '<figure class="personal-take-image-frame">'
        f'<img src="{escape(image_to_data_uri(path), quote=True)}" '
        f'alt="{escape(alt_text, quote=True)}">'
        "</figure>"
        if path.exists()
        else (
            '<div class="personal-take-image-frame personal-take-image-missing" '
            'role="status">Image unavailable</div>'
        )
    )
    for path, alt_text in image_details
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
        <section class="personal-take-image-grid" aria-label="Post-literate data engineering illustrations">
            {images_html}
        </section>
        {paragraphs}
    </article>
</main>
"""

st.html(article_html)
