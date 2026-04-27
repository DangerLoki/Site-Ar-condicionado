from flask import Blueprint, render_template, current_app
from urllib.parse import quote

main = Blueprint("main", __name__)

WHATSAPP_MESSAGE = "Olá! Gostaria de solicitar um orçamento de ar condicionado."

SERVICES = [
    {
        "icon": "❄️",
        "title": "Instalação",
        "description": (
            "Instalação profissional de aparelhos Split, Cassete, Janela e "
            "Piso-Teto com equipamentos e mão de obra de alta qualidade."
        ),
    },
    {
        "icon": "🔧",
        "title": "Manutenção Preventiva",
        "description": (
            "Revisão completa para garantir o funcionamento eficiente e "
            "prolongar a vida útil do seu equipamento."
        ),
    },
    {
        "icon": "🛠️",
        "title": "Manutenção Corretiva",
        "description": (
            "Diagnóstico rápido e reparo de qualquer falha no seu ar condicionado, "
            "com peças originais e garantia."
        ),
    },
    {
        "icon": "🧹",
        "title": "Limpeza e Higienização",
        "description": (
            "Higienização completa com produtos bactericidas, eliminando fungos, "
            "bactérias e ácaros do seu equipamento."
        ),
    },
    {
        "icon": "♻️",
        "title": "Recarga de Gás",
        "description": (
            "Recarga de fluido refrigerante R-22, R-410A e R-32 por "
            "técnicos certificados."
        ),
    },
    {
        "icon": "🏢",
        "title": "Projetos Comerciais",
        "description": (
            "Projetos completos de climatização para escritórios, lojas, "
            "restaurantes e galpões industriais."
        ),
    },
]

TESTIMONIALS = [
    {
        "name": "Carlos Mendes",
        "location": "Paulista, SP",
        "stars": 5,
        "text": (
            "Serviço excelente! A equipe chegou no horário marcado, foi super "
            "profissional e o preço foi justo. Recomendo!"
        ),
    },
    {
        "name": "Ana Paula Lima",
        "location": "Moema, SP",
        "stars": 5,
        "text": (
            "Fizeram a instalação de 3 aparelhos na minha loja rapidinho e sem "
            "sujeira. Atendimento via WhatsApp muito prático."
        ),
    },
    {
        "name": "Roberto Souza",
        "location": "Santo André, SP",
        "stars": 5,
        "text": (
            "Técnico muito competente, identificou o problema do meu ar na hora. "
            "Preço honesto e serviço garantido."
        ),
    },
]


@main.route("/")
def index():
    company = current_app.config["COMPANY"]
    whatsapp_url = f"https://wa.me/{company['whatsapp']}?text={quote(WHATSAPP_MESSAGE)}"
    return render_template(
        "index.html",
        services=SERVICES,
        testimonials=TESTIMONIALS,
        whatsapp_url=whatsapp_url,
    )

