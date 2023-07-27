"""App entry point."""
# from pandas_sqlalchemy import init_script
import os
from executions import join_twoxlsxfiles_add_reportingDate
from configuration.config import get_config
from sqlalchemy import types


# Invoke the get config from config.py
config = get_config()
# Define instance parameters
connection_string = config["SQL"]["localhost_CONNECTION_STRING"]
file = config["Files"]["NettingNegative"]
file2 = config["Files"]["NettingPositive"]
folderpath = config["Files"]["FolderPath"]
allowed_filetypes = config["Files"]["allowed_filetypes"]
schema = "test"
ifexists = "replace"  # 'append'
table = os.path.splitext(file)[0]
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


join_twoxlsxfiles_add_reportingDate(
    connection_string,
    folderpath,
    file,
    file2,
    allowed_filetypes,
    table,
    schema,
    ifexists,
    column_types_netting,
)
