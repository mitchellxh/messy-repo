#!/usr/bin/env python3
"""
Data cleaning utilities
TODO: This script needs to be refactored
"""

def clean_data(filename):
    # Quick and dirty data cleaning
    with open(filename, 'r') as f:
        data = f.read()
    
    # Remove extra spaces
    cleaned = data.replace('  ', ' ')
    
    return cleaned

def process_csv(input_file, output_file):
    """Process CSV file - DEPRECATED, use new version"""
    import csv
    
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        with open(output_file, 'w') as outfile:
            writer = csv.writer(outfile)
            for row in reader:
                # Some processing logic here
                writer.writerow(row)

if __name__ == "__main__":
    print("Running data utils...")
    # clean_data("some_file.txt")