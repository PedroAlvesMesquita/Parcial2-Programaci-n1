
import logging
from pathlib import Path

LOG_FILE = "registro.log"

def setup_logger():
    # Crea carpeta si no existe (aquí mismo)
    Path(LOG_FILE).parent.mkdir(exist_ok=True)
    logger = logging.getLogger("gestor_pedidos")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(LOG_FILE, encoding="utf-8")
        fmt = logging.Formatter("%(asctime)s – %(levelname)s – %(message)s")
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    return logger

# Exponemos el logger
logger = setup_logger()
