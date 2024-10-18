package database

import (
	"fmt"
	"log"
	"os"
	"strconv"

	"github.com/joho/godotenv"
)

type DBstruct struct {
	User   string
	PW     string
	Server string
	Port   int
	DB     string
}

func LoadSQLSERVERInfo() (*DBstruct, error) {
	err := godotenv.Load(".env")
	if err != nil {
		log.Fatal("환경 변수를 로드하는데 실패했습니다.", err)
	}

	port, err := strconv.Atoi(os.Getenv("Port"))
	if err != nil {
		return nil, fmt.Errorf("Port 환경변수가 잘못된 형식입니다.: %v", err)
	}

	dbinfo := &DBstruct{
		User:   os.Getenv("User"),
		PW:     os.Getenv("PW"),
		Server: os.Getenv("Server"),
		Port:   port,
		DB:     os.Getenv("DB"),
	}
	return dbinfo, nil
}
