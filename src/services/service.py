import pymssql
from sqlalchemy import create_engine, MetaData, Table, Column, String, insert


from configs.config import Settings
from queries.query import ms_table_query
from models.ms_post_model import SQLSERVER2POST
from models.ms_my_model import SQLSERVER2MYSQL

def select_msdb_info():
    ms_sql = Settings()
    queries = ms_table_query()

    # SQL Server에 연결
    mssql_conn = pymssql.connect(
        server=ms_sql.ms_server,
        port=ms_sql.ms_port,
        user=ms_sql.ms_user,
        password=ms_sql.ms_pw,
        database=ms_sql.ms_db
    )

    cursor = mssql_conn.cursor()

    table_select_query = queries.select_table_info()

    cursor.execute(table_select_query)
    tables = cursor.fetchall()
    ms_tables = [table[0] for table in tables]


    table_datatype = dict()
    total_data = dict()
    for ms_table in ms_tables:
        column_info_query = queries.select_column_dtype_info(ms_table)

        cursor.execute(column_info_query)
        columns = cursor.fetchall()

        table_datatype[ms_table] = columns

        select_data_query = queries.select_all_data(ms_table)

        cursor.execute(select_data_query)
        data = cursor.fetchall()
        total_data[ms_table] = data

    # 연결 종료
    cursor.close()
    mssql_conn.close()

    return ms_tables, table_datatype, total_data



def make_table(ms_tables, ms_table_datatype, ms_total_data, dbtype: str):
    info = Settings()

    if dbtype == "postgresql":    
        DATABASE_URL = f"postgresql://{info.post_user}:{info.post_pw}@{info.post_server}:{info.post_port}/{info.post_db}"
        data_type_mapping = SQLSERVER2POST().ms_data_mapping()
    elif dbtype == "mysql":
        DATABASE_URL = f"mysql+pymysql://{info.my_user}:{info.my_pw}@{info.my_server}:{info.my_port}/{info.my_db}"
        data_type_mapping = SQLSERVER2MYSQL().ms_mysql_data_mapping()
    else:
        return
    
    engine = create_engine(DATABASE_URL)

    metadata = MetaData()

    for ms_table in ms_tables:
        columns = ms_table_datatype[ms_table]

        sqlalchemy_columns = []

        for column in columns:
            column_name = column[0]
            # data type을 소문자로 변경
            data_type = column[1].lower()
            # mapping 되지 않는 경우 기본 값
            pg_data_type = data_type_mapping.get(data_type, String)
            # SQLAlchemy의 Column 객체 생성
            sqlalchemy_columns.append(Column(column_name, pg_data_type))

        # SQLAlchemy의 Table 객체 생성
        table_obj = Table(ms_table.lower(), metadata, *sqlalchemy_columns)

        # PostgreSQL에서 테이블 생성
        metadata.create_all(engine, tables=[table_obj])
        print(f"Table {ms_table} created in DB.")


        ms_data = ms_total_data[ms_table]
        if ms_data:
            with engine.connect() as conn:
                for data in ms_data:
                    if data:
                        # 데이터 삽입
                        insert_stmt = insert(table_obj).values(dict(zip([column[0] for column in columns], data)))
                        conn.execute(insert_stmt)
                conn.commit()
                print(f"Data inserted into table {ms_table}.")
        else:
            print(f"No data found in table {ms_table}.")