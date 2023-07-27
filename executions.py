from database_sqlserver.sql_utils import Database
from database_sqlserver.sql_utils import ImportFiles
from database_sqlserver.df_utils import dfTransformations


def import_csv_tosqlserver(
    connection_string, folderpath, file, allowed_filetypes, table, schema
):
    # Create an instance of the Database class and pass the required arguments
    db = Database(connection_string, folderpath, file, allowed_filetypes)
    # Create an instance of the files class and pass the arguments.
    import_files = ImportFiles(folderpath + file)
    # Execute the function
    db.connect_and_load_to_sqlserver(
        import_files.read_csv_file(), table, schema, "replace"
    )
    return print("Success joining dataframes")


def join_twoxlsxfiles_add_reportingDate(
    connection_string,
    folderpath,
    file1,
    file2,
    allowed_filetypes,
    table,
    schema,
    ifexists,
    column_types=None,
):
    # Create an instance of the Database class and pass the required arguments
    db = Database(connection_string, folderpath, file1, allowed_filetypes)

    # Create an instance of the files class and pass the arguments.
    import_files1 = ImportFiles(folderpath + file1)
    import_files2 = ImportFiles(folderpath + file2)

    # Process the first excel file
    df1 = import_files1.read_excel_file("Sheet1")
    dfUtils1 = dfTransformations(df1)
    df1 = dfUtils1.df_addcolumn(df1, "ReportingDate", "2022-08-31", "fixed value")

    # Process the second excel file
    df2 = import_files2.read_excel_file("Sheet1")
    dfUtils2 = dfTransformations(df2)
    df2 = dfUtils2.df_addcolumn(df2, "ReportingDate", "2023-02-28", "fixed value")

    # Union of two dataframes
    df = dfUtils1.union_dataframes(df1, df2)
    # Assuming there's a method to insert the dataframe into the database
    db.connect_and_load_to_sqlserver(df, table, schema, ifexists, column_types)
    return print("Success joining dataframes")


def join_netting_files_and_importsqlserver(
    connection_string,
    folderpath,
    file1,
    file2,
    allowed_filetypes,
    table,
    schema,
    ifexists,
    reporting_dates,  # Accept an array of two dates [date1, date2]
    netting_type='positive',
    column_types=None,
):
    # Create an instance of the Database class and pass the required arguments
    db = Database(connection_string, folderpath, file1, allowed_filetypes)

    # Create an instance of the files class and pass the arguments.
    import_files1 = ImportFiles(folderpath + file1)
    import_files2 = ImportFiles(folderpath + file2)

    # Unpack the reporting_dates array into two separate variables
    date1, date2 = reporting_dates

    # Process the first excel file
    df1 = import_files1.read_excel_file("Sheet1")
    dfUtils1 = dfTransformations(df1)
    df1 = dfUtils1.df_netting_columnrenaming(
    dfUtils1.df_addcolumn(df1, "ReportingDate", date1, "fixed value"), netting_type
    )


    # Process the second excel file
    df2 = import_files2.read_excel_file("Sheet1")
    dfUtils2 = dfTransformations(df2)
    df2 = dfUtils2.df_netting_columnrenaming(
    dfUtils2.df_addcolumn(df2, "ReportingDate", date2, "fixed value"), netting_type
    )

    # Union of two dataframes
    df = dfUtils1.union_dataframes(df1, df2)
    # Assuming there's a method to insert the dataframe into the database
    db.connect_and_load_to_sqlserver(df, table, schema, ifexists, column_types)
    return print("Success joining dataframes")