# Servicio de Parámetros

Microservicio en Django + DRF para gestionar parámetros con valores flexibles (null, number, boolean, string, array, object).

## Tecnologías
- Python 3.9
- Django 4.2
- Django REST Framework
- PostgreSQL
- Docker (y despliegue en Kubernetes)

## Arquitectura y patrón de diseño
- Arquitectura: microservicio REST, containerizado.
- Patrón: MVC de Django con DRF (Model + Serializer + ViewSet + Router). Se expone una API RESTful con `ModelViewSet` y enrutamiento automático.

## Configuración de entornos
El proyecto selecciona el archivo de entorno por `DJANGO_ENV`:
- dev → .env
- test → .env.test
- prod → .env.prod

Variables requeridas: DJANGO_SECRET_KEY, DJANGO_DEBUG, DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT.

## Ejecución local
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Elegir entorno
export DJANGO_ENV=dev  # o test/prod

python manage.py migrate
python manage.py runserver
```
API base: http://127.0.0.1:8000/api/v1/  
Docs: http://127.0.0.1:8000/swagger/

## Pruebas
```bash
export DJANGO_ENV=test
python manage.py test
```

## Docker
```bash
docker build -t parameter-service:local .
docker run -p 8000:8000 \
  -e DJANGO_ENV=prod \
  -e DJANGO_SECRET_KEY=change-me \
  -e DJANGO_DEBUG=False \
  -e DB_NAME=parameter_db \
  -e DB_USER=user \
  -e DB_PASS=pass \
  -e DB_HOST=host.docker.internal \
  -e DB_PORT=5432 \
  parameter-service:local
```

## Kubernetes
- Empaqueta y publica la imagen en tu registry.
- Crea los `Secrets` con las variables.
- Aplica manifiestos:
```bash
kubectl apply -f k8s/deployment.yaml
```

## Endpoints
Base `/api/v1/`
- GET/POST `/parameters/`
- GET/PUT/DELETE `/parameters/{name}/`

Ejemplo body:
```json
{ "name": "policyAlert", "values": true }
```