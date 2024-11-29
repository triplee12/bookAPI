from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for the application."""
    PASSWORD : str
    DB_USER : str
    DB_NAME : str
    OAUTH_SECRET : str
    ACCESS_TOKEN_EXPIRY_WEEKS : int
    ALGORITHM : str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
