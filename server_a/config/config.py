from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEBUG: bool = False

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
