"""Repository paths shared by notebooks and supporting scripts."""

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DATASETS_DIR = REPO_ROOT / "datasets"
ARTIFACTS_DIR = REPO_ROOT / "artifacts"

