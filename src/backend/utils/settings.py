from pydantic import (
    AliasChoices,
    Field,
    PostgresDsn,
    RedisDsn,
)
from pydantic_settings import BaseSettings, SettingsConfigDict

# Using for Loading LLM .env
class SettingsLLM(BaseSettings):
    
    api_key: str = Field(alias="LLM_API_KEY")

    model: str = Field(alias="LLM_MODEl")
    

# Using for Loading DB .env
class SettingsDB(BaseSettings):
    pass


# Using for Loading API .env
class SettingsAPI(BaseSettings):
    pass

if __name__ == "__main__":
    test = SettingsLLM()
    
    print(SettingsLLM().model_dump())