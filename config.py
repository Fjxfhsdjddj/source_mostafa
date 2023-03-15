from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/6abaa2db3ae5ebae362f8.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/6abaa2db3ae5ebae362f8.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tanyathanwy2023")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "@MARCO_R6")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5328713035").split()))


FAILED = "https://graph.org/file/6abaa2db3ae5ebae362f8.jpg"
