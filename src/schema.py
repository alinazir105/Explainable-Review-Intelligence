BUSINESS_DTYPES = {
    'business_id': 'string',
    'name': 'string',
    'stars': 'float32',
    'review_count': 'int32',
}

BUSINESS_REQUIRED_COLUMNS = {
    'business_id',
    'stars',
    'review_count'
}


REVIEW_DTYPES = {
    'review_id': 'string',
    'business_id': 'string',
    'text': 'string',
    'stars': 'float32',
    'useful': 'int16',
    'funny': 'int16',
    'cool': 'int16',
}

REVIEW_REQUIRED_COLUMNS = {
    'review_id',
    'business_id',
    'text',
    'stars'
}

def validate_columns(df, required_columns):
    missing = required_columns - set(df.columns)
    
    if missing:
        raise ValueError(f"Missing required columns: {missing}")