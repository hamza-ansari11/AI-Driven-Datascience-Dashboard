import pandas as pd

def load_data(uploaded_file):
    """Load CSV data."""
    try:
        df = pd.read_csv(uploaded_file)
        return df
    except Exception as e:
        raise ValueError(f"Could not read file: {e}")

def clean_data(df):
    """Clean the data by removing missing values."""
    # Removing rows with any missing values
    df_clean = df.dropna()
    return df_clean
