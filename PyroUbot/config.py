import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "8116593707").split()))

API_ID = int(os.getenv("API_ID", "31165171"))

API_HASH = os.getenv("API_HASH", "7fcb663bf48d8f8e46b4e4b31fc6d69a")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8476343612:AAFX0R70-FQe7-h4fm3_xYqZGsUjoEXrgQQ")

OWNER_ID = int(os.getenv("OWNER_ID", "8116593707"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ibnumuzakim7:ibnumuzakim132@ibnumuzakim.sbwnig8.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4912568273"))
