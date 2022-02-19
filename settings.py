from decouple import config


ENGINE_PATH = f"postgresql://{config('DB_USER')}:{config('DB_PWD')}@{config('DB_HOST')}/{config('DB')}"
