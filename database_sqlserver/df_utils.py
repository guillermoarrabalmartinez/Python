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
            raise ValueError(
                "Invalid value type. Supported types are 'date' and 'fixed value'."
            )
        return df

    def df_netting_columnrenaming(self, df, netting_type="positive"):
        """rename the columns in case of netting files to match the databse names
        :param dataframe df: dataframe to be modified
        """
        # Netting Positive
        if netting_type == "positive":
            df = df.rename(
                columns={
                    "ST_LT_ALLOCATION.ST_LT": "STLT_ID",
                    "Portfolio Type": "PortfolioType",
                    "SAP Partner Type": "SAPPartnerType",
                    "Counterparty": "Counterparty",
                    "ENDUR_ID_ORIG": "EndurDealID",
                    "Gross assets before balance sheet netting": "Netting1",
                    "Netting": "Netting2",
                    "Net assets, reported on the balance sheet": "Netting3",
                    "Assets that are not subject to master netting agreements or are not subject to legally enforcable master netting agreements": "Netting4",
                    "Total assets recognized on the balance sheet": "Netting5",
                    "Financial liabilities": "Netting6",
                    "Assets after recognition of the netting-potential": "Netting7",
                }
            )
            print(df.columns.tolist())
        else:
            df = df.rename(
                columns={
                    "ST_LT_ALLOCATION.ST_LT": "STLT_ID",
                    "Portfolio Type": "PortfolioType",
                    "SAP Partner Type": "SAPPartnerType",
                    "Counterparty": "Counterparty",
                    "ENDUR_ID_ORIG": "EndurDealID",
                    "Gross liabilities before balance sheet netting": "Netting1",
                    "Netting": "Netting2",
                    "Net liabilities, reported on the balance sheet": "Netting3",
                    "Liabilities which are not subject to netting agreements or which are not subject to legally enforcable netting agreements": "Netting4",
                    "Total liabilities recognized on the balance sheet": "Netting5",
                    "Financial assets": "Netting6",
                    "Liabilities after recognition of the netting-potential": "Netting7",
                }
            )
            print(df.columns.tolist())
        return df

    def union_dataframes(self, df1, df2):
        """Perform a union of two dataframes
        :param dataframe df1: first dataframe
        :param dataframe df2: second dataframe
        :return: union of the two dataframes
        """
        return pd.concat([df1, df2], ignore_index=True)
