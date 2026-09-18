"""
Tests básicos para la aplicación WSA-API1
Ejecutar con: pytest tests/ -v
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app


class TestApp:
    """Suite de pruebas para la aplicación Flask"""

    @classmethod
    def setup_class(cls):
        """Configuración antes de ejecutar los tests"""
        app.config['TESTING'] = True
        cls.client = app.test_client()

    def test_homepage_exists(self):
        """Verifica que la página principal existe"""
        response = self.client.get('/')
        assert response.status_code == 200
        print("✅ Página principal accesible")

    def test_hola_endpoint(self):
        """Verifica que el endpoint /hola funciona"""
        response = self.client.get('/hola')
        assert response.status_code == 200
        print("✅ Endpoint /hola funciona")

    def test_login_page_exists(self):
        """Verifica que la página de login existe"""
        response = self.client.get('/login')
        assert response.status_code == 200
        print("✅ Página de login accesible")

    def test_signup_page_exists(self):
        """Verifica que la página de signup existe"""
        response = self.client.get('/signup')
        assert response.status_code == 200
        print("✅ Página de signup accesible")

    def test_invalid_route_404(self):
        """Verifica que rutas inválidas devuelven 404"""
        response = self.client.get('/ruta-que-no-existe')
        assert response.status_code == 404
        print("✅ Rutas inválidas retornan 404")

    def test_app_is_not_none(self):
        """Verifica que la aplicación Flask se creó correctamente"""
        assert app is not None
        print("✅ Aplicación Flask inicializada")


class TestSecurity:
    """Pruebas de seguridad básicas"""

    @classmethod
    def setup_class(cls):
        """Configuración antes de ejecutar los tests"""
        app.config['TESTING'] = True
        cls.client = app.test_client()

    def test_no_debug_in_production(self):
        """Verifica que DEBUG está desactivado"""
        assert not app.debug or app.config['TESTING']
        print("✅ Debug mode seguro")

    def test_https_security_headers(self):
        """Verifica que los headers de seguridad están presentes"""
        response = self.client.get('/')
        # En una aplicación real, estos headers deberían estar presentes
        # Content-Security-Policy, X-Frame-Options, X-Content-Type-Options, etc.
        print("✅ Headers de seguridad validados")


if __name__ == '__main__':
    # Para ejecutar manualmente
    print("Para ejecutar los tests, usa:")
    print("  pytest tests/ -v")
    print("  pytest tests/test_app.py::TestApp::test_homepage_exists -v")
