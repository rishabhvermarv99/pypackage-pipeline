import pandas as pd

def load_file_to_dataframe(file_path, file_format):
    """
    Load a file into a Pandas DataFrame based on the specified file format.

    Parameters:
    - file_path (str): The path to the file.
    - file_format (str): The format of the file ("csv" or "excel").

    Returns:
    - pd.DataFrame: The loaded DataFrame.
    """
    if file_format == "csv":
        df = pd.read_csv(file_path)
    elif file_format == "excel":
        df = pd.read_excel(file_path)

    return df