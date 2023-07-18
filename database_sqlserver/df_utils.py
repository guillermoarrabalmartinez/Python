import pandas as pd

class dfTransformations:
    """Class to manage make simple transformations to a dataframe"""
    def __init__(self, df):
        self.df = df

    def df_addcolumn(self, df, column_name, column_value, value_type):
        """read csv file
        :param dataframe df: dataframe to be modified
        :param str column_name: name of the new column
        :param str column_value: value of the new column
        :param array column_value: value of the new column
        """
        if value_type == "date":
            df[column_name] = pd.to_datetime(column_value)
        elif value_type == "fixed value":
            df[column_name] = column_value
        else:
            raise ValueError("Invalid value type. Supported types are 'date' and 'fixed value'.")
        return df
    
    def union_dataframes(self, df1, df2):
        """Perform a union of two dataframes
        :param dataframe df1: first dataframe
        :param dataframe df2: second dataframe
        :return: union of the two dataframes
        """
        return pd.concat([df1, df2], ignore_index=True)