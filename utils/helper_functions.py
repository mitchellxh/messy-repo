def load_data(file_path):
    """Load data from CSV file"""
    try:
        import pandas as pd
        return pd.read_csv(file_path)
    except ImportError:
        print("Pandas not available, using basic CSV reading")
        data = []
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:  # Skip header
                data.append(line.strip().split(','))
        return data

def calculate_stats(data):
    """Calculate basic statistics"""
    # This function needs improvement
    if isinstance(data, list):
        amounts = [float(row[4]) for row in data if len(row) > 4]
    else:
        amounts = data['Amount'].tolist()
    
    return {
        'total': sum(amounts),
        'average': sum(amounts) / len(amounts),
        'count': len(amounts)
    }

# Quick test
if __name__ == "__main__":
    print("Testing utility functions...")
    # Uncomment to test:
    # data = load_data("../raw_data/customer_data_raw.csv")
    # stats = calculate_stats(data)
    # print(stats)