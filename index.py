"""Flask API"""
from src.configs import AppConfig
from src import init_app

app = init_app(AppConfig)


if __name__ == '__main__':
    app.run(
        host=AppConfig.HOST,
        port=AppConfig.PORT,
        debug=AppConfig.DEBUG
    )
