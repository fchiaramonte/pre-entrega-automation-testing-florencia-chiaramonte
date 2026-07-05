# pages/inventory_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger(__name__)


class InventoryPage:
    """
    Page Object Model para la página de inventario de SauceDemo.
    Encapsula todos los locators y acciones relacionadas al inventario.
    """

    URL = "https://www.saucedemo.com/inventory.html"

    # Locators
    TITULO_SECCION = (By.CSS_SELECTOR, "div.header_secondary_container .title")
    PRODUCTOS = (By.CLASS_NAME, "inventory_item")
    NOMBRES_PRODUCTOS = (By.CLASS_NAME, "inventory_item_name")
    PRECIOS_PRODUCTOS = (By.CLASS_NAME, "inventory_item_price")
    BOTONES_ADD_TO_CART = (By.XPATH, "//button[contains(@data-test, 'add-to-cart')]")
    BADGE_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
    LINK_CARRITO = (By.CLASS_NAME, "shopping_cart_link")
    MENU_HAMBURGUESA = (By.ID, "react-burger-menu-btn")
    FILTRO_PRODUCTOS = (By.CSS_SELECTOR, "select.product_sort_container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo_seccion(self) -> str:
        """Retorna el texto del título de la sección (ej: 'Products')."""
        logger.debug("Obteniendo título de sección")
        return self.driver.find_element(*self.TITULO_SECCION).text

    def obtener_productos(self) -> list:
        """Retorna la lista de elementos de productos visibles en el inventario."""
        logger.debug("Obteniendo lista de productos")
        return self.driver.find_elements(*self.PRODUCTOS)

    def obtener_nombres_productos(self) -> list[str]:
        """Retorna una lista con los nombres de todos los productos."""
        logger.debug("Obteniendo nombres de productos")
        elementos = self.driver.find_elements(*self.NOMBRES_PRODUCTOS)
        return [e.text for e in elementos]

    def obtener_nombre_primer_producto(self) -> str:
        """Retorna el nombre del primer producto de la lista."""
        nombres = self.driver.find_elements(*self.NOMBRES_PRODUCTOS)
        return nombres[0].text if nombres else ""

    def obtener_precio_primer_producto(self) -> str:
        """Retorna el precio del primer producto de la lista."""
        precios = self.driver.find_elements(*self.PRECIOS_PRODUCTOS)
        return precios[0].text if precios else ""

    def agregar_primer_producto_al_carrito(self):
        """Hace clic en el botón 'Add to cart' del primer producto."""
        logger.info("Agregando primer producto al carrito")
        boton = self.driver.find_element(*self.BOTONES_ADD_TO_CART)
        boton.click()

    def obtener_contador_carrito(self) -> str:
        """Retorna el número que muestra el badge del carrito."""
        logger.debug("Obteniendo contador del carrito")
        badge = self.wait.until(EC.visibility_of_element_located(self.BADGE_CARRITO))
        return badge.text

    def badge_carrito_visible(self) -> bool:
        """Retorna True si el badge del carrito está visible."""
        badges = self.driver.find_elements(*self.BADGE_CARRITO)
        return len(badges) > 0

    def ir_al_carrito(self):
        """Hace clic en el ícono del carrito."""
        logger.info("Navegando al carrito")
        self.driver.find_element(*self.LINK_CARRITO).click()

    def menu_hamburguesa_visible(self) -> bool:
        """Retorna True si el menú hamburguesa está visible."""
        return self.driver.find_element(*self.MENU_HAMBURGUESA).is_displayed()

    def icono_carrito_visible(self) -> bool:
        """Retorna True si el ícono del carrito está visible."""
        return self.driver.find_element(*self.LINK_CARRITO).is_displayed()

    def filtro_visible(self) -> bool:
        """Retorna True si el filtro de productos está visible."""
        return self.driver.find_element(*self.FILTRO_PRODUCTOS).is_displayed()