"""Testes para as configurações da aplicação."""
from src.config import Config, DevelopmentConfig, ProductionConfig
from src.routes import SERVICES, TESTIMONIALS


class TestConfig:
    """Testes das classes de configuração."""

    def test_config_base_tem_secret_key(self):
        assert Config.SECRET_KEY is not None
        assert len(Config.SECRET_KEY) > 0

    def test_config_base_debug_desligado(self):
        assert Config.DEBUG is False

    def test_development_config_debug_ligado(self):
        assert DevelopmentConfig.DEBUG is True

    def test_production_config_debug_desligado(self):
        assert ProductionConfig.DEBUG is False

    def test_freezer_destination_definido(self):
        assert hasattr(Config, "FREEZER_DESTINATION")

    def test_freezer_relative_urls_ativo(self):
        assert Config.FREEZER_RELATIVE_URLS is True


class TestAppFactory:
    """Testes do factory create_app."""

    def test_app_criada_com_sucesso(self, app):
        assert app is not None

    def test_modo_testing_ativo(self, app):
        assert app.config["TESTING"] is True

    def test_blueprint_main_registrado(self, app):
        assert "main" in app.blueprints

    def test_template_folder_correto(self, app):
        assert "templates" in app.template_folder

    def test_static_folder_correto(self, app):
        assert "static" in app.static_folder


class TestDados:
    """Testes de integridade dos dados (serviços e depoimentos)."""

    def test_servicos_nao_vazio(self):
        assert len(SERVICES) > 0

    def test_cada_servico_tem_campos_obrigatorios(self):
        for service in SERVICES:
            assert "icon" in service
            assert "title" in service
            assert "description" in service
            assert service["title"]
            assert service["description"]

    def test_depoimentos_nao_vazio(self):
        assert len(TESTIMONIALS) > 0

    def test_cada_depoimento_tem_campos_obrigatorios(self):
        for t in TESTIMONIALS:
            assert "name" in t
            assert "location" in t
            assert "stars" in t
            assert "text" in t

    def test_estrelas_depoimento_entre_1_e_5(self):
        for t in TESTIMONIALS:
            assert 1 <= t["stars"] <= 5

    def test_whatsapp_number_apenas_digitos(self):
        number = Config.COMPANY["whatsapp"]
        assert number.isdigit(), (
            "COMPANY['whatsapp'] deve conter apenas dígitos (sem +, espaços ou -)"
        )

    def test_whatsapp_number_tem_ddi_ddd(self):
        # DDI (55) + DDD (2 dígitos) + número (8-9 dígitos) = mínimo 12 dígitos
        assert len(Config.COMPANY["whatsapp"]) >= 12

    def test_company_tem_campos_obrigatorios(self):
        required = ["name", "city", "region", "phone", "whatsapp", "tagline"]
        for field in required:
            assert field in Config.COMPANY, f"COMPANY deve ter o campo '{field}'"
            assert Config.COMPANY[field], f"COMPANY['{field}'] não pode ser vazio"
