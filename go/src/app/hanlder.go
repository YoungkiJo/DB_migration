package app

import (
	"database/sql"
	"db_migration/src/app/dblayer"
	"db_migration/src/database"
	"fmt"
)

func SelectMSDBInfo(msTables *[]string, msTableDatatypes *map[string][][2]string, msTotalData *map[string][][]interface{}) {
	msSQL, _ := database.LoadSQLSERVERInfo()
	queries := dblayer.MSTableQuery{}

	connString := fmt.Sprintf("server=%s;port=%d;user id=%s;password=%s;database=%s;",
		msSQL.Server, msSQL.Port, msSQL.User, msSQL.PW, msSQL.DB)

	db, err := sql.Open("mssql", connString)
	if err != nil {
		fmt.Errorf("데이터베이스에 연결할 수 없습니다.")
	}
	defer db.Close()

	query := queries.SelectTableInfo()
	rows, err := db.Query(query)
	if err != nil {
		fmt.Errorf("쿼리 실행 실패: %v", err)
	}
	defer rows.Close()

	for rows.Next() {
		var tableName string
		if err := rows.Scan(&tableName); err != nil {
			fmt.Errorf("결과를 스캔하는데 실패했습니다: %v", err)
		}
		*msTables = append(*msTables, tableName)
	}

	var columns [][2]string
	var colName, dtype string
	// var data [][]interface{}
	// var value interface{}
	for _, msTable := range *msTables {
		query = queries.SelectColumnDtypeInfo(msTable)
		colRows, err := db.Query(query)
		if err != nil {
			fmt.Errorf("쿼리 실행 실패: %v", err)
		}
		defer colRows.Close()

		for colRows.Next() {
			if err := colRows.Scan(&colName, &dtype); err != nil {
				fmt.Errorf("결과를 스캔하는데 실패했습니다: %v", err)
			}
			columns = append(columns, [2]string{colName, dtype})
		}
		(*msTableDatatypes)[msTable] = columns
	}
}
