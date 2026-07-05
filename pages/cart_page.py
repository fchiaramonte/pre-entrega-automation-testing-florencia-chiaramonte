# pages/cart_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger(__name__)


class CartPage:
    """
    Page Object Model para la página del carrito de SauceDemo.
    Encapsula todos los locators y acciones relacionadas al carrito.
    """

    URL = "https://www.saucedemo.com/cart.html"

    # Locators
    ITEMS_CARRITO = (By.CLASS_NAME, "cart_item")
    NOMBRES_ITEMS = (By.CLASS_NAME, "inventory_item_name")
    BOTON_CHECKOUT = (By.ID, "checkout")
    BOTON_CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def esperar_carga(self):
        """Espera a que el carrito esté visible."""
        logger.info("Esperando carga del carrito")
        self.wait.until(EC.url_contains("/cart.html"))

    def obtener_items(self) -> list:
        """Retorna la lista de elementos de productos en el carrito."""
        logger.debug("Obteniendo items del carrito")
        self.wait.until(EC.visibility_of_element_located(self.ITEMS_CARRITO))
        return self.driver.find_elements(*self.ITEMS_CARRITO)

    def obtener_nombres_items(self) -> list[str]:
        """Retorna una lista con los nombres de los productos en el carrito."""
        logger.debug("Obteniendo nombres de items en el carrito")
        items = self.obtener_items()
        return [
            item.find_element(*self.NOMBRES_ITEMS).text
            for item in items
        ]

    def url_es_correcta(self) -> bool:
        """Retorna True si la URL actual corresponde al carrito."""
        return "/cart.html" in self.driver.current_url

    def checkout_visible(self) -> bool:
        """Retorna True si el botón de checkout está visible."""
        logger.debug("Verificando visibilidad del botón checkout")
        self.wait.until(EC.visibility_of_element_located(self.ITEMS_CARRITO))
        boton = self.driver.find_element(*self.BOTON_CHECKOUT)
        return boton.is_displayed()

    def click_checkout(self):
        """Hace clic en el botón de checkout."""
        logger.info("Haciendo clic en checkout")
        self.driver.find_element(*self.BOTON_CHECKOUT).click()

    def click_continue_shopping(self):
        """Hace clic en el botón para continuar comprando."""
        logger.info("Haciendo clic en continuar comprando")
        self.driver.find_element(*self.BOTON_CONTINUE_SHOPPING).click()