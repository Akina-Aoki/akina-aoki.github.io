# Aira Franco — Data Engineer Portfolio

A four-page static portfolio website for Aira Franco, showcasing her professional profile, experience, data engineering skills, projects, and essay on AI-assisted engineering. The visual design uses semantic HTML, shared CSS, and lightweight JavaScript.

## Website structure

- [`index.html`](index.html) — **Resume**
- [`tech-stack-and-skills.html`](tech-stack-and-skills.html) — **Tech Stack and Skills**
- [`projects.html`](projects.html) — **Projects**
- [`my-personal-take-on-ai.html`](my-personal-take-on-ai.html) — **My Personal Take on AI**

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
3. Select the **`main`** publishing branch and the **`/ (root)`** folder.
4. Save and wait for GitHub Pages to publish the site.

The root `.nojekyll` file tells GitHub Pages to serve the files directly without Jekyll processing.

## Original Streamlit version

The original Python and Streamlit application is maintained separately at [Akina-Aoki/data_engineer_portfolio_streamlit](https://github.com/Akina-Aoki/data_engineer_portfolio_streamlit).
