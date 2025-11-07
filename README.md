# Servicio de Parámetros

Microservicio en Django + DRF para gestionar parámetros con valores flexibles (null, number, boolean, string, array, object).

## Tecnologías
- Python 3.9
- Django 4.2
- Django REST Framework
- PostgreSQL
- Docker / docker-compose

## Arquitectura y patrón de diseño
- Arquitectura: microservicio REST (Django + DRF) containerizado.
- Patrón: MVC (Model + Serializer + ViewSet + Router). `ModelViewSet` expone CRUD REST.

## Entornos
Selección por variable `DJANGO_ENV` (dev|test|prod). Archivos: `.env`, `.env.test`, `.env.prod` (se cargan según `DJANGO_ENV`). Se recomienda incluir un `.env.example` (no incluido aún) para documentar variables:

```
DJANGO_SECRET_KEY=
DJANGO_DEBUG=
DB_NAME=
DB_USER=
DB_PASS=
DB_HOST=
DB_PORT=
DJANGO_ALLOWED_HOSTS=
```

## Inicio rápido con docker-compose
Requiere Docker y docker-compose plugin.

```bash
docker compose up --build
```

El servicio:
- Ejecuta migraciones automáticamente (ver [docker-compose.yml](docker-compose.yml)).
- Expone API en http://localhost:8000/api/v1/
- Base de datos PostgreSQL expuesta en puerto 5432 (solo local).

Detener:
```bash
docker compose down
```

Logs:
```bash
docker compose logs -f web
```

### Ejecutar pruebas dentro del contenedor
```bash
docker compose run --rm web python manage.py test
```

### Cambiar entorno
Editar la sección `environment` del servicio `web` en [docker-compose.yml](docker-compose.yml) (p.e. `DJANGO_ENV: prod` y ajustar variables).

## Ejecución sin Docker (opcional)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export DJANGO_ENV=dev
python manage.py migrate
python manage.py runserver
```

## Endpoints
Base `/api/v1/`
- GET /parameters/
- POST /parameters/
- GET /parameters/{name}/
- PUT /parameters/{name}/
- PATCH /parameters/{name}/
- DELETE /parameters/{name}/

Ejemplo creación:
```json
{ "name": "policyAlert", "values": true }
```

## Tests
Incluye prueba de creación ([parameters/tests.py](parameters/tests.py)).

## Despliegue (resumen)
1. Construir imagen: `docker build -t your-registry/parameter-service:TAG .`
2. Publicar en registry.
3. Kubernetes/ECS: definir secretos con las variables y aplicar manifiestos (ver futura carpeta `k8s/`).

## Seguridad y validación
- `values`: validado como tipos JSON (ver [parameters/serializers.py](parameters/serializers.py)).
- Respuestas: DRF maneja códigos estándar (201, 200, 400, 404, 204).