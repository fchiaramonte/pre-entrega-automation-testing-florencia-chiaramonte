from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"
VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"
TIMEOUT = 10


def hacer_login(driver, username=VALID_USER, password=VALID_PASSWORD):
    driver.get(BASE_URL)
    campo_usuario = WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    campo_usuario.clear()
    campo_usuario.send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def esperar_inventario(driver):
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )


def obtener_titulo_seccion(driver):
    return driver.find_element(
        By.CSS_SELECTOR, "div.header_secondary_container .title"
    ).text


def obtener_productos(driver):
    return driver.find_elements(By.CLASS_NAME, "inventory_item")


def obtener_nombre_primer_producto(driver):
    nombres = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    return nombres[0].text if nombres else ""


def obtener_precio_primer_producto(driver):
    precios = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    return precios[0].text if precios else ""


def agregar_primer_producto_al_carrito(driver):
    boton = driver.find_element(
        By.XPATH, "(//button[contains(@data-test, 'add-to-cart')])[1]"
    )
    boton.click()


def obtener_contador_carrito(driver):
    badge = WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    return badge.text


def ir_al_carrito(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


def obtener_items_en_carrito(driver):
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    return driver.find_elements(By.CLASS_NAME, "cart_item")