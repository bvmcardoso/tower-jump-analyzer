"""
Report exporter module.
Saves the analysis output into a CSV file with full visibility.
"""

import os
import pandas as pd
from config import OUTPUT_FILE

def export_report(df: pd.DataFrame):
    """
    Writes the result DataFrame to disk.
    Ensures output directory exists before saving.

    Args:
        df (pd.DataFrame): Final processed data including invalid records
    """
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)
    print({"Report saved on": OUTPUT_FILE})
