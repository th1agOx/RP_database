import os 
import logging
from logging.handlers import RotatingFileHandler 

def setup_logger(name, log_file, level=logging.INFO) :
    formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')

    log_path = f"logs/{log_file}"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    try:
        file_handler = RotatingFileHandler(log_path, maxBytes=1_000_000, backupCount=3)
        file_handler.setFormatter(formatter)

    except Exception as e :
        print(f"[FALHA AO CRIAR FILE HANDLER] {e}")
        file_handler = None

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter) 

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.hasHandlers():
            if file_handler:
                logger.addHandler(file_handler)

            logger.addHandler(stream_handler)

    return logger

payload_logger = setup_logger("PayLoad_log", "requests.log")
send_status_db_logger = setup_logger("Status_database_log", "Status_db.log")
orm_errors_logger = setup_logger("orm_error_logger", "orm_errors.log", level=logging.ERROR)
commit_logger = setup_logger("Commit_Logger", "commits.log")