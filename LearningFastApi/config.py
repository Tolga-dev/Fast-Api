class Settings:
    database_hostname = "localhost"
    database_port = 8000
    database_password = "Postgre"
    database_name = "postgres"  
    database_username = "postgres"
    secret_key = "HELLO_HANDSOME"
    algorithm = "HS256"
    access_token_expire_minutes = 10

    # def __init__(self, env_path=".deneme"):
    # 
    #     self._load_env_file(env_path)
    # 
    # def _load_env_file(self, env_path):
    #     try:
    #         with open(env_path, "r", encoding="utf-8") as file:
    #             for line in file:
    #                 line = line.strip()
    # 
    #                 if "=" in line:
    #                     key, value = line.split("=", 1)
    #                     key = key.strip()
    #                     value = value.strip().strip('"').strip("'")
    #                     attr_name = key.lower()
    #                     if hasattr(self, attr_name): 
    #                         setattr(self, attr_name, str(value))
    # 
    #     except FileNotFoundError:
    #         raise FileNotFoundError(f"The .deneme file at {env_path} was not found.")

settings = Settings()

# DATABASE_HOSTNAME=localhost
# DATABASE_PORT=8000
# DATABASE_PASSWORD=Postgre
# DATABASE_NAME=postgres
# DATABASE_USERNAME=postgres
# SECRET_KEY=HELLO_HANDSOME
# ALGORITHM=HS256
# ACCESS_TOKEN_EXPIRE_MINUTES=10



# from pydantic_settings import BaseSettings, SettingsConfigDict
# class Settings(BaseSettings):
#     tolga: str
#     model_config = SettingsConfigDict(env_file=".deneme")
#     
# settings = Settings()
# print(settings.tolga)
