package main

import (
	"db_migration/src/app"

	_ "github.com/denisenkom/go-mssqldb"
)

func main() {
	var msTables []string
	msTableDatatypes := make(map[string][][2]string)
	msTotalData := make(map[string][][]interface{})

	app.SelectMSDBInfo(&msTables, &msTableDatatypes, &msTotalData)

}
