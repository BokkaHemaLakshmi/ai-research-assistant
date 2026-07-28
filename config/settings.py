import os 
from pydantic_settings import BaseSettings 
 
class Settings(BaseSettings): 
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "") 
    VECTOR_DB_DIR: str = os.getenv("VECTOR_DB_DIR", "./data/vector_db") 
    MODEL_PATH: str = os.getenv("MODEL_PATH", "./models/tf_classifier.h5") 
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./data/metadata.db") 
 
    class Config: 
        env_file = ".env" 
        extra = "ignore" 
 
settings = Settings() 
