import pandas as pd

class ImportFiles:
    """Class to manage the data import into the SQL Server database"""
    def __init__(self, filepath) -> None:
        self.filepath = filepath

    def read_csv_file(self, skip_rows=0):
        """read csv file
        :param int skip_rows: number of rows to skip in the header"""
        df = pd.read_csv(self.filepath, sep=",", skiprows=skip_rows)
        return df

    def read_excel_file(self, sheet_name, skip_rows=0, use_columns=None):
        """read excel file
        :param str sheet_name: name of the Excel sheet to be analyzed
        :param int skip_rows: number of rows to skip in the header
        :param list[str] use_columns: array of columns to be extracted, none by default"""
        df = pd.read_excel(self.filepath, sheet_name=sheet_name, skiprows=skip_rows, usecols=use_columns)
        return df
