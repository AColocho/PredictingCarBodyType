import os

class config:
    STATIC_IMAGES = os.getcwd()+'/app/static/images'
    
    @staticmethod
    def init_app(app):
        pass
    
    
class DevelopmentConfig(config):
    DEBUG=True

class ProductionConfig(config):
    DEBUG=False

config = {
    'development': DevelopmentConfig,
    'production':ProductionConfig}
