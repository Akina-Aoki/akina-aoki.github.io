# Aira Franco — Data Engineer Portfolio

A static portfolio website for Aira Franco, showcasing her professional profile, education, work and volunteer experience, data engineering skills, projects, technology stack, and essay on AI-assisted engineering. The visual design preserves the original dark, technical identity while using only semantic HTML, CSS, and lightweight JavaScript.

## Live website

[https://akina-aoki.github.io/](https://akina-aoki.github.io/)

## Local preview

No installation or build step is required. From the repository root, start a local static server:

**Windows:**

```powershell
python -m http.server 8000
```

**macOS/Linux:**

```bash
python3 -m http.server 8000
```

Then open [http://localhost:8000/](http://localhost:8000/) in a browser.

## GitHub Pages deployment

The deployed site is plain HTML, CSS, and JavaScript. GitHub Pages can serve it directly from the repository root:

1. Open the repository **Settings** and select **Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select the publishing branch and the **`/ (root)`** folder.
4. Save and wait for GitHub Pages to publish the site.

The root `.nojekyll` file tells GitHub Pages to serve the files directly without Jekyll processing.

## Original Streamlit version

The original Python and Streamlit application is maintained separately at [Akina-Aoki/data_engineer_portfolio_streamlit](https://github.com/Akina-Aoki/data_engineer_portfolio_streamlit).
