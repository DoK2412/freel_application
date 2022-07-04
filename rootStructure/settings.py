from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_post: int = 8000
    database_url: str = 'postgresql://dok2413:451183311z@127.0.0.1/freelance'
    sikret_key_ucaller: str = 'cbcvaj8KNo8JBThm7ba6f5sdUzlmfdyc'
    service_id_ucaller: int = 955796


setting = Settings()