import pandas as pd
def clean_data(df = pd.DataFrame()) -> pd.DataFrame:
    """
    Cleans the input DataFrame by performing the following operations:
    - Removes duplicate rows
    - Fills missing values with the mean of their respective columns
    - Strips leading and trailing whitespace from string columns

    Parameters:
    df (pd.DataFrame): The input DataFrame to be cleaned.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    # Remove duplicate rows
    df = df.drop_duplicates()

    #Add a new column 'tsunami_boolean' based on 'tsunami' column and keep the original 'tsunami' column
    if 'tsunami' in df.columns:
        original_tsunami_col = df['tsunami']
        df['tsunami_boolean'] = original_tsunami_col.astype(bool)

    return df