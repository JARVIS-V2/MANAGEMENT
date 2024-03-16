import os

# Token from botfather
TOKEN = os.environ.get("TOKEN", "")  # Get from BotFather

# Make a new group then add  then send /id and fill id here.
JOIN_LOGGER = os.environ.get("JOIN_LOGGER", "-1002044893623")  # Fill with the group ID after adding @ScenarioXbot and sending /id

# Bot owner's ID and username
OWNER_ID = int(os.environ.get("OWNER_ID", "7157587567"))  # Fill with your Telegram user ID
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "JARVIS_V2")  # Fill with your Telegram username

# Lists of user IDs for different roles
DRAGONS = {int(x) for x in os.environ.get("DRAGONS", "").split()}  # Fill with user IDs for the 'DRAGONS' role
DEV_USERS = {int(x) for x in os.environ.get("DEV_USERS", "").split()}  # Fill with user IDs for the 'DEV_USERS' role
DEMONS = {int(x) for x in os.environ.get("DEMONS", "").split()}  # Fill with user IDs for the 'DEMONS' role
WOLVES = {int(x) for x in os.environ.get("WOLVES", "").split()}  # Fill with user IDs for the 'WOLVES' role
TIGERS = {int(x) for x in os.environ.get("TIGERS", "").split()}  # Fill with user IDs for the 'TIGERS' role

# Should profile pic of user be shown in /info command?
INFOPIC = bool(os.environ.get("INFOPIC", True))

# Group where event logs are sent
EVENT_LOGS = os.environ.get("EVENT_LOGS", None)  # Fill with the group ID for event logs

# Group where error logs are sent
ERROR_LOGS = os.environ.get("ERROR_LOGS", None)  # Fill with the group ID for error logs

# Whether the bot uses webhook or not
WEBHOOK = bool(os.environ.get("WEBHOOK", False))

# Heroku app details
URL = os.environ.get("URL", "")  # Heroku app URL
PORT = int(os.environ.get("PORT", 8443))  # Heroku app port
CERT_PATH = os.environ.get("CERT_PATH")  # Path to SSL certificate (if applicable)

# Bot owner's API credentials
API_ID = os.environ.get("API_ID", "")  # Get from https://my.telegram.org/apps
API_HASH = os.environ.get("API_HASH", "")  # Get from https://my.telegram.org/apps

# Database URL
DB_URL = os.environ.get("DATABASE_URL", "")  # Database connection URL

# Donation link
DONATION_LINK = os.environ.get("DONATION_LINK", "")  # Your donation link

# APIs and keys
WALL_API = os.environ.get("WALL_API", None)  # Get from https://wall.alphacoders.com/api.php
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", "")  # Get from https://www.remove.bg/
OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", "")  # Get from https://openweathermap.org/api
GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None)  # Get from http://genius.com/api-clients
MONGO_DB_URL = os.environ.get("MONGO_DB_URL", "")  # Your MongoDB URL
REDIS_URL = os.environ.get("REDIS_URL", "")  # Your Redis URL
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", "")  # Your YouTube API key
SPAMWATCH_API = os.environ.get("SPAMWATCH_API", "")  # Get from https://t.me/SpamWatchBot

# Bot details
BOT_ID = int(os.environ.get("BOT_ID", None))  # Your bot's Telegram ID
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "")  # Your support chat group link
SPAMWATCH_SUPPORT_CHAT = os.environ.get("https://t.me/+9OC6BH29oo9kMDU1", "")  # Your SpamWatch support chat link
BOT_USERNAME = os.environ.get("BOT_USERNAME", "")  # Your bot's username

# Miscellaneous
STRING_SESSION = os.environ.get("STRING_SESSION", None)  # Telethon Based String Session
REPO = EMON"doraemon890/JARVIS-X-MANAGER"  # GitHub repository
DEVELOPER = "JARVIS"  # Your developer/team name
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "")  # Your Heroku app name
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")  # Your Heroku API key
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "")  # Your upstream branch
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "")  # Your upstream repository
ALLOW_CHATS = os.environ.get("ALLOW_CHATS", "")  # Allow chats
BOT_NAME = os.environ.get("BOT_NAME", "")  # Your bot's name
MONGO_DB = "jarvisxd45"  # MongoDB database name
ARQ_API_URL = "https://arq.hamker.in"  # ARQ API URL
GOOGLE_CHROME_BIN = "/usr/bin/google-chrome"  # Path to Google Chrome binary
CHROME_DRIVER = "/usr/bin/chromedriver"  # Path to ChromeDriver
SUDO_USERS = "7059759820"  # Superuser IDs
WHITELIST_USERS = "7059759820"  # Whitelisted user IDs
BOT_API_URL = os.environ.get('BOT_API_URL', "https://api.telegram.org/bot")  # Bot API URL
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "JARVIS_X_SUPPORT")  # Your updates channel

# Images
HELP_IMG = os.environ.get("HELP_IMG", "")  # Help image URL
GROUP_START_IMG = os.environ.get("GROUP_START_IMG", "")  # Group start image URL
JARVISHUB_PIC = os.environ.get("JARVISHUB_PIC", "")  # JARVIS image URL

# Configuration settings
BL_CHATS = {int(x) for x in os.environ.get("BL_CHATS", "").split()}  # Blacklisted chat IDs
LOAD = os.environ.get("LOAD", "").split()  # Modules to load
NO_LOAD = os.environ.get("NO_LOAD", "translation").split()  # Modules not to load
DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))  # Whether to delete commands after execution
STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", True))  # Whether to strictly ban users
WORKERS = int(os.environ.get("WORKERS", 8))  # Number of worker threads
BAN_STICKER = os.environ.get("BAN_STICKER", "")  # Sticker ID for ban messages
ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)  # Allow exclamations in commands
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")  # Temporary download directory
CASH_API_KEY = os.environ.get("CASH_API_KEY", "70F3DVSKF6RUAHQV")  # CASH API key
TIME_API_KEY = os.environ.get("TIME_API_KEY", "K5PTMFOEC82M")  # TIME API key
