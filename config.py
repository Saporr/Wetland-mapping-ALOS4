from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
ALOS_DIR = DATA_DIR / "alos_images"
GROUND_TRUTH = DATA_DIR / "ground_truth" / "data_part3.shp"
