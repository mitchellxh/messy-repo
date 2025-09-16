#!/usr/bin/env python3

# Quick script to generate some test data
# This is just a temporary file - probably should be deleted

import random
import csv
from datetime import datetime, timedelta

products = ['Widget A', 'Widget B', 'Widget C', 'Gadget X', 'Tool Y']
regions = ['North', 'South', 'East', 'West', 'Central']
salespeople = ['John Smith', 'Jane Doe', 'Bob Johnson', 'Alice Brown', 'Mike Wilson']

def generate_sales_data(num_records=50):
    """Generate random sales data for testing"""
    data = []
    start_date = datetime(2023, 1, 1)
    
    for i in range(num_records):
        record = {
            'Date': (start_date + timedelta(days=i)).strftime('%Y-%m-%d'),
            'Product': random.choice(products),
            'Sales': random.randint(100, 500),
            'Region': random.choice(regions),
            'Salesperson': random.choice(salespeople)
        }
        data.append(record)
    
    return data

if __name__ == "__main__":
    # Uncomment to generate test data:
    # data = generate_sales_data()
    # print(f"Generated {len(data)} records")
    pass