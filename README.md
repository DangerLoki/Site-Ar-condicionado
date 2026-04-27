# ❄️ Ale Ar-Condicionado — Site Institucional

> Site institucional para divulgação de uma empresa de ar-condicionado, desenvolvido com **Flask + Frozen-Flask** e publicado como um site **100% estático**, pronto para deploy em GitHub Pages, Netlify, Vercel, Cloudflare Pages ou qualquer hospedagem estática.

## 🖥️ Preview

![Preview do site](docs/assets/preview.gif)

| Seção | Descrição |
|---|---|
| **Hero** | Chamada principal com CTA direto para WhatsApp |
| **Serviços** | Cards com os principais serviços oferecidos |
| **Sobre** | Estatísticas da empresa e diferenciais |
| **Depoimentos** | Avaliações de clientes |
| **Contato** | CTA final com informações de atendimento e botão flutuante do WhatsApp |

---

## 🛠️ Tecnologias

- **Python 3.14** — linguagem principal
- **Flask 3** — framework web usado como motor de templates com Jinja2
- **Frozen-Flask** — geração de arquivos estáticos na pasta `build/`
- **pytest + pytest-flask** — testes automatizados
- **HTML5 / CSS3 / JavaScript** — estrutura, estilo e interações do front-end
- **Google Fonts** — tipografia
- **WhatsApp API** — link direto `wa.me` para contato

---

## 🎯 Objetivo do Projeto

O projeto foi criado para atender uma necessidade real de presença digital de uma pequena empresa local, mantendo baixo custo de hospedagem e manutenção simples.

A escolha por **Flask + Frozen-Flask** permite desenvolver com organização de templates, rotas e configuração centralizada, mas entregar em produção apenas arquivos estáticos, sem necessidade de servidor Python, banco de dados ou backend ativo.

---

## 📁 Estrutura do Projeto

```text
.
├── run.py              # Servidor de desenvolvimento
├── freeze.py           # Geração do site estático
├── pyproject.toml      # Dependências e configuração do projeto
├── .github/
│   └── workflows/
│       └── deploy.yml  # CI/CD GitHub Actions
├── docs/
│   └── assets/
│       └── preview.gif # GIF de demonstração do site
├── tests/
│   ├── conftest.py
│   ├── test_config.py
│   └── test_routes.py
└── src/
    ├── __init__.py     # App factory Flask
    ├── config.py       # Configurações e dados da empresa
    ├── routes/
    │   └── __init__.py # Blueprint + dados de serviços/depoimentos
    ├── static/
    │   ├── css/style.css
    │   ├── img/whatsapp.svg
    │   └── js/main.js
    └── templates/
        └── index.html
```
---

## ⚙️ Configuração da Empresa

Todos os dados principais da empresa ficam centralizados em **`src/config.py`**.

Alterar essas informações em um único arquivo reflete no site inteiro:

```python
COMPANY = {
    "name": "Ale Ar-condicionado",
    "tagline": "Especialistas em climatização em São Paulo e Grande SP.",
    "city": "São Paulo",
    "region": "Grande SP",
    "phone": "(11) 96105-6924",
    "whatsapp": "5511961056924",
    "email": "contato@alearcondicionado.com.br",
    "hours": "Seg – Sab: 08h às 18h",
    "founded": "2014",
    "clients": "5.000+",
    "experience": "10+",
    "satisfaction": "98%",
    "response": "15min",
}
```

---

## 🚀 Como Rodar

### 1. Clonar o repositório

```bash
git clone https://github.com/DangerLoki/Site-Ar-condicionado.git
cd Site-Ar-condicionado
```

### 2. Criar e ativar o ambiente virtual

Linux/Mac:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install ".[dev]"
```

### 4. Rodar o servidor de desenvolvimento

```bash
python run.py
```

Acesse:

```text
http://localhost:5000
```

---

## 🧊 Gerar Site Estático

Para gerar a versão estática do site:

```bash
python freeze.py
```

Os arquivos serão gerados em:

```text
build/
```

Para visualizar o build localmente:

```bash
python freeze.py serve
```

Acesse:

```text
http://localhost:8080
```

---

## 🧪 Testes

Para executar os testes:

```bash
pytest
```

Exemplo de resultado esperado:

```text
35 passed
```

Cobertura dos testes:

* Status HTTP das rotas
* Renderização dos serviços e depoimentos
* Presença do link WhatsApp com número correto
* Validação de arquivos estáticos como CSS, JS e SVG
* Configurações e dados da empresa
* App factory e blueprints Flask
* Integridade dos dados utilizados na página

---

## 📦 Deploy

O comando abaixo gera a pasta `build/` com HTML, CSS, JS e imagens prontos para publicação:

```bash
python freeze.py
```

O projeto pode ser publicado em:

| Plataforma           | Configuração                                                   |
| -------------------- | -------------------------------------------------------------- |
| **GitHub Pages**     | Publicação dos arquivos estáticos gerados em `build/`          |
| **Netlify**          | Build command: `python freeze.py` / Publish directory: `build` |
| **Vercel**           | Output directory: `build`                                      |
| **Cloudflare Pages** | Build command: `python freeze.py` / Output directory: `build`  |

---

## 🧠 Decisões Técnicas

* **Flask** foi usado para estruturar o projeto com rotas, app factory e templates Jinja2.
* **Frozen-Flask** foi usado para transformar a aplicação Flask em um site estático.
* O projeto não utiliza banco de dados, autenticação ou painel administrativo, pois a proposta é um site institucional simples.
* Os dados da empresa foram centralizados em `src/config.py` para facilitar manutenção.
* O deploy estático reduz custo, complexidade e necessidade de infraestrutura.
* Os testes foram adicionados para validar rotas, configuração e renderização dos principais elementos da página.
