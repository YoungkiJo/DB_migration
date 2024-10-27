fn main() {
    let (ms_tables, ms_table_datatpes, ms_total_data) = select_msdb_info();
    make_table(ms_tables, ms_table_datatypes, ms_total_data, "postgresql")
}
