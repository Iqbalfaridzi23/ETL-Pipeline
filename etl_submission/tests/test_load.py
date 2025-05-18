import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pandas as pd
import os
from utils.load import load_data

class TestLoad(unittest.TestCase):
    def test_save_csv_file(self):
        df = pd.DataFrame({
            'Title': ['Shirt'],
            'Price': [10000.0],
            'Rating': [4.5],
            'Colors': [2],
            'Size': ['M'],
            'Gender': ['Men']
        })
        filename = "test_products.csv"
        load_data(df, filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()