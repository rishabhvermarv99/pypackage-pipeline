import unittest
import pandas as pd
from sigmoidpythonlib import myfunctions  

class TestMyFunctions(unittest.TestCase):

    def test_read_file(self):
        # Test reading a CSV file
        sample_csv = "sample.csv" 
        df = myfunctions.read_file(sample_csv)

        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 3)  
        self.assertEqual(len(df.columns), 3)  

    def test_write_dataframe_to_csv(self):
        
        sample_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        sample_df = pd.DataFrame(sample_data)
        output_csv = "output.csv"  

        myfunctions.write_dataframe_to_csv(sample_df, output_csv)
        df = myfunctions.read_file(output_csv)

        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), len(sample_df))
        self.assertEqual(len(df.columns), len(sample_df.columns))

if __name__ == '__main__':
    unittest.main()
