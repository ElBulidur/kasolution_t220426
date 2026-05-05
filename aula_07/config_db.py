
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class ConfigDB:
    DB_CONFIG = {
        "host":"localhost",
        "user":"root",
        "password":"root",
        "database":"kasolution",
        "port":"3306"
    }
    
    DB_URL = f"mysql+pymysql://root:root@localhost:3306/kasolution"
    
    def pegar_config_db(self):
        return self.DB_CONFIG
    
    def pegar_url_db(self):
        return self.DB_URL
    
    
    
    
    
    
    
    