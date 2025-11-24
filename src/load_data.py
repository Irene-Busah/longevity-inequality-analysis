# loading the relevant libraries
import pandas as pd
import os
import logging

# configuring the basic logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s - %(levelname)s - %(message)s]'
)


# defining the file paths
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_PATH = os.path.join(REPO_ROOT, "data", "raw")
PROCESSED_DATA_DIR = os.path.join(REPO_ROOT, "data", "processed")

# print()


# defining the function to load files
def load_csv(filename):
    """
    Loads data from a CSV file.

    Parameters
    ----------
    filename : str
        Either the file name (like 'gdp-per-capita.csv') 
        or a full/relative path ('data/raw/gdp-per-capita.csv').

    Returns
    -------
    pandas.DataFrame
        The loaded dataframe, or None if not found.
    """

    # Check if the user passed a full path
    if os.path.isabs(filename) or os.path.exists(filename):
        path = filename
    else:
        path = os.path.join(RAW_PATH, filename)

    try:
        df = pd.read_csv(path)
        logging.info(f"✅ Loaded successfully! Shape: {df.shape}")
        return df

    except FileNotFoundError:
        logging.error(f"❌ File not found: {path}")
        return None
    

def load_excel(filename):
    """Loads the data from Excel files"""

    # path = os.path.join(RAW_PATH, filename)
    try:
        dataframe = pd.read_excel(filename)
        logging.info("Data Loaded Successfully!")
        logging.info(dataframe.shape)
    
    except FileNotFoundError:
        logging.info("File not found")
        return None
    
    return dataframe


def load_json(filename):
    """Loads the data from JSON file"""

    # path = os.path.join(RAW_PATH, filename)
    try:
        dataframe = pd.read_json(filename)
        logging.info("Data Loaded Successfully!")
        logging.info(dataframe.shape)
    
    except FileNotFoundError:
        logging.info("File not found")
        return None
    
    return dataframe



# data = load_csv('gdp-per-capita.csv')
# print(data.shape)


