def load_data(df, filename='products.csv'):
    try:
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"[ERROR] Failed to save CSV: {e}")
