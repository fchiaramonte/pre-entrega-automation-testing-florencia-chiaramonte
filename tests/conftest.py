import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from utils.driver_setup import get_driver
from utils.helpers import hacer_login, esperar_inventario


@pytest.fixture(scope="function")
def driver():
    driver = get_driver(headless=True)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver_logueado(driver):
    hacer_login(driver)
    esperar_inventario(driver)
    yield driver