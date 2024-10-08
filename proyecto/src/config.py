class Config:
    SECRET_KEY = "&I^u26560WsJ4?Fl"

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = "frontenddecoracioneseventos.mysql.database.azure.com"
    MYSQL_USER = "JuanSalgado"
    MYSQL_PASSWORD = "&I^u26560WsJ4?Fl"
    MYSQL_DB = "decoraciones_eventos"
config = {
    'development': DevelopmentConfig
}
 