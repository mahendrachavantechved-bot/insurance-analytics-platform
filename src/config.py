# src/config.py

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATABASE_DIR = PROJECT_ROOT / "database"
DATABASE_DIR.mkdir(exist_ok=True)

DUCKDB_PATH = DATABASE_DIR / "analytics.duckdb"

DATA_DIR = PROJECT_ROOT / "data"

RAW_DIR = DATA_DIR / "raw"
PARQUET_DIR = DATA_DIR / "parquet"
RESULTS_DIR = DATA_DIR / "results"
GRAPH_EXPORT_DIR = DATA_DIR / "graph_exports"

RAW_DIR.mkdir(parents=True, exist_ok=True)
PARQUET_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_EXPORT_DIR.mkdir(parents=True, exist_ok=True)
