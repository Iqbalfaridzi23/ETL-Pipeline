from utils.extract import extract_products
from utils.transform import transform_data
from utils.load import load_data


def main():
    print("Extracting data...")
    raw_data = extract_products()
    print("Raw data shape:", raw_data.shape)
    print(raw_data.head())

    print("Transforming data...")
    clean_data = transform_data(raw_data)
    print("Transformed data shape:", clean_data.shape)
    print(clean_data.head())

    print("Loading data...")
    load_data(clean_data)
    print("ETL pipeline complete. Data saved to products.csv")


if __name__ == "__main__":
    main()
