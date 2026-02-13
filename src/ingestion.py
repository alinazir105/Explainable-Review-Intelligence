import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def load_json_lines(path, dtype=None, nrows=None):
    """
    Load a JSON Lines file into a pandas DataFrame.
    """
    
    logging.info(f"Loading data from {path}")
    if nrows:
        df = pd.read_json(path, lines=True, dtype=dtype, nrows=nrows)
    else:
        df = pd.read_json(path, lines=True, dtype=dtype)

    logging.info(f"Loaded {len(df)} records from {path}")
    return df