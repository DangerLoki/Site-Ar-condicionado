"""Testes para as rotas / views da aplicação."""
from src.routes import SERVICES, TESTIMONIALS
from src.config import Config


class TestIndexPage:
    """Testes da rota principal '/'."""

    def test_status_200(self, client):
        """Página inicial deve retornar HTTP 200."""
        response = client.get("/")
        assert response.status_code == 200

    def test_content_type_html(self, client):
        """Resposta deve ser HTML."""
        response = client.get("/")
        assert "text/html" in response.content_type

    def test_titulo_empresa_presente(self, client):
        """Nome da empresa deve aparecer na página."""
        response = client.get("/")
        assert b"ClimaMax" in response.data

    def test_localizacao_sao_paulo(self, client):
        """Referência a São Paulo deve estar na página."""
        response = client.get("/")
        assert b"Paulo" in response.data

    def test_link_whatsapp_presente(self, client):
        """Link do WhatsApp (wa.me) deve estar na página."""
        response = client.get("/")
        assert b"wa.me" in response.data

    def test_numero_whatsapp_no_link(self, client):
        """Número do WhatsApp definido em COMPANY deve aparecer no link."""
        response = client.get("/")
        number = Config.COMPANY["whatsapp"].encode()
        assert number in response.data

    def test_secao_servicos_presente(self, client):
        """Seção de serviços deve estar na página."""
        response = client.get("/")
        assert b"Servi" in response.data  # "Serviços" (UTF-8 safe)

    def test_todos_servicos_renderizados(self, client):
        """Todos os títulos de serviços devem aparecer na página."""
        response = client.get("/")
        for service in SERVICES:
            assert service["title"].encode() in response.data

    def test_secao_depoimentos_presente(self, client):
        """Seção de depoimentos deve estar na página."""
        response = client.get("/")
        assert b"clientes" in response.data.lower()

    def test_todos_depoimentos_renderizados(self, client):
        """Todos os nomes dos depoimentos devem aparecer na página."""
        response = client.get("/")
        for t in TESTIMONIALS:
            assert t["name"].encode() in response.data

    def test_botao_flutuante_whatsapp(self, client):
        """Botão flutuante do WhatsApp deve estar no HTML."""
        response = client.get("/")
        assert b"whatsapp-float" in response.data

    def test_secao_sobre_presente(self, client):
        """Seção 'Sobre' deve estar na página."""
        response = client.get("/")
        assert b"sobre" in response.data.lower()

    def test_rota_inexistente_retorna_404(self, client):
        """Rota desconhecida deve retornar 404."""
        response = client.get("/pagina-que-nao-existe")
        assert response.status_code == 404


class TestStaticFiles:
    """Testes para arquivos estáticos."""

    def test_css_acessivel(self, client):
        """Arquivo CSS principal deve ser servido."""
        response = client.get("/static/css/style.css")
        assert response.status_code == 200

    def test_js_acessivel(self, client):
        """Arquivo JS principal deve ser servido."""
        response = client.get("/static/js/main.js")
        assert response.status_code == 200

    def test_whatsapp_svg_acessivel(self, client):
        """Ícone do WhatsApp deve ser servido."""
        response = client.get("/static/img/whatsapp.svg")
        assert response.status_code == 200
