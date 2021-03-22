# Configuraciones Globales del servidor
class Config:
    SECRET_KEY = 'NoaYolandaAbigailPerezJustiniano_090118'  # key para autenticar los formularios


# Configuraciones especìficas, para desarrollo
class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}