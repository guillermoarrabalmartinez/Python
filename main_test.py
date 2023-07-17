"""App entry point."""
#from pandas_sqlalchemy import init_script
import os
from database_sqlserver.sql_utils import Database
from database_sqlserver.sql_utils import ImportFiles
from configuration.config import get_config


# Invoke the get config from config.py 
config = get_config()
# Define instance parameters
connection_string = config['SQL']['localhost_CONNECTION_STRING']
file = config['Files']['PD1PFile']
folderpath = config['Files']['FolderPath']
allowed_filetypes = config['Files']['allowed_filetypes']
schema = "test"
table =  os.path.splitext(file)[0]
# Create an instance of the Database class and pass the required arguments
db = Database(connection_string, folderpath, file, allowed_filetypes)
# Create an instance of the files class and pass the arguments.
import_files = ImportFiles(folderpath + file)



db.connect_and_load_to_sqlserver(import_files.read_csv_file(), table, schema,"replace")
# test_result = db.execute_sql_query(f'SELECT TOP(5) * FROM {schema}.{table}')
# Print the rows
