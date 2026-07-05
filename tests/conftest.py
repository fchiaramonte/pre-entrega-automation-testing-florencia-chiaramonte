# conftest.py

import sys
import os
import json
import pytest
from datetime import datetime
from utils.driver_setup import get_driver
from utils.helpers import hacer_login, esperar_inventario
from utils.logger import get_logger

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

logger = get_logger(__name__)

@pytest.fixture(scope="function")
def driver():
    """Inicializa el WebDriver y lo cierra al finalizar el test."""
    logger.info("Iniciando WebDriver")
    driver = get_driver(headless=True)
    yield driver
    logger.info("Cerrando WebDriver")
    driver.quit()


@pytest.fixture(scope="function")
def driver_logueado(driver):
    """Retorna un WebDriver ya autenticado en SauceDemo."""
    logger.info("Ejecutando login previo al test")
    hacer_login(driver)
    esperar_inventario(driver)
    yield driver

@pytest.fixture(scope="session")
def test_data():
    """
    Carga y retorna los datos de prueba desde data/test_data.json.
    Scope session: se carga una sola vez para todos los tests.
    """
    ruta = os.path.join(os.path.dirname(__file__), "data", "test_data.json")
    logger.info(f"Cargando datos de prueba desde: {ruta}")
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook que captura un screenshot automáticamente cuando un test falla.
    El archivo se guarda en reports/screenshots/ con nombre descriptivo.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("driver_logueado")

        if driver:
            carpeta = os.path.join("reports", "screenshots")
            os.makedirs(carpeta, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_test = item.name.replace(" ", "_")
            nombre_archivo = f"{timestamp}_{nombre_test}.png"
            ruta_screenshot = os.path.join(carpeta, nombre_archivo)

            driver.save_screenshot(ruta_screenshot)
            logger.warning(f"Test fallido. Screenshot guardado en: {ruta_screenshot}")