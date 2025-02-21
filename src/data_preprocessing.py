import pandas as pd

def preprocess_data(input_file):
    df = pd.read_csv(input_file)
    df['feedback'] = df['feedback'].str.lower()  # Example text cleaning
    # Add more preprocessing steps as needed
    return df
