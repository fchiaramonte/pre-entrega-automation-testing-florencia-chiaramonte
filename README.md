# Pre-Entrega Automation Testing — SauceDemo

Proyecto de pre-entrega del curso **Automation Testing (Talento Tech)**.  
Automatiza los flujos principales de [saucedemo.com](https://www.saucedemo.com) usando **Selenium WebDriver**, **Pytest** y **Python**.

---

## Propósito del proyecto

Desarrollar flujos básicos automatizados que haga navegación web aplicando los conocimientos vistos hasta la clase #8:

- **Login**: verificar que un usuario válido accede al inventario y que credenciales inválidas muestran error.
- **Inventario**: validar el título de sección, la cantidad y los datos de los productos.
- **Carrito**: agregar un producto, verificar el badge y confirmar el ítem dentro del carrito.

---

## Tecnologías utilizadas

| Herramienta | Versión mínima | Uso |
|---|---|---|
| Python | 3.10+ | Lenguaje principal |
| Selenium | 4.x | Automatización del navegador |
| Pytest | 7.x | Framework de testing |
| pytest-html | 4.x | Generación de reportes HTML |
| ChromeDriver | (automático con Selenium 4) | Driver del navegador |
| Git / GitHub | — | Control de versiones |

---

## Estructura del proyecto

pre-entrega-automation-testing/
│
├── tests/
│   ├── conftest.py          # Fixtures globales (driver, driver_logueado)
│   ├── test_login.py        # Tests de autenticación
│   ├── test_inventario.py   # Tests de catálogo
│   └── test_carrito.py      # Tests de carrito
│
├── utils/
│   ├── driver_setup.py      # Configuración del WebDriver
│   └── helpers.py           # Funciones auxiliares reutilizables
│
├── reports/                 # Reportes HTML generados por Pytest
├── conftest.py              # Configuración de path para módulos
├── pytest.ini               # Markers personalizados
├── requirements.txt         # Dependencias
└── README.md                # Este archivo

---

## Casos de prueba cubiertos

### test_login.py — Autenticación
| Test | Tipo | Descripción |
|---|---|---|
| test_login_exitoso_redirige_a_inventario | smoke | URL contiene /inventory.html |
| test_login_exitoso_muestra_titulo_swag_labs | smoke | Título de pestaña es Swag Labs |
| test_login_exitoso_muestra_seccion_products | smoke | Encabezado es Products |
| test_login_con_usuario_invalido_muestra_error | exception | Credenciales incorrectas muestran error |
| test_login_con_campos_vacios_muestra_error | exception | Campos vacíos muestran error |
| test_login_invalido_parametrizado | exception | 3 combinaciones inválidas parametrizadas |

### test_inventario.py — Catálogo
| Test | Tipo | Descripción |
|---|---|---|
| test_titulo_seccion_es_products | smoke | Título exacto de la sección |
| test_existen_productos_en_inventario | smoke | Al menos 1 producto visible |
| test_inventario_tiene_exactamente_seis_productos | — | Exactamente 6 productos |
| test_primer_producto_tiene_nombre | — | Nombre del primer producto no vacío |
| test_primer_producto_tiene_precio | — | Precio con formato $ |
| test_menu_hamburguesa_esta_presente | smoke | Botón de menú visible |
| test_icono_carrito_esta_presente | — | Ícono del carrito visible |
| test_filtro_de_productos_esta_presente | — | Selector de ordenamiento visible |
| test_productos_conocidos_estan_listados | — | 3 productos conocidos parametrizados |

### test_carrito.py — Carrito de compras
| Test | Tipo | Descripción |
|---|---|---|
| test_agregar_producto_incrementa_badge | smoke | Badge muestra 1 tras agregar |
| test_producto_aparece_en_carrito | smoke | Producto listado en el carrito |
| test_carrito_vacio_no_muestra_badge | — | Badge no visible con carrito vacío |
| test_url_carrito_es_correcta | — | URL contiene /cart.html |
| test_agregar_dos_productos_actualiza_badge | — | Badge >= 1 con múltiples productos |
| test_boton_checkout_presente_en_carrito | — | Botón Checkout visible |

---

## Sitio web objetivo

**[www.saucedemo.com](https://www.saucedemo.com)**  
Credenciales de prueba: `standard_user` / `secret_sauce`