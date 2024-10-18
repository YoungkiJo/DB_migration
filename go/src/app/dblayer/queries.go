package dblayer

import "fmt"

type MSTableQuery struct{}

// TABLE_NAME을 선택하는 쿼리
func (m *MSTableQuery) SelectTableInfo() string {
	query := `
	SELECT TABLE_NAME
	FROM INFORMATION_SCHEMA.TABLES
	WHERE TABLE_TYPE = 'BASE TABLE'
	`
	return query
}

// 특정 테이블의 열 이름과 데이터 타입을 선택하는 쿼리
func (m *MSTableQuery) SelectColumnDtypeInfo(tableName string) string {
	query := fmt.Sprintf(`
	SELECT COLUMN_NAME, DATA_TYPE
	FROM INFORMATION_SCHEMA.COLUMNS
	WHERE TABLE_NAME = '%s';
	`, tableName)
	return query
}

// 특정 테이블의 모든 데이터를 선택하는 쿼리
func (m *MSTableQuery) SelectAllData(tableName string) string {
	query := fmt.Sprintf("SELECT * FROM %s", tableName)
	return query
}
