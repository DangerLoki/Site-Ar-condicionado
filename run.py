from src import create_app
from src.config import DevelopmentConfig


def main():
    """Entry point para `dev` definido no pyproject.toml."""
    app = create_app(DevelopmentConfig)
    app.run(debug=True, host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()


