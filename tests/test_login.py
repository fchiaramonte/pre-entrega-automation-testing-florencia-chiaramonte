import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import hacer_login, esperar_inventario, TIMEOUT


class TestLogin:

    @pytest.mark.smoke
    def test_login_exitoso_redirige_a_inventario(self, driver):
        hacer_login(driver)
        esperar_inventario(driver)
        assert "/inventory.html" in driver.current_url

    @pytest.mark.smoke
    def test_login_exitoso_muestra_titulo_swag_labs(self, driver):
        hacer_login(driver)
        esperar_inventario(driver)
        assert driver.title == "Swag Labs"

    @pytest.mark.smoke
    def test_login_exitoso_muestra_seccion_products(self, driver):
        hacer_login(driver)
        esperar_inventario(driver)
        titulo = driver.find_element(
            By.CSS_SELECTOR, "div.header_secondary_container .title"
        ).text
        assert titulo == "Products"

    @pytest.mark.exception
    def test_login_con_usuario_invalido_muestra_error(self, driver):
        hacer_login(driver, username="usuario_invalido", password="clave_incorrecta")
        mensaje_error = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
        )
        assert mensaje_error.is_displayed()
        assert "Epic sadface" in mensaje_error.text

    @pytest.mark.exception
    def test_login_con_campos_vacios_muestra_error(self, driver):
        hacer_login(driver, username="", password="")
        mensaje_error = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
        )
        assert mensaje_error.is_displayed()

    @pytest.mark.parametrize("username, password", [
        ("locked_out_user", "secret_sauce"),
        ("usuario_falso", "clave_falsa"),
        ("", "secret_sauce"),
    ])
    @pytest.mark.exception
    def test_login_invalido_parametrizado(self, driver, username, password):
        hacer_login(driver, username=username, password=password)
        mensaje_error = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
        )
        assert mensaje_error.is_displayed()