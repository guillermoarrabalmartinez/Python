# Python work with SQL Server

Create a config.json file to put there your parameters:
``` 
{
    "SQL": {
        "CONNECTION_STRING_1": "mssql+pyodbc://test\\test/test?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server",
        "CONNECTION_STRING_2": "mssql+pyodbc://test/test?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server",
        "allowed_ifexiststable_Actions": ["replace", "append"]
    },
    "Files": {
        "Csv": "data.csv",
        "FolderPath": "C:\\Users\\test\\test\\test\\test\\",
        "allowed_filetypes": ["csv", "xlsx"],
        "Excel": "data.xlsx",
        "Excel1": "data1.xlsx"
    }
} 
```