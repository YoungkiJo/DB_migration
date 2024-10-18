from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, TEXT, DATETIME, DOUBLE, DECIMAL

class SQLSERVER2MYSQL:
    # MySQL 데이터 타입 정의
    INT = BIGINT  # MySQL에서 INT와 BIGINT는 따로 있지만, BIGINT를 사용해 통일
    BIGINT = BIGINT
    VARCHAR = VARCHAR(1200)
    NVARCHAR = VARCHAR
    TEXT = TEXT
    DATETIME = DATETIME
    DATETIME2 = DATETIME  # MySQL에서는 DATETIME과 DATETIME2의 차이가 없으므로 같은 것으로 처리
    FLOAT = DOUBLE  # MySQL에서는 FLOAT와 DOUBLE을 분리하지만 DOUBLE로 매핑
    DECIMAL = DECIMAL

    def ms_mysql_data_mapping(self):
        mapping_data = {
            'int': SQLSERVER2MYSQL.INT,
            'bigint': SQLSERVER2MYSQL.BIGINT,
            'varchar': SQLSERVER2MYSQL.VARCHAR,
            'nvarchar': SQLSERVER2MYSQL.NVARCHAR,
            'text': SQLSERVER2MYSQL.TEXT,
            'datetime': SQLSERVER2MYSQL.DATETIME,
            'datetime2': SQLSERVER2MYSQL.DATETIME2,
            'float': SQLSERVER2MYSQL.FLOAT,
            'decimal': SQLSERVER2MYSQL.DECIMAL
        }
        return mapping_data