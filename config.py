# Configuraciones Globales del servidor
class Config:
    pass


# Configuraciones especìficas, para desarrollo
class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}