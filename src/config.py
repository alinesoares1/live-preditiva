# Centraliza parâmetros que mudam com frequência.
from pathlib import Path

# caminhos
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DATASET_PATH = DATA_DIR / "dataset_engajamento_clientes.csv"

# configurações de datas
DATE_COLUMN = "data"
CLIENT_ID_COLUMN = "cliente_id"