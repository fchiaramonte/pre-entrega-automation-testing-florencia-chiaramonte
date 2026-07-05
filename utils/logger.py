# utils/logger.py

import logging
import os
from datetime import datetime


def get_logger(nombre: str = "automation") -> logging.Logger:
    """
    Crea y retorna un logger configurado con salida a consola y archivo.

    Args:
        nombre: Nombre del logger (generalmente el nombre del módulo).

    Returns:
        Una instancia de Logger lista para usar.
    """
    logger = logging.getLogger(nombre)

    # Evita agregar handlers duplicados si el logger ya fue creado
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # Formato del mensaje de log
    formato = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Handler de consola
    handler_consola = logging.StreamHandler()
    handler_consola.setLevel(logging.INFO)
    handler_consola.setFormatter(formato)

    # Handler de archivo (guarda en logs/automation.log)
    os.makedirs("logs", exist_ok=True)
    nombre_archivo = f"logs/automation_{datetime.now().strftime('%Y%m%d')}.log"
    handler_archivo = logging.FileHandler(nombre_archivo, encoding="utf-8")
    handler_archivo.setLevel(logging.DEBUG)
    handler_archivo.setFormatter(formato)

    logger.addHandler(handler_consola)
    logger.addHandler(handler_archivo)

    return logger