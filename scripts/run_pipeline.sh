#!/usr/bin/env bash
set -e

python3 src/bronze/ingest_bronze.py
python3 src/silver/transform_silver.py
python3 src/gold/build_gold.py
