"""
Gera o site estático na pasta build/.
"""
import sys
from pathlib import Path
from flask_frozen import Freezer
from src import create_app
from src.config import ProductionConfig

BASE_DIR = Path(__file__).resolve().parent

app = create_app(ProductionConfig)
app.config["FREEZER_DESTINATION"] = str(BASE_DIR / "build")
app.config["FREEZER_RELATIVE_URLS"] = True
app.config["FREEZER_REMOVE_EXTRA_FILES"] = True

freezer = Freezer(app)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "serve":
        # Serve o site gerado localmente
        import http.server
        import os

        os.chdir(BASE_DIR / "build")
        handler = http.server.SimpleHTTPRequestHandler
        with http.server.HTTPServer(("", 8080), handler) as httpd:
            print("Servindo build/ em http://localhost:8080  (Ctrl+C para parar)")
            httpd.serve_forever()
    else:
        freezer.freeze()
        print("✅  Site estático gerado em build/")
