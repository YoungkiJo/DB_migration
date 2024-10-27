use sqlx::types::{BigDecimal, chrono::NaiveDateTime};
use std::collections::HashMap;

#[derive(Debug)]
enum MySQLDataType {
    BigInt,
    VarChar(usize),
    Text,
    DateTime,
    Double,
    Decimal,
}

struct SQLServerToMySQL;

impl SQLServerToMySQL {
    fn ms_mysql_data_mapping() -> HashMap<&'static str, MySQLDataType> {
        let mut mapping_data = HashMap::new();

        mapping_data.insert("int", MySQLDataType::BigInt);
        mapping_data.insert("bigint", MySQLDataType::BigInt);
        mapping_data.insert("varchar", MySQLDataType::VarChar(1200));
        mapping_data.insert("nvarchar", MySQLDataType::VarChar(1200));
        mapping_data.insert("text", MySQLDataType::Text);
        mapping_data.insert("datetime", MySQLDataType::DateTime);
        mapping_data.insert("datetime2", MySQLDataType::DateTime);
        mapping_data.insert("float", MySQLDataType::Double);
        mapping_data.insert("decimal", MySQLDataType::Decimal);

        mapping_data
    }
}