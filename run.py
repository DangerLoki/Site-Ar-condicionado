from src import create_app
from src.config import DevelopmentConfig

if __name__ == "__main__":
    app = create_app(DevelopmentConfig)
    app.run(debug=True, host="0.0.0.0", port=5000)


