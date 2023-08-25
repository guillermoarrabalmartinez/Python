"""App entry point."""
#from pandas_sqlalchemy import init_script
import os
#from database_sqlserver.sql_utils import Database
#from database_sqlserver.sql_utils import ImportFiles
from executions import join_twoxlsxfiles_add_reportingDate, join_netting_files_and_importsqlserver
from configuration.config import get_config
from sqlalchemy import types


# Invoke the get config from config.py 
config = get_config()
# Define instance parameters
connection_string = config['SQL']['SUBDN748_CONNECTION_STRING']
file = config["Files"]["NettingPos31.03"]
file2 = config["Files"]["NettingPos28.02"]
folderpath = config['Files']['FolderPath']
allowed_filetypes = config['Files']['allowed_filetypes']
schema = "QV"
ifexists = "append"  # 'append','replace'
nettingtype = 'positive'
table =  "Netting_PositiveNegative" 
reporting_dates = ['2023-03-31', '2023-02-28']
#os.path.splitext(file)[0]
# # Create an instance of the Database class and pass the required arguments
# db = Database(connection_string, folderpath, file, allowed_filetypes)
# # Create an instance of the files class and pass the arguments.
# import_files = ImportFiles(folderpath + file)
# #Execute the function
# db.connect_and_load_to_sqlserver(import_files.read_csv_file(), table, schema,"replace")
# # test_result = db.execute_sql_query(f'SELECT TOP(5) * FROM {schema}.{table}')
# # Print the rows
column_types_TD = {
    'TWIN_DEAL_ID': types.String(length=255),
    'Twin original': types.String(length=255),
    'PV Twin original': types.Numeric(precision=30, scale=10),
    'Twin generated': types.String(length=255),
    'PV Twin generated': types.Numeric(precision=30, scale=10),
    'Total': types.Numeric(precision=30, scale=10)
}

column_types_netting = {
    "STLT_ID": types.String(length=255),
    "PortfolioType": types.String(length=255),
    "SAPPartnerType": types.String(length=255),
    "Counterparty": types.String(length=255),
    "EndurDealID": types.String(length=255),
    "Netting1": types.Float(precision=23),
    "Netting2": types.Float(precision=23),
    "Netting3": types.Float(precision=23),
    "Netting4": types.Float(precision=23),
    "Netting5": types.Float(precision=23),
    "Netting6": types.Float(precision=23),
    "Netting7": types.Float(precision=23),
    "ReportingDate": types.Date(),
}

# join_twoxlsxfiles_add_reportingDate(connection_string, folderpath, 
#                                 file, file2, allowed_filetypes, table, schema, column_types_TD)

join_netting_files_and_importsqlserver(
    connection_string,
    folderpath,
    file,
    file2,
    allowed_filetypes,
    table,
    schema,
    ifexists,
    reporting_dates,  
    netting_type=nettingtype,
    column_types=column_types_netting
)