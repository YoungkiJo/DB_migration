from services.service import select_msdb_info, make_table


if __name__ == "__main__":
    ms_tables, ms_table_datatypes, ms_total_data = select_msdb_info()
    make_table(ms_tables, ms_table_datatypes, ms_total_data, "mysql")

    