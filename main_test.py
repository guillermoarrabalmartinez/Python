"""App entry point."""
# from pandas_sqlalchemy import init_script
import os
from executions import join_twoxlsxfiles_add_reportingDate, join_netting_files_and_importsqlserver
from configuration.config import get_config
from sqlalchemy import types


# Invoke the get config from config.py
config = get_config()
# Define instance parameters
connection_string = config["SQL"]["localhost_CONNECTION_STRING"]
file = config["Files"]["NettingNeg31.03"]
file2 = config["Files"]["NettingNeg28.02"]
folderpath = config["Files"]["FolderPath"]
allowed_filetypes = config["Files"]["allowed_filetypes"]
schema = "test"
ifexists = "replace"  # 'append'
table = os.path.splitext(file)[0]
reporting_dates = ['2023-03-31', '2023-02-28']
column_types_TD = {
    "TWIN_DEAL_ID": types.String(length=255),
    "Twin original": types.String(length=255),
    "PV Twin original": types.Numeric(precision=30, scale=10),
    "Twin generated": types.String(length=255),
    "PV Twin generated": types.Numeric(precision=30, scale=10),
    "Total": types.Numeric(precision=30, scale=10),
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


# join_twoxlsxfiles_add_reportingDate(
#     connection_string,
#     folderpath,
#     file,
#     file2,
#     allowed_filetypes,
#     table,
#     schema,
#     ifexists,
#     column_types_netting,
# )

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
    netting_type='negative',
    column_types=column_types_netting
)
