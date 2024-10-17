

class ms_table_query:
    def select_table_info(self):
        query = """
        SELECT TABLE_NAME
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_TYPE = 'BASE TABLE'
        """
        return query
    
    def select_column_dtype_info(self, table_name):
        query = f"""
        SELECT COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = '{table_name}';
        """
        return query
    
    def select_all_data(self, table_name):
        query = f"""
        SELECT * FROM {table_name}
        """
        return query