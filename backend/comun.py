import logging
from .config import NIVEL_LOG

# Configuración de logs
logger = logging.getLogger("uvicorn")
log_lvl = getattr(logging, NIVEL_LOG)
logging.basicConfig(level=log_lvl)
