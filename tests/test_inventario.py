import pytest
from selenium.webdriver.common.by import By
from utils.helpers import (
    obtener_titulo_seccion,
    obtener_productos,
    obtener_nombre_primer_producto,
    obtener_precio_primer_producto,
)


class TestInventario:

    @pytest.mark.smoke
    def test_titulo_seccion_es_products(self, driver_logueado):
        assert obtener_titulo_seccion(driver_logueado) == "Products"

    @pytest.mark.smoke
    def test_existen_productos_en_inventario(self, driver_logueado):
        assert len(obtener_productos(driver_logueado)) > 0

    def test_inventario_tiene_exactamente_seis_productos(self, driver_logueado):
        assert len(obtener_productos(driver_logueado)) == 6

    def test_primer_producto_tiene_nombre(self, driver_logueado):
        assert obtener_nombre_primer_producto(driver_logueado) != ""

    def test_primer_producto_tiene_precio(self, driver_logueado):
        precio = obtener_precio_primer_producto(driver_logueado)
        assert precio != ""
        assert "$" in precio

    @pytest.mark.smoke
    def test_menu_hamburguesa_esta_presente(self, driver_logueado):
        menu = driver_logueado.find_element(By.ID, "react-burger-menu-btn")
        assert menu.is_displayed()

    def test_icono_carrito_esta_presente(self, driver_logueado):
        carrito = driver_logueado.find_element(By.CLASS_NAME, "shopping_cart_link")
        assert carrito.is_displayed()

    def test_filtro_de_productos_esta_presente(self, driver_logueado):
        filtro = driver_logueado.find_element(
            By.CSS_SELECTOR, "select.product_sort_container"
        )
        assert filtro.is_displayed()

    @pytest.mark.parametrize("producto_esperado", [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
    ])
    def test_productos_conocidos_estan_listados(self, driver_logueado, producto_esperado):
        nombres = [
            e.text for e in driver_logueado.find_elements(By.CLASS_NAME, "inventory_item_name")
        ]
        assert producto_esperado in nombres