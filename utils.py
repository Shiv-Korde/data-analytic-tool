import pandas as pd
import numpy as np

def load_testbench_data(file):
    return pd.read_csv(file, sep="\t")

def detect_anomalies(df, col, threshold=3.0):
    z_scores = (df[col] - df[col].mean()) / df[col].std()
    anomalies = df[np.abs(z_scores) > threshold]
    return anomalies
