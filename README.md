# ❄️ Ale Ar-Condicionado — Site Institucional

> Site institucional de divulgação para empresa de ar-condicionado, desenvolvido com **Flask + Frozen-Flask** gerando um site 100% estático pronto para deploy em qualquer CDN ou hospedagem estática.

## 🖥️ Preview

![Preview do site](docs/assets/preview.gif)

| Seção | Descrição |
|---|---|
| **Hero** | Chamada principal com CTA direto para WhatsApp |
| **Serviços** | Cards com os 6 principais serviços oferecidos |
| **Sobre** | Estatísticas da empresa e diferenciais |
| **Depoimentos** | Avaliações de clientes reais |
| **Contato** | CTA final + botão flutuante do WhatsApp |

---

## 🛠️ Tecnologias

- **Python 3.14** — linguagem principal
- **Flask 3** — framework web / motor de templates (Jinja2)
- **Frozen-Flask** — geração de site estático (`build/`)
- **pytest + pytest-flask** — testes automatizados (35 testes)
- **HTML5 / CSS3 / JavaScript** — sem dependência de frameworks front-end
- **Google Fonts (Inter)** — tipografia
- **WhatsApp API** — link direto `wa.me` para contato

---

## 📁 Estrutura do Projeto

```
.
├── run.py              # Servidor de desenvolvimento
├── freeze.py           # Geração do site estático
├── pyproject.toml      # Dependências e configuração do projeto
├── .github/
│   └── workflows/
│       └── deploy.yml  # CI/CD GitHub Actions
├── tests/
│   ├── conftest.py
│   ├── test_config.py
│   └── test_routes.py
└── src/
    ├── __init__.py     # App factory Flask
    ├── config.py       # ⚙️ Configurações e dados da empresa
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

Todos os dados da empresa ficam centralizados em **`src/config.py`**.  
Alterar uma vez reflete em todo o site automaticamente:

```python
COMPANY = {
    "name":        "Ale Ar-condicionado",
    "tagline":     "Especialistas em climatização em São Paulo e Grande SP.",
    "city":        "São Paulo",
    "region":      "Grande SP",
    "phone":       "(11) 96105-6924",
    "whatsapp":    "5511961056924",   # DDI + DDD + número (só dígitos)
    "email":       "contato@alearcondicionado.com.br",
    "hours":       "Seg – Sab: 08h às 18h",
    "founded":     "2014",
    "clients":     "5.000+",
    "experience":  "10+",
    "satisfaction":"98%",
    "response":    "15min",
}
```

---

## 🚀 Como Rodar

### 1. Clonar e instalar dependências

```bash
git clone https://github.com/seu-usuario/ale-arcondicionado.git
cd ale-arcondicionado

python -m venv .venv
source .venv/bin/activate      # Linux/Mac
.venv\Scripts\activate         # Windows

pip install ".[dev]"
```

### 2. Servidor de desenvolvimento

```bash
python run.py
# Acesse: http://localhost:5000
```

### 3. Gerar site estático

```bash
python freeze.py
# Arquivos gerados em build/
```

### 4. Visualizar o build localmente

```bash
python freeze.py serve
# Acesse: http://localhost:8080
```

---

## 🧪 Testes

```bash
pytest
```

```
35 passed in 0.17s
```

Cobertura dos testes:

- ✅ Status HTTP das rotas
- ✅ Renderização de todos os serviços e depoimentos
- ✅ Presença do link WhatsApp com número correto
- ✅ Arquivos estáticos (CSS, JS, SVG)
- ✅ Configurações e dados da empresa
- ✅ App factory e blueprints Flask
- ✅ Integridade dos dados (estrelas, campos obrigatórios, formato do WhatsApp)

---

## 📦 Deploy

O comando `python freeze.py` gera a pasta `build/` com HTML, CSS, JS e imagens prontos.  
Pode ser publicado diretamente em:

| Plataforma | Como fazer |
|---|---|
| **GitHub Pages** | Push da pasta `build/` para branch `gh-pages` |
| **Netlify** | Drop da pasta `build/` na interface ou via CLI |
| **Vercel** | `vercel --prod` apontando para `build/` |
| **Cloudflare Pages** | Conectar repositório, build command: `python freeze.py`, output: `build` |

---

## 📄 Licença

Este projeto foi desenvolvido como portfólio. Sinta-se livre para usar como base para projetos similares.
