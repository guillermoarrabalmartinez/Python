import time
import os
import pandas as pd
import numpy as np
import sqlalchemy.schema
from sqlalchemy import create_engine, exc, types
from database_sqlserver.import_files import ImportFiles

class Database:
    """Pandas SQL Alquemy"""
    def __init__(self,connection_string, folderpath, file, allowed_filetypes):
        """Different parameters to be passed in the instance creation"""
        self.engine = create_engine(connection_string)
        self.file = file
        self.folderpath = folderpath
        self.allowed_filetypes = allowed_filetypes


    def connect_and_load_to_sqlserver(self, df, table_name: str, schema_name=None, if_exists='replace',column_types=None):
        """Function to connect and load a dataframe onto sqlserver sql:localhost
        :param df: dataframe to load to sql
        :param table_name: name of the table is going to be created
        :param schema_name: name of the schema in which the table will be allocated
        :param if_exists: in case you want to append change that parameter (replace/append)"""
        start_time = time.time()
        # Split the file name in case it has extension like: data.csv --> data
        table_name_simple = os.path.splitext(table_name)[0]
        # Create SQLAlchemy engine
        try:
            # Check if the schema exists
            #if not schema_exists(engine, schema_name):
            #    engine.execute(sqlalchemy.schema.CreateSchema(schema_name))
            #    raise ValueError(f"The schema '{schema_name}' does not exist.")
            df.to_sql(
                table_name_simple, 
                schema=schema_name, 
                con=self.engine, 
                if_exists=if_exists, 
                index=False,
                dtype=column_types)
            result_rows = f'Loaded {len(df)} rows INTO {table_name_simple} table.'
            result_time = "Table " + schema_name + "." + table_name_simple + " loaded in: {} seconds".format(time.time() - start_time)
            print(result_time)
            print(result_rows)
        except exc.SQLAlchemyError as e:
            print('An error occurred while loading the data into the SQL Server table.')
            print(f'Error details: {str(e)}')       


        def execute_sql_query(self, query: str):
            with self.engine.connect() as connection:
                connection.execute(query)


        def import_sqlserver_fromfile(self, filetype: str,folder_path: str, file_name: str, table_name:str ,schema_name=None, if_exists='replace',column_types=None,sheet_name=None,use_columns=None):
            """Function to connect and load a dataframe onto sqlserver from a file 
            :param df: dataframe to load to sql
            :param filetype: type of file to import (allowed: csv, xlsx)
            :param table_name: name of the table is going to be created
            :param schema_name: name of the schema in which the table will be allocated
            :param if_exists: in case you want to append change that parameter (replace/append)
            :param sheet_name: name of the sheet in the Excel file"""

            file_name = self.file
            folder_path = self.folder_path
            allowed_filetypes = self.allowed_filetypes
            if filetype not in allowed_filetypes:
                raise ValueError(f"Invalid filetype. Allowed filetypes: {', '.join(allowed_filetypes)}")
                return  # Exit the function if an error is raised
            elif filetype == 'csv':
                df = ImportFiles.read_csv_file(folder_path+file_name)
            elif filetype == 'xlsx' and sheet_name is not None:
                df = ImportFiles.read_excel_file(folder_path+file_name,sheet_name = sheet_name)
            else: print("something wrong")
            Database.connect_and_load_to_sqlserver(df,table_name,schema_name,)
