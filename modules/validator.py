# VALIDATION FUNCTIONS

def check_nulls(df):
    """
    Check missing values in dataset
    """
    return df.isnull().sum()


def detect_anomalies(df):
    """
    Detect abnormal price values
    """
    return df[df['price'] > 150]


def check_duplicates(df):
    """
    Check duplicate rows
    """
    return df[df.duplicated()]