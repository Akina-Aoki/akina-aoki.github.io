from base64 import b64encode
from mimetypes import guess_type
from pathlib import Path

import streamlit as st


def image_to_data_uri(image_path: Path) -> str:
    """Convert a local image into a Base64 data URI."""

    mime_type = guess_type(image_path.name)[0] or "image/jpeg"
    encoded_image = b64encode(image_path.read_bytes()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded_image}"


def read_text_file(path: Path) -> str:
    """Read and return a UTF-8 text file."""

    return path.read_text(encoding="utf-8")


def load_css(path: Path) -> None:
    """Load a CSS file and inject it into the current Streamlit page."""

    css = read_text_file(path)
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)