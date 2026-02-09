import pandas as pd

def calculate_recency(
    df: pd.DataFrame,
    date_column: str,
    reference_date: pd.Timestamp | None = None
) -> pd.DataFrame:
    """
    Calcula recência como diferença entre a data de referência (default: hoje)
    e a data da interação.
    """
    df = df.copy()

    df[date_column] = pd.to_datetime(df[date_column])

    if reference_date is None:
        reference_date = pd.Timestamp.today().normalize()

    df["recencia_dias"] = (reference_date - df[date_column]).dt.days

    return df
