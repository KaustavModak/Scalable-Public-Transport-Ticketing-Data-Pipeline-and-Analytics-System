# -----------------------------------
# TRANSFORMATION FUNCTIONS
# -----------------------------------

def normalize_price(df):
    """
    Normalize price column between 0 and 1
    Helps in scaling for analysis
    """
    df['price_norm'] = (df['price'] - df['price'].min()) / (df['price'].max() - df['price'].min())
    return df


def add_features(df):
    """
    Add new features if needed
    Example: price category
    """
    df['price_category'] = df['price'].apply(
        lambda x: 'Low' if x < 50 else 'Medium' if x < 80 else 'High'
    )
    return df


def aggregate(df):
    """
    Aggregate revenue by route
    """
    return df.groupby("route")["price"].sum()