# Insurance Analytics Platform

## Architecture

GitHub
↓
Python Simulation Engine
↓
DuckDB
↓
Memgraph
↓
Streamlit Dashboard

## Components

### Simulation Layer

Existing Monte Carlo simulation engine.

### DuckDB Layer

System of record for:

- Portfolio
- Policies
- Claims
- Simulation Results
- Validation Results

### Memgraph Layer

Relationship intelligence:

- Scenarios
- Risk Drivers
- Vehicle Classes
- Validation Lineage

### Dashboard Layer

Streamlit executive analytics dashboard.

## Current Status

Phase 1:
Repository Initialization
