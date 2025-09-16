#!/bin/bash

# Data processing pipeline script
# WARNING: This script has not been tested thoroughly

echo "Starting data processing pipeline..."

# Check if required files exist
if [ ! -f "sensor_data_jan15.csv" ]; then
    echo "ERROR: sensor_data_jan15.csv not found"
    exit 1
fi

# Create output directory
mkdir -p output

# Process sensor data
echo "Processing sensor data..."
python3 scripts/process_sensors.py

# Generate reports
echo "Generating reports..."
python3 utils/generate_report.py

# Backup results
echo "Creating backups..."
cp output/*.csv backup/

echo "Processing complete!"
echo "Check output/ directory for results"

# TODO: Add error handling
# TODO: Add logging
# TODO: Test on different environments