# src/logic.py

"""
Module docstring: Brief description of the module.
"""

import pandas as pd

def load_file_to_dataframe(file_path, file_format):
    """
    Function docstring: Description of the load_file_to_dataframe function.
    """
    if file_format == "csv":
        df = pd.read_csv(file_path)
    elif file_format == "excel":
        df = pd.read_excel(file_path)

    return df
