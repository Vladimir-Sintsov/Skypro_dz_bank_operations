from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

CSV_PATH = BASE_DIR.joinpath("data/transactions.csv")
JSON_PATH = BASE_DIR.joinpath("data/operations.json")
XLSX_PATH = BASE_DIR.joinpath("data/transactions.xlsx")

LOG_MASKS_PATH = BASE_DIR.joinpath("logs/masks.log")
LOG_UTILS_PATH = BASE_DIR.joinpath("logs/utils.log")
