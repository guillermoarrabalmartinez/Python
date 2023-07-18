"""App entry point."""
#from pandas_sqlalchemy import init_script
import os
from executions import join_twoxlsxfiles_add_reportingDate
from configuration.config import get_config
from sqlalchemy import types


# Invoke the get config from config.py 
config = get_config()
# Define instance parameters
connection_string = config['SQL']['localhost_CONNECTION_STRING']
file = config['Files']['TWIN_DEALS_2022_08_31']
file2 = config['Files']['TWIN_DEALS_2023_02_28']
folderpath = config['Files']['FolderPath']
allowed_filetypes = config['Files']['allowed_filetypes']
schema = "test"
table =  os.path.splitext(file)[0]
column_types_TD = {
    'TWIN_DEAL_ID': types.String(length=255),
    'Twin original': types.String(length=255),
    'PV Twin original': types.Numeric(precision=30, scale=10),
    'Twin generated': types.String(length=255),
    'PV Twin generated': types.Numeric(precision=30, scale=10),
    'Total': types.Numeric(precision=30, scale=10)
}
join_twoxlsxfiles_add_reportingDate(connection_string, folderpath, 
                                file, file2, allowed_filetypes, table, schema, column_types_TD)