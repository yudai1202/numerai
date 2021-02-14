import pandas as pd


def get_group_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create features by calculating statistical moments for each group.

    :param df: Pandas DataFrame containing all features
    """
    for group in [
        "intelligence",
        "wisdom",
        "charisma",
        "dexterity",
        "strength",
        "constitution",
    ]:
        cols = [col for col in df.columns if group in col]
        df.loc[:, f"feature_{group}_mean"] = df.loc[:, cols].mean(axis=1)
        df.loc[:, f"feature_{group}_std"] = df.loc[:, cols].std(axis=1)
        df.loc[:, f"feature_{group}_skew"] = df.loc[:, cols].skew(axis=1)
    return df
