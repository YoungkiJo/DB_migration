from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ms_server: str
    ms_port: int
    ms_user: str
    ms_pw: str
    ms_db: str

    post_user: str
    post_pw: str
    post_server: str
    post_port: str
    post_db: str

    my_user: str
    my_pw: str
    my_server: str
    my_port: str
    my_db: str

    class Config:
        env_file = ".env"