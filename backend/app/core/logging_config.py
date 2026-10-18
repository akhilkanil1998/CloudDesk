import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from app.core.config import settings

print("Logging configuration module loaded")
logger = logging.getLogger()

logger.setLevel(logging.INFO)

# current_date = datetime.now().strftime("%Y-%m-%d")


# max_file_size = 5 * 1024 * 1024 # 5MB

log_dir = Path(settings.LOG_DIR)

log_dir.mkdir(parents=True, exist_ok=True)


log_file = log_dir/"log.txt"

backup_file_count =3

handler = TimedRotatingFileHandler(
    filename=log_file, 
    # maxBytes= max_file_size,
    backupCount= backup_file_count,
    when="midnight", interval=1, 
    encoding="utf-8", utc=False
)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


logger.info("This is a test log")