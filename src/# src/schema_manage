# src/schema_manager.py

SCHEMA_SQL = """

CREATE TABLE IF NOT EXISTS portfolio_summary (
    portfolio_id VARCHAR,
    snapshot_date DATE,
    total_gwp DOUBLE,
    od_gwp DOUBLE,
    tp_gwp DOUBLE,
    combined_ratio DOUBLE,
    solvency_margin DOUBLE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS policy_master (
    policy_id VARCHAR,
    vehicle_class VARCHAR,
    channel VARCHAR,
    zone VARCHAR,
    premium DOUBLE,
    inception_date DATE,
    expiry_date DATE
);

CREATE TABLE IF NOT EXISTS claims_master (
    claim_id VARCHAR,
    policy_id VARCHAR,
    claim_date DATE,
    incurred_amount DOUBLE,
    paid_amount DOUBLE,
    status VARCHAR
);

CREATE TABLE IF NOT EXISTS simulation_runs (
    run_id VARCHAR,
    scenario_id VARCHAR,
    run_timestamp TIMESTAMP,
    iterations INTEGER,
    confidence_tier VARCHAR
);

CREATE TABLE IF NOT EXISTS simulation_results (
    run_id VARCHAR,
    scenario_id VARCHAR,
    metric_name VARCHAR,
    baseline DOUBLE,
    p10 DOUBLE,
    p50 DOUBLE,
    p90 DOUBLE,
    confidence_tier VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS validation_results (
    validation_id VARCHAR,
    run_id VARCHAR,
    directional_sanity VARCHAR,
    distribution_non_degenerate VARCHAR,
    scenario_ordering VARCHAR,
    overall_status VARCHAR,
    validation_timestamp TIMESTAMP
);

"""
