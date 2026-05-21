import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import (
    agregar_primer_producto_al_carrito,
    obtener_contador_carrito,
    obtener_nombre_primer_producto,
    ir_al_carrito,
    obtener_items_en_carrito,
    TIMEOUT,
)


class TestCarrito:

    @pytest.mark.smoke
    def test_agregar_producto_incrementa_badge(self, driver_logueado):
        agregar_primer_producto_al_carrito(driver_logueado)
        assert obtener_contador_carrito(driver_logueado) == "1"

    @pytest.mark.smoke
    def test_producto_aparece_en_carrito(self, driver_logueado):
        nombre_producto = obtener_nombre_primer_producto(driver_logueado)
        agregar_primer_producto_al_carrito(driver_logueado)
        ir_al_carrito(driver_logueado)
        items = obtener_items_en_carrito(driver_logueado)
        assert len(items) > 0
        nombres_en_carrito = [
            item.find_element(By.CLASS_NAME, "inventory_item_name").text
            for item in items
        ]
        assert nombre_producto in nombres_en_carrito

    def test_carrito_vacio_no_muestra_badge(self, driver_logueado):
        badges = driver_logueado.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badges) == 0

    def test_url_carrito_es_correcta(self, driver_logueado):
        agregar_primer_producto_al_carrito(driver_logueado)
        ir_al_carrito(driver_logueado)
        WebDriverWait(driver_logueado, TIMEOUT).until(
            EC.url_contains("/cart.html")
        )
        assert "/cart.html" in driver_logueado.current_url

    def test_boton_checkout_presente_en_carrito(self, driver_logueado):
        agregar_primer_producto_al_carrito(driver_logueado)
        ir_al_carrito(driver_logueado)
        WebDriverWait(driver_logueado, TIMEOUT).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
        )
        boton_checkout = driver_logueado.find_element(By.ID, "checkout")
        assert boton_checkout.is_displayed()