from sqlalchemy.dialects.postgresql import VARCHAR, BIGINT, TIMESTAMP, DOUBLE_PRECISION, NUMERIC

class SQLSERVER2POST:
    # SQLAlchemy 데이터 타입 정의
    INT = BIGINT
    BIGINT = BIGINT
    VARCHAR = VARCHAR
    NVARCHAR = VARCHAR  # NVARCHAR를 VARCHAR로 매핑
    TEXT = VARCHAR
    DATETIME = TIMESTAMP
    DATETIME2 = TIMESTAMP
    FLOAT = DOUBLE_PRECISION
    DECIMAL = NUMERIC

    def ms_post_data_mapping(self):
        mapping_data = {
        'int': SQLSERVER2POST.INT,
        'bigint': SQLSERVER2POST.BIGINT,
        'varchar': SQLSERVER2POST.VARCHAR,
        'nvarchar': SQLSERVER2POST.NVARCHAR,
        'text': SQLSERVER2POST.TEXT,
        'datetime': SQLSERVER2POST.DATETIME,
        'datetime2': SQLSERVER2POST.DATETIME2,
        'float': SQLSERVER2POST.FLOAT,
        'decimal': SQLSERVER2POST.DECIMAL
        }
        return mapping_data