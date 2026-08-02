from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ASSETS_PATH = PROJECT_ROOT / "assets"

PROFILE_IMAGE = ASSETS_PATH / "profile_pic.jpg"
ROADMAP_IMAGE = ASSETS_PATH / "roadmap.png"
TECH_STACK_IMAGE = ASSETS_PATH / "de_tech_stack_pyramid.png"

RESUME_CANDIDATES = (
    ASSETS_PATH / "CV_Aira_Franco_en.pdf",
    ASSETS_PATH / "resume.pdf",
)