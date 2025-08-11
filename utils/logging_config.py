import logging
from params.paths import LOGS_DIR

def configurar_logger_planea(nombre: str, archivo_log="workflow.log") -> logging.Logger:
    # Crear carpetas necesarias: logs y logs/planea
    log_dir_planea = LOGS_DIR / "planea"
    log_dir_planea.mkdir(parents=True, exist_ok=True)

    log_path = log_dir_planea / archivo_log

    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger

def configurar_logger_excale(nombre: str, archivo_log="workflow.log") -> logging.Logger:
    # Crear carpetas necesarias: logs y logs/excale
    log_dir_planea = LOGS_DIR / "excale"
    log_dir_planea.mkdir(parents=True, exist_ok=True)

    log_path = log_dir_planea / archivo_log

    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger
