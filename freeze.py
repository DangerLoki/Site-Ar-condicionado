"""
Script para gerar o site estático usando Flask-Frozen.
"""
import sys
from pathlib import Path
from flask_frozen import Freezer
from src import create_app
from src.config import ProductionConfig

BASE_DIR = Path(__file__).resolve().parent


def _make_freezer():
    app = create_app(ProductionConfig)
    app.config["FREEZER_DESTINATION"] = str(BASE_DIR / "build")
    app.config["FREEZER_RELATIVE_URLS"] = True
    app.config["FREEZER_REMOVE_EXTRA_FILES"] = True
    return Freezer(app)


def main():
    """Entry point para `freeze` definido no pyproject.toml."""
    args = sys.argv[1:]
    if args and args[0] == "serve":
        import http.server, os
        os.chdir(BASE_DIR / "build")
        handler = http.server.SimpleHTTPRequestHandler
        with http.server.HTTPServer(("", 8080), handler) as httpd:
            print("Servindo build/ em http://localhost:8080  (Ctrl+C para parar)")
            httpd.serve_forever()
    else:
        _make_freezer().freeze()
        print("✅  Site estático gerado em build/")


if __name__ == "__main__":
    main()
