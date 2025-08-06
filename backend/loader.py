"""
Data loader module.
Responsible for reading the raw CSV input file.
"""


import pandas as pd
from config import INPUT_FILE

def load_data() -> pd.DataFrame:
    """
    Loads the CSV data file into a Pandas DataFrame.
    
    Returns:
        pd.DataFrame: Raw dataset with all available columns.
    
    Raises:
        FileNotFoundError: If the input file does not exist.
    """
    try:
        df = pd.read_csv(INPUT_FILE)
        return df
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Cannot read input file: {INPUT_FILE}") from e


