# lakehouse-medallion-pipeline
Production-style medallion (bronze/silver/gold) pipeline with data quality, tests, and CI.


## Overview
This project demonstrates a production-style lakehouse medallion architecture:
- **Bronze**: Raw data ingestion (immutable)
- **Silver**: Data cleaning, validation, and deduplication
- **Gold**: Analytics-ready aggregations

The pipeline includes basic data quality checks and a CI workflow that runs on every push.

## Project Structure

## Run locally

Install dependencies:
```bash
pip install -r requirements.txt

python3 src/bronze/ingest_bronze.py
python3 src/silver/transform_silver.py
python3 src/gold/build_gold.py

