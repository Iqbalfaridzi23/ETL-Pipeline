import pandas as pd

def transform_data(df):
    try:
        df = df.copy()

        df = df[~df['title'].str.contains("Unknown Product", na=False)]
        df = df[~df['Rating'].str.contains("Invalid Rating", na=False)]

        df['Price'] = pd.to_numeric(df['Price'].str.replace(r'[^\d.]', '', regex=True), errors='coerce') * 16000
        df['Rating'] = pd.to_numeric(df['Rating'].str.extract(r'(\d+(\.\d+)?)')[0], errors='coerce')
        df['Colors'] = pd.to_numeric(df['Colors'].str.extract(r'(\d+)')[0], errors='coerce')

        df['Size'] = df['Size'].str.replace('Size: ', '', regex=False)
        df['Gender'] = df['Gender'].str.replace('Gender: ', '', regex=False)

        df.dropna(subset=['Price', 'Rating', 'Colors', 'Size', 'Gender'], inplace=True)
        df.rename(columns={'title': 'Title'}, inplace=True)
        df.drop_duplicates(inplace=True)

        return df

    except Exception as e:
        print(f"[ERROR] Failed to transform data: {e}")
        return pd.DataFrame()
