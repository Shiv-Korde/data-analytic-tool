import pandas as pd
import numpy as np
import csv

def load_testbench_data(file):
    # Read the first few lines to guess delimiter
    try:
        sample = file.read(2048).decode("utf-8")
        file.seek(0)  # Reset pointer
        dialect = csv.Sniffer().sniff(sample)
        delimiter = dialect.delimiter
    except Exception:
        delimiter = ","  # Fallback if delimiter cannot be detected

    return pd.read_csv(file, sep=delimiter)

def detect_anomalies(df, col, threshold=3.0):
    z_scores = (df[col] - df[col].mean()) / df[col].std()
    return df[np.abs(z_scores) > threshold]
