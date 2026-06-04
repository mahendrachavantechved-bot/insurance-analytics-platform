from src.duckdb_loader import DuckDBManager

db = DuckDBManager()

print(
    db.get_latest_results()
)

db.close()
