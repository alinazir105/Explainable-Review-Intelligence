import pandas as pd
import ast

DICT_COLUMNS = ['attributes', 'hours']

def parse_string_dict(value):
    """
    Parse a string representation of a dictionary into an actual dictionary.
    """
    # Handle NaN values by returning an empty dictionary
    if pd.isna(value):
        return {}
    
    # If the value is already a dictionary, return it as is
    if isinstance(value, dict):
        return value
    
    # Attempt to parse the string as a dictionary
    try:
        return ast.literal_eval(value)
    except Exception:
        return {}
    

def normalize_dict_column(df, column):
    """
    Normalize specified columns in the DataFrame that contain string representations of dictionaries.
    """
    # Parse the string dictionaries into actual dictionaries
    parsed = df[column].apply(parse_string_dict)

    # Normalize the dictionaries into separate columns
    expanded = pd.json_normalize(parsed)

    # Rename the expanded columns to include the original column name as a prefix
    expanded.columns = [f"{column}_{c}" for c in expanded.columns]

    # Drop the original column and concatenate the expanded columns back to the DataFrame
    df = pd.concat([df.drop(column, axis=1), expanded], axis=1)
    
    return df

def normalize_nested_dict_column(df):
    for col in list(df.columns):
        if col.startswith('attributes_') or col.startswith('hours_'):
            series_as_str = df[col].astype(str)
        
            looks_like_dict = series_as_str.str.contains('{', regex=False) 

            if looks_like_dict.any():
                df = normalize_dict_column(df, col)

    return df


def clean_review_text(df):
    """
    Clean the review text by removing extra whitespace and converting to lowercase.
    """
    df['text'] = df['text'].str.strip()
    return df


def convert_boolean_attributes(df):
    """
    Convert attributes that are stored as strings but represent boolean values into actual boolean columns.
    """
    attributes_df = df.filter(like='attributes_')
    for col in attributes_df.columns:
        unique_values = attributes_df[col].dropna().unique()
        unique_values = [v for v in unique_values if v is not None]
        if set(unique_values).issubset({True, False}):
            df[col] = df[col].astype('boolean')

    return df