import pandas as pd
import numpy as np

def load_testbench_data(file):
    # Decode bytes to string for line-by-line processing
    content = file.read().decode("utf-8").splitlines()

    # Identify the actual data header line
    data_start_idx = None
    for i, line in enumerate(content):
        if line.strip().startswith("Timestamp"):
            data_start_idx = i
            break

    if data_start_idx is None:
        raise ValueError("No valid header line starting with 'Timestamp' found.")

    # Read header and data
    header = content[data_start_idx].strip().split("\t")
    data_lines = content[data_start_idx + 1:]

    cleaned_data = []
    for line in data_lines:
        cols = line.strip().split("\t")
        if len(cols) == len(header):  # Ensure row length matches header
            cleaned_data.append(cols)

    # Convert to DataFrame
    df = pd.DataFrame(cleaned_data, columns=header)

    # Convert timestamp and numeric columns
    df["timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    df.drop(columns=["Timestamp"], inplace=True)

    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df.dropna(subset=["timestamp"])
