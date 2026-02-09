from src.io import load_dataset
from src.features import calculate_recency
from src.config import DATASET_PATH, DATE_COLUMN

def main():
    df = load_dataset(DATASET_PATH)

    df = calculate_recency(
        df=df,
        date_column=DATE_COLUMN
    )

    print(df.head())

if __name__ == "__main__":
    main()
