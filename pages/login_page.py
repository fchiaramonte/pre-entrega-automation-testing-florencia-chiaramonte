# pages/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger(__name__)


class LoginPage:
    """
    Page Object Model para la página de login de SauceDemo.
    Encapsula todos los locators y acciones relacionadas al login.
    """

    URL = "https://www.saucedemo.com"

    # Locators
    INPUT_USUARIO = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BOTON_LOGIN = (By.ID, "login-button")
    ERROR_MENSAJE = (By.CLASS_NAME, "error-message-container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        """Navega a la URL de la página de login."""
        logger.info(f"Abriendo página de login: {self.URL}")
        self.driver.get(self.URL)

    def ingresar_usuario(self, username: str):
        """Escribe el nombre de usuario en el campo correspondiente."""
        logger.debug(f"Ingresando usuario: {username}")
        campo = self.wait.until(EC.visibility_of_element_located(self.INPUT_USUARIO))
        campo.clear()
        campo.send_keys(username)

    def ingresar_password(self, password: str):
        """Escribe la contraseña en el campo correspondiente."""
        logger.debug("Ingresando contraseña")
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys(password)

    def click_login(self):
        """Hace clic en el botón de login."""
        logger.info("Haciendo clic en el botón de login")
        self.driver.find_element(*self.BOTON_LOGIN).click()

    def login(self, username: str, password: str):
        """
        Flujo completo de login: abre la página, ingresa credenciales y confirma.

        Args:
            username: Nombre de usuario.
            password: Contraseña.
        """
        self.abrir()
        self.ingresar_usuario(username)
        self.ingresar_password(password)
        self.click_login()
        logger.info("Login ejecutado")

    def obtener_mensaje_error(self) -> str:
        """Retorna el texto del mensaje de error si está visible."""
        logger.debug("Obteniendo mensaje de error")
        mensaje = self.wait.until(EC.visibility_of_element_located(self.ERROR_MENSAJE))
        return mensaje.text

    def error_esta_visible(self) -> bool:
        """Retorna True si el mensaje de error está visible en pantalla."""
        try:
            elemento = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MENSAJE)
            )
            return elemento.is_displayed()
        except Exception:
            return False