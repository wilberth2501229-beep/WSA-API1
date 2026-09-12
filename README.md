# WSA-API1

API web desarrollada con Flask, Flask-RESTful y Supabase. El proyecto incluye paginas para la pantalla principal, inicio de sesion y registro de usuarios.

## Requisitos

- Python 3.10 o superior
- Una cuenta y un proyecto de Supabase

## Instalacion

Clona el repositorio y entra en su carpeta:

```bash
git clone https://github.com/wilberth2501229-beep/WSA-API1.git
cd WSA-API1
```

Crea y activa un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Configuracion de Supabase

Copia el archivo de ejemplo:

```bash
cp .env.example .env
```

Edita `.env` y agrega los datos de tu proyecto:

```env
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_KEY=tu-clave-de-supabase
```

No subas `.env` a GitHub. El archivo esta incluido en `.gitignore` para evitar publicar las credenciales.

La tabla `usuarios` debe existir en Supabase para que el registro funcione.

## Ejecucion

Con el entorno virtual activo, ejecuta:

```bash
python app.py
```

El servidor estara disponible en:

```text
http://localhost:8080
```

Para detenerlo, presiona `Ctrl + C`.

## Rutas disponibles

| Metodo | Ruta | Descripcion |
| --- | --- | --- |
| GET | `/` | Muestra la pagina principal |
| GET | `/hola` | Devuelve un mensaje de prueba |
| GET | `/login` | Muestra el formulario de inicio de sesion |
| POST | `/login` | Recibe los datos del formulario de inicio de sesion |
| GET | `/signup` | Muestra el formulario de registro |
| POST | `/signup` | Registra un usuario en Supabase |

## Estructura del proyecto

```text
WSA-API1/
├── app.py
├── extensiones.py
├── recursos.py
├── rutas.py
├── requirements.txt
├── .env.example
└── templates/
    ├── index.html
    ├── loginpage.html
    └── signup.html
```

## Seguridad

- No incluyas claves reales en el codigo fuente.
- No subas el archivo `.env` al repositorio.
- Si una clave ya fue publicada, revocala o regenerala desde Supabase.
