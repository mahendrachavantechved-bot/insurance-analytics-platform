# src/duckdb_loader.py

import uuid
import duckdb
import pandas as pd

from src.config import (
    DUCKDB_PATH,
    PARQUET_DIR
)

from src.schema_manager import SCHEMA_SQL


class DuckDBManager:

    def __init__(self):
        self.conn = duckdb.connect(str(DUCKDB_PATH))
        self.initialize_schema()

    def initialize_schema(self):
        self.conn.execute(SCHEMA_SQL)
        print("Schema initialized.")

    def save_simulation_result(self, result):

        run_id = str(uuid.uuid4())

        self.conn.execute(
            """
            INSERT INTO simulation_runs
            VALUES (?, ?, CURRENT_TIMESTAMP, ?, ?)
            """,
            [
                run_id,
                result.scenario_id,
                result.iterations,
                result.confidence_tier
            ]
        )

        self.conn.execute(
            """
            INSERT INTO simulation_results
            (
                run_id,
                scenario_id,
                metric_name,
                baseline,
                p10,
                p50,
                p90,
                confidence_tier
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                run_id,
                result.scenario_id,
                result.metric_name,
                result.baseline_value,
                result.p10,
                result.p50,
                result.p90,
                result.confidence_tier
            ]
        )

        self.conn.commit()

        return run_id

    def save_validation_result(
            self,
            run_id,
            directional_sanity,
            distribution_non_degenerate,
            scenario_ordering,
            overall_status):

        validation_id = str(uuid.uuid4())

        self.conn.execute(
            """
            INSERT INTO validation_results
            VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            """,
            [
                validation_id,
                run_id,
                directional_sanity,
                distribution_non_degenerate,
                scenario_ordering,
                overall_status
            ]
        )

        self.conn.commit()

    def get_latest_results(self):

        query = """
        SELECT *
        FROM simulation_results
        ORDER BY created_at DESC
        """

        return self.conn.execute(query).df()

    def export_table_to_parquet(self,
                                table_name,
                                file_name):

        output_path = PARQUET_DIR / file_name

        query = f"""
        COPY (
            SELECT *
            FROM {table_name}
        )
        TO '{output_path}'
        (FORMAT PARQUET);
        """

        self.conn.execute(query)

        print(f"Exported: {output_path}")

    def load_policy_parquet(self,
                            parquet_file):

        df = pd.read_parquet(parquet_file)

        self.conn.register(
            "policy_df",
            df
        )

        self.conn.execute(
            """
            INSERT INTO policy_master
            SELECT *
            FROM policy_df
            """
        )

        self.conn.commit()

    def load_claims_parquet(self,
                            parquet_file):

        df = pd.read_parquet(parquet_file)

        self.conn.register(
            "claims_df",
            df
        )

        self.conn.execute(
            """
            INSERT INTO claims_master
            SELECT *
            FROM claims_df
            """
        )

        self.conn.commit()

    def close(self):
        self.conn.close()
