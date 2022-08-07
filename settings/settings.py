from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str
    server_port: int
    database_url: str


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)