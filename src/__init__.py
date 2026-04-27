from flask import Flask
from src.config import Config

def create_app(config=Config):
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )
    app.config.from_object(config)

    # Injeta dados da empresa em TODOS os templates automaticamente
    @app.context_processor
    def inject_company():
        return {"company": app.config["COMPANY"]}

    from src.routes import main
    app.register_blueprint(main)

    return app
