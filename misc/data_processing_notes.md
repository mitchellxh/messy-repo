# Data Processing Documentation

This document explains how to process the sales data files.

## Files Overview
- `sales_data_raw.txt` - Raw data from the database export
- `sales_data_processed-2.txt` - Second version of processed data
- `customer_data_raw.csv` - Customer information
- `customer_data_processed-v3.csv` - Latest customer data with categories

## Processing Steps
1. Extract raw data from database
2. Clean and format data
3. Apply business rules
4. Generate summary statistics

**Note**: The processing pipeline is scattered across multiple scripts and notebooks.
Some files may be outdated or contain bugs.

## Known Issues
- Inconsistent date formats
- Missing data validation
- No automated testing
- Multiple versions of the same analysis