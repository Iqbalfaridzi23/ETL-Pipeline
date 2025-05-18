import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from utils.extract import extract_products
import pandas as pd

class TestExtract(unittest.TestCase):
    def test_extract_returns_dataframe(self):
        df = extract_products(pages=1)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn("title", df.columns)
        self.assertIn("Price", df.columns)
        self.assertIn("Timestamp", df.columns)

if __name__ == "__main__":
    unittest.main()
