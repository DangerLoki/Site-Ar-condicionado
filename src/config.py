class Config:
    SECRET_KEY = "Ale Ar-condicionado 2026"
    DEBUG = False
    FREEZER_DESTINATION = "../build"
    FREEZER_RELATIVE_URLS = True

    # -------------------------------------------------------
    # Dados da empresa — altere aqui para refletir em todo o site
    # -------------------------------------------------------
    COMPANY = {
        "name":        "Ale Ar-condicionado",          # Nome exibido no site
        "tagline":     "Especialistas em climatização em São Paulo e Grande SP.",
        "city":        "São Paulo",
        "region":      "Grande SP",
        "phone":       "(11) 96105-6924",
        "whatsapp":    "5511961056924",        # DDI + DDD + número (só dígitos)
        "email":       "contato@alearcondicionado.com.br",
        "hours":       "Seg – Sab: 08h às 18h",
        "founded":     "2014",
        "clients":     "5.000+",
        "experience":  "10+",
        "satisfaction":"98%",
        "response":    "15min",
    }


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

