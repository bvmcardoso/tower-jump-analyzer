"""
Data cleaning module.
Flags invalid records without dropping them.
"""

import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepares the dataset by:
    - Converting LocalDateTime strings to datetime objects
    - Ensuring Latitude and Longitude are numeric
    - Marking each record as valid/invalid based on critical fields
    - Sorting all data chronologically

    Note: No records are deleted. Invalid entries are flagged with a 'Valid' column.

    Args:
        df (pd.DataFrame): Raw input dataframe

    Returns:
        pd.DataFrame: Full dataframe with a new 'Valid' column (True/False)
    """

    df["LocalDateTime"] = pd.to_datetime(
        df["LocalDateTime"],
        format="%m/%d/%y %H:%M",
        errors="coerce"
    )

    df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
    df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")

    df["Valid"] = df[["Latitude", "Longitude", "State", "LocalDateTime"]].notnull().all(axis=1)

    return df.sort_values(by="LocalDateTime").reset_index(drop=True)
