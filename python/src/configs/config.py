from pydantic_settings import BaseSettings


class sqlserver_config(BaseSettings):
    ms_server: str
    ms_port: int
    ms_user: str
    ms_pw: str
    ms_db: str

    class Config:
        env_file = ".env"
        extra = "ignore"

class postgre_config(BaseSettings):
    post_user: str
    post_pw: str
    post_server: str
    post_port: str
    post_db: str

    class Config:
        env_file = ".env"
        extra = "ignore"


class mysql_config(BaseSettings):
    my_user: str
    my_pw: str
    my_server: str
    my_port: str
    my_db: str

    class Config:
        env_file = ".env"
        extra = "ignore"
