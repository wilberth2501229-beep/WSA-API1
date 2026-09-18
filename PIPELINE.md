# Pipeline CI/CD para WSA-API1

## ¿Qué es un Pipeline?

Un **pipeline** es una serie de pasos automatizados que se ejecutan secuencialmente para validar, probar y desplegar código. Es como una cadena de montaje que asegura que tu código sea confiable y esté listo para producción.

---

## Estructura del Pipeline

Este proyecto implementa un pipeline de **4 etapas principales**:

### 📦 Etapa 1: BUILD (Construcción)

**¿Qué ocurre?**
- Se clona el repositorio en un servidor limpio
- Se configura el entorno de Python 3.10
- Se instalan todas las dependencias desde `requirements.txt`
- Se verifica que las dependencias se instalaron correctamente

**¿Por qué es importante?**
- Asegura que el proyecto sea compilable en un entorno limpio
- Detecta dependencias faltantes o incompatibles antes de pasar a las siguientes etapas
- Garantiza que cualquier persona pueda ejecutar el proyecto sin errores de setup

**Comandos ejecutados:**
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

### ✅ Etapa 2: TEST (Pruebas)

**¿Qué ocurre?**
- Se ejecutan pruebas unitarias (si están definidas)
- Se valida la sintaxis de todos los archivos Python
- Se verifica la estructura y formato del código
- Se genera un reporte de cobertura de tests

**¿Por qué es importante?**
- Detecta errores lógicos en el código antes de que lleguen a producción
- Asegura que los cambios no rompan funcionalidades existentes
- Valida que el código siga los estándares de calidad

**Archivos validados:**
- `app.py`
- `recursos.py`
- `rutas.py`
- `extensiones.py`

---

### 🔒 Etapa 3: SECURITY (Análisis de Seguridad)

**¿Qué ocurre?**
- Se revisan las dependencias en busca de vulnerabilidades conocidas (Safety)
- Se realiza un análisis estático de seguridad (Bandit)
- Se verifica que no haya credenciales hardcodeadas en el código
- Se valida que el archivo `.env` no esté en el repositorio

**¿Por qué es importante?**
- Previene vulnerabilidades de seguridad antes de que afecten a usuarios
- Evita que credenciales sensibles se filtren en GitHub
- Cumple con estándares de seguridad recomendados

**Herramientas utilizadas:**
- **Safety**: Revisa dependencias vulnerables
- **Bandit**: Análisis estático de seguridad Python

---

### 🚀 Etapa 4: DEPLOY (Despliegue)

**¿Qué ocurre?**
- Se verifica que todas las etapas anteriores pasaron correctamente
- Se validan las variables de entorno (Secrets en GitHub)
- Se prepara la aplicación para producción
- Se notifica que está lista para despliegue

**¿Por qué es importante?**
- Solo código validado llega a producción
- Automatiza el proceso de actualización
- Minimiza errores humanos en deployments

**Nota:** Este proyecto es educativo, así que el deploy es manual. En proyectos reales se usaría:
- Heroku, AWS, Google Cloud, DigitalOcean
- Docker para contenerizar la aplicación
- Kubernetes para orquestación

---

## Flujo General

```
Haces Push a GitHub (main o PR)
        ↓
┌───────────────────────────────────┐
│  ✅ BUILD (Instala dependencias)  │
└───────────────┬───────────────────┘
                ↓
┌───────────────────────────────────┐
│  ✅ TEST (Ejecuta pruebas)        │
└───────────────┬───────────────────┘
                ↓
┌───────────────────────────────────┐
│  ✅ SECURITY (Revisa seguridad)   │
└───────────────┬───────────────────┘
                ↓
┌───────────────────────────────────┐
│  ✅ DEPLOY (A producción si todo OK)
└───────────────────────────────────┘
```

---

## Configuración

### 1. Archivo de configuración

El pipeline se define en: `.github/workflows/pipeline.yml`

Este archivo usa **GitHub Actions** para ejecutarse automáticamente cuando:
- Haces `push` a la rama `main`
- Haces `push` a ramas que comienzan con `feature_`
- Creas un Pull Request hacia `main`

### 2. Variables de Entorno (Secrets)

Para que el deploy funcione, debes configurar en GitHub:

```
Settings → Secrets and variables → Actions → New repository secret
```

Agrega:
- `SUPABASE_URL`: Tu URL de Supabase
- `SUPABASE_KEY`: Tu clave de Supabase

**Nunca** hagas commit de credenciales reales en el código.

---

## Estados del Pipeline

| Estado | Significado | Acción |
|--------|-------------|--------|
| 🟡 Pending | Pipeline en ejecución | Espera a que termine |
| ✅ Success | Todo pasó correctamente | Código listo para producción |
| ❌ Failed | Algo falló | Revisa los logs y corrige |
| ⏭️ Skipped | Etapa omitida | Según condiciones configuradas |

---

## Beneficios de este Pipeline

✅ **Automatización**: No esperes a desplegar, el pipeline lo hace automáticamente  
✅ **Calidad**: Detecta errores antes de producción  
✅ **Seguridad**: Revisa vulnerabilidades y credenciales expuestas  
✅ **Confiabilidad**: Asegura que los cambios no rompan nada  
✅ **Trazabilidad**: Cada cambio tiene un historial de qué pasó en cada etapa  

---

## Ejemplo de Ejecución

Cuando haces un commit y push:

```bash
git add .
git commit -m "feat: nueva funcionalidad"
git push origin feature_nueva-funcionalidad
```

El pipeline se ejecuta automáticamente:

```
[08:15:00] 🟡 Build iniciado...
[08:15:45] ✅ Build completado (instalar dependencias)
[08:16:00] 🟡 Test iniciado...
[08:16:30] ✅ Test completado (0 errores)
[08:16:45] 🟡 Security iniciado...
[08:17:15] ✅ Security completado (sin vulnerabilidades)
[08:17:30] 🟡 Deploy iniciado...
[08:18:00] ✅ Deploy completado (lista para producción)
```

Si algo falla, recibirás una notificación y podrás ver el error detallado.

---

## Próximos Pasos

Para mejorar este pipeline, puedes:

1. **Agregar pruebas unitarias**
   ```bash
   mkdir tests/
   # Crea archivos test_*.py
   ```

2. **Configurar cobertura de tests**
   - Usar `pytest-cov` para medir qué porcentaje del código está testeado

3. **Agregar linting (análisis de estilo)**
   - Usar `pylint` o `flake8` para validar que el código siga PEP8

4. **Integrar DockerHub**
   - Generar imágenes Docker automáticamente

5. **Deploy automático a servidor real**
   - Conectar con Heroku, AWS, o tu servidor propio

---

## Referencias

- [GitHub Actions Documentation](https://docs.github.com/es/actions)
- [Python Best Practices](https://pep8.org/)
- [Flask Deployment](https://flask.palletsprojects.com/deployment/)
