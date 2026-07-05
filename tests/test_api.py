# tests/test_api.py

import pytest
import requests
from utils.logger import get_logger

logger = get_logger(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"


class TestAPI:
    """
    Pruebas de API sobre JSONPlaceholder.
    Cubre métodos GET, POST y DELETE con validación de
    códigos de estado, estructura y contenido de respuestas.
    """

    @pytest.mark.smoke
    def test_get_lista_posts_retorna_200(self):
        """Verifica que el endpoint de posts retorna status 200."""
        logger.info("GET /posts - verificando status 200")
        response = requests.get(f"{BASE_URL}/posts")

        assert response.status_code == 200
        logger.info(f"Status recibido: {response.status_code}")

    def test_get_lista_posts_retorna_lista_no_vacia(self):
        """Verifica que la respuesta de posts es una lista con elementos."""
        logger.info("GET /posts - verificando que la lista no esté vacía")
        response = requests.get(f"{BASE_URL}/posts")
        data = response.json()

        assert isinstance(data, list)
        assert len(data) > 0
        logger.info(f"Cantidad de posts recibidos: {len(data)}")

    def test_get_post_individual_retorna_200(self):
        """Verifica que se puede obtener un post específico por ID."""
        logger.info("GET /posts/1 - verificando status 200")
        response = requests.get(f"{BASE_URL}/posts/1")

        assert response.status_code == 200

    def test_get_post_individual_tiene_campos_requeridos(self):
        """Verifica que un post individual contiene los campos esperados."""
        logger.info("GET /posts/1 - verificando estructura del JSON")
        response = requests.get(f"{BASE_URL}/posts/1")
        data = response.json()

        assert "id" in data
        assert "title" in data
        assert "body" in data
        assert "userId" in data
        logger.info(f"Campos del post: {list(data.keys())}")

    def test_get_post_inexistente_retorna_404(self):
        """Verifica que un post con ID inválido retorna status 404."""
        logger.info("GET /posts/99999 - verificando status 404")
        response = requests.get(f"{BASE_URL}/posts/99999")

        assert response.status_code == 404
        logger.info(f"Status recibido: {response.status_code}")

    @pytest.mark.parametrize("post_id", [1, 2, 3, 5, 10])
    def test_get_posts_parametrizados_retornan_200(self, post_id):
        """Verifica que múltiples posts individuales retornan status 200."""
        logger.info(f"GET /posts/{post_id} - verificando status 200")
        response = requests.get(f"{BASE_URL}/posts/{post_id}")

        assert response.status_code == 200
        assert response.json()["id"] == post_id

    @pytest.mark.smoke
    def test_post_crear_recurso_retorna_201(self):
        """Verifica que crear un nuevo post retorna status 201."""
        nuevo_post = {
            "title": "Post de prueba",
            "body": "Contenido del post de prueba",
            "userId": 1
        }
        logger.info("POST /posts - creando nuevo recurso")
        response = requests.post(f"{BASE_URL}/posts", json=nuevo_post)

        assert response.status_code == 201
        logger.info(f"Status recibido: {response.status_code}")

    def test_post_crear_recurso_retorna_id(self):
        """Verifica que el recurso creado tiene un ID asignado en la respuesta."""
        nuevo_post = {
            "title": "Post de prueba",
            "body": "Contenido del post de prueba",
            "userId": 1
        }
        logger.info("POST /posts - verificando que la respuesta incluye un ID")
        response = requests.post(f"{BASE_URL}/posts", json=nuevo_post)
        data = response.json()

        assert "id" in data
        assert data["id"] is not None
        logger.info(f"ID asignado al nuevo recurso: {data['id']}")

    def test_post_crear_recurso_refleja_datos_enviados(self):
        """Verifica que la respuesta contiene los mismos datos enviados."""
        nuevo_post = {
            "title": "Título de prueba",
            "body": "Cuerpo de prueba",
            "userId": 1
        }
        logger.info("POST /posts - verificando que los datos enviados se reflejan en la respuesta")
        response = requests.post(f"{BASE_URL}/posts", json=nuevo_post)
        data = response.json()

        assert data["title"] == nuevo_post["title"]
        assert data["body"] == nuevo_post["body"]
        assert data["userId"] == nuevo_post["userId"]

    @pytest.mark.smoke
    def test_delete_recurso_retorna_200(self):
        """Verifica que eliminar un post existente retorna status 200."""
        logger.info("DELETE /posts/1 - verificando status 200")
        response = requests.delete(f"{BASE_URL}/posts/1")

        assert response.status_code == 200
        logger.info(f"Status recibido: {response.status_code}")

    def test_delete_recurso_retorna_cuerpo_vacio(self):
        """Verifica que la respuesta del DELETE es un objeto vacío."""
        logger.info("DELETE /posts/1 - verificando cuerpo de respuesta vacío")
        response = requests.delete(f"{BASE_URL}/posts/1")
        data = response.json()

        assert data == {}
        logger.info("Cuerpo de respuesta vacío confirmado")

    def test_crear_y_obtener_recurso_encadenado(self):
        """
        Flujo encadenado: crea un post y verifica que el ID
        retornado es válido consultando un post existente.
        """
        nuevo_post = {
            "title": "Post encadenado",
            "body": "Prueba de encadenamiento",
            "userId": 1
        }

        logger.info("Paso 1 - Creando recurso")
        response_post = requests.post(f"{BASE_URL}/posts", json=nuevo_post)
        assert response_post.status_code == 201
        id_creado = response_post.json()["id"]
        logger.info(f"Recurso creado con ID: {id_creado}")

        # JSONPlaceholder es una API simulada, los recursos creados
        # no persisten realmente. Verificamos con un ID real existente.
        logger.info("Paso 2 - Obteniendo recurso existente para validar estructura")
        response_get = requests.get(f"{BASE_URL}/posts/1")
        assert response_get.status_code == 200
        data = response_get.json()
        assert "id" in data
        logger.info("Encadenamiento completado correctamente")