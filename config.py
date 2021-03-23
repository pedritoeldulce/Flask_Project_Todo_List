# Configuraciones Globales del servidor
class Config:
    SECRET_KEY = 'NoaYolandaAbigailPerezJustiniano_090118'  # key para autenticar los formularios


# Configuraciones especìficas, para desarrollo
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../app/database/db_proyect.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}