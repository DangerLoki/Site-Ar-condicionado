import pytest
from src import create_app
from src.config import Config


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False


@pytest.fixture
def app():
    """Cria a aplicação Flask em modo de teste."""
    app = create_app(TestingConfig)
    yield app


@pytest.fixture
def client(app):
    """Cliente HTTP para fazer requisições nos testes."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Runner para testar CLI commands."""
    return app.test_cli_runner()
