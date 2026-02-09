# Responsável apenas por leitura/escrita.
import pandas as pd

def load_dataset(path: str, sep: str = ",") -> pd.DataFrame:
    df = pd.read_csv(path, sep=sep)
    return df
