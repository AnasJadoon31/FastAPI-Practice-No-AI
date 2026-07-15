from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabaseSettings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASS: str

    model_config = SettingsConfigDict(
        env_file="../.env",
        extra="ignore",
        env_ignore_empty=True
    )

settings = DatabaseSettings()

print(settings.POSTGRES_HOST)