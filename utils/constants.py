from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ASSETS_PATH = PROJECT_ROOT / "assets"
STYLES_PATH = ASSETS_PATH / "style"

PROFILE_IMAGE = ASSETS_PATH / "profile_pic.jpg"
ROADMAP_IMAGE = ASSETS_PATH / "roadmap.png"
TECH_STACK_IMAGE = ASSETS_PATH / "data_engineering_tech_stack.png"
CIRCLE_GRAPH_IMAGE = ASSETS_PATH / "circle_graph.png"
POST_LITERATE_IMAGE_1 = ASSETS_PATH / "de_post_literate_1.jpg"
POST_LITERATE_IMAGE_2 = ASSETS_PATH / "de_post_literate_2.jpg"

RESUME_CANDIDATES = (
    ASSETS_PATH / "CV_Aira_Franco_en.pdf",
    ASSETS_PATH / "resume.pdf",
)
