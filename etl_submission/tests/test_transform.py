import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from utils.transform import transform_data
import pandas as pd

class TestTransform(unittest.TestCase):
    def test_transform_valid_data(self):
        data = {
            'title': ['Jacket 1'],
            'Price': ['$100.00'],
            'Rating': ['4.5 / 5'],
            'Colors': ['3 Colors'],
            'Size': ['Size: M'],
            'Gender': ['Gender: Men']
        }
        df = pd.DataFrame(data)
        result = transform_data(df)
        self.assertEqual(result.shape[0], 1)
        self.assertTrue(pd.api.types.is_float_dtype(result['Price']))
        self.assertTrue(pd.api.types.is_integer_dtype(result['Colors']))
        self.assertIn("Title", result.columns)

if __name__ == "__main__":
    unittest.main()