from pydantic import (
    AliasChoices,
    Field,
    PostgresDsn,
    RedisDsn,
)
from pydantic_settings import BaseSettings, SettingsConfigDict

from langchain.chat_models import init_chat_model

# Using for Loading LLM .env
# TODO: Wait to have more Idea to fix it.
class SettingsLLM(BaseSettings):
    
    api_key: str = Field(alias="OPENAI_API_KEY")
    model: str = Field(alias="LLM_MODEL")
    model_provider: str = Field(alias="LLM_PROVIDER")
    base_url: str = Field(alias="LLM_BASE_URL")
    top_p : float = Field(alias="LLM_TOP_P", default=0.5)
    
    # get LLM by Default
    def get_model(self, **kwargs):
        """
        Getting model from setting.
        
        """
        return init_chat_model(
            model=self.model,
            model_provider=self.model_provider,
            base_url=self.base_url,
            kwargs=kwargs
        )
        

# Using for Loading DB .env
class SettingsDB(BaseSettings):
    
    name: str = Field(alias="DB_NAME")
    host: str = Field(alias="DB_HOST")
    port: str = Field(alias="DB_PORT")
    username: str = Field(alias="DB_USERNAME")
    password: str = Field(alias="DB_PASSWORD")
    
    def get_postgres_uri(self):
        return f"postgresql+psycopg2://{self.username}:{self.password}@{self.host}:{self.port}/{self.name}"
 
# Using for Loading API .env
class SettingsAPI(BaseSettings):
    pass

# Using for Cache.
class SettingsCache(BaseSettings):
    pass

# Using for MCP.
class SettingsMCP(BaseSettings):
    pass

# Using for A2A
class SettingsA2A(BaseSettings):
    pass

if __name__ == "__main__":
    test = SettingsLLM()
    
    print(test.model_dump())