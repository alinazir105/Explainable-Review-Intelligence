from .ingestion import load_json_lines
from .cleaning import normalize_dict_column, clean_review_text, normalize_nested_dict_column, convert_boolean_attributes
from .cleaning import DICT_COLUMNS
from .schema import BUSINESS_DTYPES, BUSINESS_REQUIRED_COLUMNS, REVIEW_DTYPES, REVIEW_REQUIRED_COLUMNS
from .schema import validate_columns

def build_business_table(path):
    df = load_json_lines(path, dtype=BUSINESS_DTYPES)

    validate_columns(df, BUSINESS_REQUIRED_COLUMNS)

    for col in DICT_COLUMNS:
        if col in df.columns:
            df = normalize_dict_column(df, col)

    df = normalize_nested_dict_column(df)
    df = convert_boolean_attributes(df)
    return df


def build_review_table(path, sample=None):
    df = load_json_lines(path, dtype=REVIEW_DTYPES)

    validate_columns(df, REVIEW_REQUIRED_COLUMNS)
    
    df = clean_review_text(df)
    
    if sample:
        df = df.sample(n=sample, random_state=42)

    return df