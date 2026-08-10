from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    host: str = "" 
    port: int = 8000   
    
    class Config:
        env_file = [".env", ".env.local"]
        
settings = Settings()