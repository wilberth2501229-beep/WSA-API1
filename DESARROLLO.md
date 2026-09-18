# Guía de Desarrollo - WSA-API1

## Instalación Local

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/WSA-API1.git
cd WSA-API1
```

### 2. Crear entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecutar la Aplicación

```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:8080`

---

## Pruebas Locales

### Ejecutar todos los tests

```bash
pytest tests/ -v
```

### Ejecutar un test específico

```bash
pytest tests/test_app.py::TestApp::test_homepage_exists -v
```

### Ver cobertura de tests

```bash
pytest tests/ --cov=. --cov-report=html
```

Abre `htmlcov/index.html` en el navegador para ver el reporte.

---

## Análisis de Seguridad Local

### Revisar dependencias vulnerables

```bash
pip install safety
safety check
```

### Análisis estático de seguridad

```bash
pip install bandit
bandit -r . -ll
```

---

## Validar Sintaxis

```bash
python -m py_compile app.py recursos.py rutas.py extensiones.py
```

---

## Simulación del Pipeline Completo

Ejecuta esto localmente para simular lo que hace el pipeline en GitHub:

```bash
#!/bin/bash

echo "📦 Etapa 1: BUILD"
pip install -r requirements.txt
echo "✅ Dependencias instaladas"

echo ""
echo "✅ Etapa 2: TEST"
pytest tests/ -v
echo "✅ Tests completados"

echo ""
echo "🔒 Etapa 3: SECURITY"
safety check || echo "⚠️ Revisa vulnerabilidades"
bandit -r . -ll || echo "⚠️ Revisa problemas de seguridad"
echo "✅ Análisis de seguridad completado"

echo ""
echo "🚀 Etapa 4: DEPLOY"
echo "✅ Aplicación lista para despliegue"
```

Guarda esto en `run-pipeline.sh` y ejecuta:

```bash
chmod +x run-pipeline.sh
./run-pipeline.sh
```

---

## Configurar GitHub Actions

Para que el pipeline se ejecute automáticamente:

1. **Push del código a GitHub**

   ```bash
   git add .
   git commit -m "feat: agregar pipeline CI/CD"
   git push origin main
   ```

2. **Configurar Secrets en GitHub**

   - Ve a: `Settings → Secrets and variables → Actions → New repository secret`
   - Agrega:
     - `SUPABASE_URL`: Tu URL de Supabase
     - `SUPABASE_KEY`: Tu clave de API

3. **Ver ejecución del pipeline**

   - Ve a la pestaña "Actions" en tu repositorio de GitHub
   - Verás el pipeline ejecutándose en tiempo real

---

## Estructura de Carpetas

```
WSA-API1/
├── app.py                 # Punto de entrada principal
├── recursos.py            # Definición de recursos API
├── rutas.py              # Rutas de la aplicación
├── extensiones.py        # Extensiones (BD, etc)
├── requirements.txt      # Dependencias Python
├── .env.example          # Ejemplo de variables de entorno
├── .github/
│   └── workflows/
│       └── pipeline.yml  # Configuración del pipeline CI/CD
├── templates/            # Archivos HTML
│   ├── index.html
│   ├── loginpage.html
│   └── signup.html
├── tests/               # Pruebas unitarias
│   └── test_app.py
├── PIPELINE.md          # Documentación del pipeline
└── DESARROLLO.md        # Este archivo
```

---

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'flask'"

Solución:
```bash
pip install -r requirements.txt
```

### Error: "Supabase credentials not found"

Solución:
```bash
cp .env.example .env
# Edita .env y agrega tus credenciales reales
```

### Tests fallan localmente pero pasan en CI

Compara las versiones de Python:
```bash
python --version  # Debe ser 3.10 o superior
```

---

## Contribuir

1. Crea una rama nueva:
   ```bash
   git checkout -b feature/tu-feature
   ```

2. Haz cambios y haz commit:
   ```bash
   git add .
   git commit -m "feat: descripción de tu cambio"
   ```

3. Push a GitHub:
   ```bash
   git push origin feature/tu-feature
   ```

4. Crea un Pull Request

El pipeline se ejecutará automáticamente y validará tu código antes de mergearlo.

---

## Referencias

- [Documentación del Pipeline](PIPELINE.md)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
