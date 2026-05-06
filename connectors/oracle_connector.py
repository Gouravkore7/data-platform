import pandas as pd

class OracleConnector:

    def __init__(self, file_path):
        self.file_path = file_path

    def fetch_data(self):
        return pd.read_csv(self.file_path)