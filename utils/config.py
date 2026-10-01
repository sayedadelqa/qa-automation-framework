"""Central place for settings, so no URL or credential is hard-coded in tests."""
import json
import os
from pathlib import Path

BASE_URL = "https://www.saucedemo.com"
API_BASE_URL = os.getenv("API_BASE_URL", "https://dummyjson.com")

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_json(name: str):
    """Read a test-data file from the data/ folder."""
    with open(DATA_DIR / name, encoding="utf-8") as f:
        return json.load(f)
