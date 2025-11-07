# Servicio de Parámetros

Este es un microservicio desarrollado en Django y Django REST Framework para gestionar parámetros de configuración con valores flexibles.

## Tecnologías

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL

## Instalación y Ejecución Local

Sigue estos pasos para levantar el proyecto en tu entorno local.

**1. Prerrequisitos**

- Tener Python 3 y `pip` instalados.
- Tener PostgreSQL instalado y corriendo.

**2. Clonar el Repositorio**

```bash
git clone <URL-de-tu-repo-en-github>
cd <nombre-de-la-carpeta>
```

**3. Configurar Entorno Virtual e Instalar Dependencias**

```bash
python -m venv venv
# Activar entorno:
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt
```
*(Nota: debes crear el archivo `requirements.txt` con `pip freeze > requirements.txt`)*

**4. Configurar Base de Datos**

- Crea una base de datos en PostgreSQL (ej. `parameter_db`).
- Renombra el archivo `.env.example` a `.env` y edita las variables de conexión a la base de datos. 
  *(Nota: Esto es una mejora. Modificarías `settings.py` para leer de un archivo `.env` usando una librería como `python-decouple`)*.
- O, edita directamente `config/settings.py` con tus credenciales de la base de datos.

**5. Aplicar Migraciones e Iniciar Servidor**

```bash
python manage.py migrate
python manage.py runserver
```

El servicio estará disponible en `http://127.0.0.1:8000`.

**6. Ejecutar Pruebas Unitarias**

```bash
python manage.py test
```

## Endpoints de la API

La base de la API es `/api/v1/`.

- `GET /api/v1/parameters/`: Lista todos los parámetros.
- `POST /api/v1/parameters/`: Crea un nuevo parámetro.
- `GET /api/v1/parameters/{name}/`: Obtiene un parámetro por su nombre.
- `PUT /api/v1/parameters/{name}/`: Actualiza un parámetro por su nombre.
- `DELETE /api/v1/parameters/{name}/`: Elimina un parámetro por su nombre.

### Ejemplo de Body para POST/PUT

```json
{
    "name": "parameterName",
    "values": ["any", "valid", "json", true, 123, {"nested": "object"}]
}
```