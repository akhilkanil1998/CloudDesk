import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from app.core.config import settings

# Creates the logger instance
logger = logging.getLogger("CloudDesk")
# Sets the level. Now it is set as INFO
logger.setLevel(logging.INFO)
# Getting path from the env file
log_dir = Path(settings.LOG_DIR)
# Checks if the directory is present and creates dir if not.
log_dir.mkdir(parents=True, exist_ok=True)

# File name
log_file = log_dir/"log.txt"
# back up count
backup_file_count =3

handler = TimedRotatingFileHandler(
    filename=log_file, 
    backupCount= backup_file_count,
    when="midnight", interval=1, 
    encoding="utf-8", utc=False
)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
handler.setFormatter(formatter)

# Avoid adding duplicate handlers to this logger.
if not any(
    isinstance(existing, TimedRotatingFileHandler)
    and Path(existing.baseFilename) == log_file.resolve()
    for existing in logger.handlers
):
    logger.addHandler(handler)
else:
    handler.close()