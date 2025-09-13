# calculator-pytest

python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
pytest -v

Rodando por marcador:

Básicas: pytest -m operacoes_basicas -v

Extras: pytest -m extras -v

Exceções: pytest -m excecoes -v

Smoke: pytest -m smoke -q