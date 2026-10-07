# Proyecto Backend - Sistema de Venta de Tickets

Aplicación web backend desarrollada con **Django**, orientada a la gestión y venta de tickets para eventos.

El proyecto incorpora una **API RESTful desarrollada con Django REST Framework (DRF)**, permitiendo administrar eventos, encuestas y opciones de respuesta mediante operaciones HTTP estándar.

---

## 1. Tecnologías utilizadas

- Python 3.11+
- Django 5.2
- Django REST Framework
- PostgreSQL
- HTML5
- CSS3
- Git
- GitHub

---

## 2. Funcionalidades principales

El sistema permite:

- Gestionar eventos.
- Consultar información de eventos.
- Crear, modificar y eliminar eventos.
- Gestionar encuestas asociadas a eventos.
- Gestionar opciones de respuesta de las encuestas.
- Registrar y consultar votos mediante la funcionalidad existente del proyecto.
- Administrar información mediante Django Admin.
- Utilizar una API RESTful.
- Utilizar autenticación mediante sesión y token.
- Controlar permisos para operaciones de lectura y escritura.
- Entregar respuestas en formato JSON.
- Utilizar paginación en los endpoints de la API.

---

# 3. Estructura general del proyecto

```text
proyectobackend/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── events/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── polls/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── migrations/
│   ├── models.py
│   └── ...
│
├── static/
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 4. Requisitos previos

Antes de ejecutar el proyecto se necesita tener instalado:

- Python 3.11 o superior.
- PostgreSQL.
- Git.
- Un editor de código, como Visual Studio Code.

---

# 5. Clonar el proyecto

Clonar el repositorio:

```bash
git clone https://github.com/Tiocore/proyectobackend.git
```

Ingresar al proyecto:

```bash
cd proyectobackend
```

---

# 6. Crear el entorno virtual

Crear el entorno virtual:

```bash
python -m venv .venv
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Si el entorno se activó correctamente, aparecerá `(.venv)` al comienzo de la terminal.

---

# 7. Instalar las dependencias

Con el entorno virtual activo:

```bash
pip install -r requirements.txt
```

Entre las dependencias principales se encuentran:

- Django
- Django REST Framework
- PostgreSQL
- Gunicorn
- Pillow
- dj-database-url

---

# 8. Configuración de PostgreSQL

El proyecto utiliza **PostgreSQL** como sistema de gestión de base de datos.

La configuración de la conexión debe realizarse mediante variables de entorno y no mediante credenciales escritas directamente en el código fuente.

Ejemplo de variables:

```text
DB_NAME=nombre_base_datos
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=5432
```

Los valores reales de las credenciales no deben publicarse en GitHub.

---

# 9. Migraciones

Después de configurar la base de datos:

```bash
python manage.py makemigrations
```

Luego:

```bash
python manage.py migrate
```

Esto crea y actualiza las tablas necesarias para las aplicaciones del proyecto.

---

# 10. Crear usuario administrador

Para crear un usuario administrador:

```bash
python manage.py createsuperuser
```

Seguir las instrucciones de Django para establecer:

- nombre de usuario;
- correo electrónico;
- contraseña.

El panel administrativo estará disponible en:

```text
http://127.0.0.1:8000/admin/
```

---

# 11. Ejecutar el proyecto

Iniciar el servidor:

```bash
python manage.py runserver
```

La aplicación estará disponible en:

```text
http://127.0.0.1:8000/
```

---

# 12. API REST

El proyecto utiliza **Django REST Framework** para proporcionar una API RESTful.

La API utiliza:

- Serializers.
- ViewSets.
- Routers.
- JSON.
- Autenticación.
- Permisos.
- Paginación.
- Operaciones CRUD.

La API se encuentra bajo el prefijo:

```text
/api/
```

---

# 13. API de Events

## Listar eventos

```http
GET /api/events/
```

Obtiene todos los eventos disponibles.

---

## Obtener un evento

```http
GET /api/events/<id>/
```

Ejemplo:

```http
GET /api/events/1/
```

---

## Crear un evento

```http
POST /api/events/
```

Ejemplo:

```json
{
    "name": "Nuevo Evento",
    "description": "Descripción del evento",
    "date": "2026-11-15T18:00:00Z",
    "location": "Parque O'Higgins",
    "price": "2500.00",
    "capacity": 500,
    "image": null
}
```

---

## Actualizar completamente un evento

```http
PUT /api/events/<id>/
```

---

## Actualizar parcialmente un evento

```http
PATCH /api/events/<id>/
```

Ejemplo:

```json
{
    "price": "3000.00"
}
```

---

## Eliminar un evento

```http
DELETE /api/events/<id>/
```

Una eliminación exitosa devuelve:

```text
204 No Content
```

---

# 14. API de Polls

Las encuestas están relacionadas con los eventos mediante una relación `OneToOne`.

## Listar encuestas

```http
GET /api/polls/
```

---

## Obtener una encuesta

```http
GET /api/polls/<id>/
```

---

## Crear una encuesta

```http
POST /api/polls/
```

Ejemplo:

```json
{
    "event": 1,
    "question": "¿Qué te pareció este evento?"
}
```

Un evento solamente puede tener una encuesta asociada.

---

## Actualizar completamente una encuesta

```http
PUT /api/polls/<id>/
```

---

## Actualizar parcialmente una encuesta

```http
PATCH /api/polls/<id>/
```

Ejemplo:

```json
{
    "question": "¿Qué opinas de la experiencia del evento?"
}
```

---

## Eliminar una encuesta

```http
DELETE /api/polls/<id>/
```

Respuesta esperada:

```text
204 No Content
```

---

# 15. API de Choices

Las opciones pertenecen a una encuesta mediante una relación `ForeignKey`.

## Listar opciones

```http
GET /api/choices/
```

---

## Obtener una opción

```http
GET /api/choices/<id>/
```

---

## Crear una opción

```http
POST /api/choices/
```

Ejemplo:

```json
{
    "poll": 1,
    "choice_text": "Excelente"
}
```

El campo `votes` se genera automáticamente con valor inicial `0`.

---

## Actualizar completamente una opción

```http
PUT /api/choices/<id>/
```

---

## Actualizar parcialmente una opción

```http
PATCH /api/choices/<id>/
```

Ejemplo:

```json
{
    "choice_text": "Muy buena"
}
```

---

## Eliminar una opción

```http
DELETE /api/choices/<id>/
```

Respuesta esperada:

```text
204 No Content
```

---

# 16. Resumen de endpoints

| Método | Endpoint | Función |
|---|---|---|
| GET | `/api/events/` | Listar eventos |
| POST | `/api/events/` | Crear evento |
| GET | `/api/events/<id>/` | Obtener evento |
| PUT | `/api/events/<id>/` | Actualizar evento |
| PATCH | `/api/events/<id>/` | Actualizar parcialmente |
| DELETE | `/api/events/<id>/` | Eliminar evento |
| GET | `/api/polls/` | Listar encuestas |
| POST | `/api/polls/` | Crear encuesta |
| GET | `/api/polls/<id>/` | Obtener encuesta |
| PUT | `/api/polls/<id>/` | Actualizar encuesta |
| PATCH | `/api/polls/<id>/` | Actualizar parcialmente |
| DELETE | `/api/polls/<id>/` | Eliminar encuesta |
| GET | `/api/choices/` | Listar opciones |
| POST | `/api/choices/` | Crear opción |
| GET | `/api/choices/<id>/` | Obtener opción |
| PUT | `/api/choices/<id>/` | Actualizar opción |
| PATCH | `/api/choices/<id>/` | Actualizar parcialmente |
| DELETE | `/api/choices/<id>/` | Eliminar opción |

---

# 17. Autenticación

La API utiliza dos mecanismos de autenticación:

- Session Authentication.
- Token Authentication.

La configuración se encuentra en `config/settings.py`.

Las operaciones de lectura son públicas, mientras que las operaciones de modificación requieren autenticación según los permisos configurados.

---

# 18. Autenticación mediante Token

Para obtener un token se puede utilizar:

```http
POST /api-token-auth/
```

Ejemplo:

```json
{
    "username": "usuario",
    "password": "contraseña"
}
```

La respuesta contiene:

```json
{
    "token": "..."
}
```

El token debe enviarse en las peticiones protegidas mediante:

```http
Authorization: Token TU_TOKEN
```

Los tokens deben mantenerse privados y nunca deben publicarse en el repositorio.

---

# 19. Autenticación mediante sesión

Django REST Framework también proporciona autenticación mediante sesión.

El acceso está disponible mediante:

```text
http://127.0.0.1:8000/api-auth/login/
```

Esta opción permite utilizar la interfaz navegable de Django REST Framework durante el desarrollo.

---

# 20. Permisos

La API utiliza:

```python
IsAuthenticatedOrReadOnly
```

Esto significa que:

- Las peticiones `GET` pueden realizarse sin autenticación.
- Las operaciones de escritura requieren autenticación.

Las operaciones protegidas incluyen:

```text
POST
PUT
PATCH
DELETE
```

---

# 21. Respuestas JSON

Los endpoints de la API utilizan JSON como formato principal de respuesta.

Ejemplo:

```json
{
    "id": 1,
    "name": "Festival de Música",
    "description": "Evento musical",
    "date": "2026-10-29T16:30:00Z",
    "location": "Santiago",
    "price": "1000.00",
    "capacity": 300,
    "image": null
}
```

---

# 22. Paginación

La API utiliza paginación mediante:

```python
PageNumberPagination
```

con un máximo de:

```text
10 registros por página
```

Cuando existen suficientes registros, la respuesta puede incluir:

```json
{
    "count": 20,
    "next": "...",
    "previous": null,
    "results": []
}
```

---

# 23. Validaciones y manejo de errores

Django REST Framework permite validar automáticamente los datos recibidos mediante los serializers y los modelos de Django.

Ante datos inválidos, la API devuelve:

```text
400 Bad Request
```

Los recursos inexistentes devuelven:

```text
404 Not Found
```

Una eliminación exitosa devuelve:

```text
204 No Content
```

Las operaciones que requieren autenticación pueden devolver:

```text
401 Unauthorized
```

o:

```text
403 Forbidden
```

dependiendo del mecanismo de autenticación utilizado.

---

# 24. Seguridad

Se aplican las siguientes recomendaciones:

- Las credenciales de PostgreSQL no deben almacenarse directamente en el código.
- Las variables sensibles deben mantenerse en variables de entorno.
- El archivo `.env` está excluido mediante `.gitignore`.
- Los tokens de autenticación no deben compartirse públicamente.
- `SECRET_KEY` debe mantenerse protegida.
- En producción se recomienda utilizar HTTPS.
- `ALLOWED_HOSTS` debe configurarse correctamente.
- `CSRF_TRUSTED_ORIGINS` debe configurarse para los dominios que correspondan.
- Las dependencias deben mantenerse actualizadas.
- No se deben subir bases de datos locales o archivos sensibles al repositorio.

---

# 25. Comprobación del proyecto

Para verificar que la configuración de Django no tenga errores:

```bash
python manage.py check
```

El resultado esperado es:

```text
System check identified no issues (0 silenced).
```

Para comprobar las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# 26. Git y GitHub

El proyecto utiliza Git para el control de versiones y GitHub para almacenar el código fuente.

Repositorio:

```text
https://github.com/Tiocore/proyectobackend
```

Comandos principales:

```bash
git status
git add .
git commit -m "Descripción del cambio"
git push origin main
```

---

# 27. Archivos excluidos del repositorio

El proyecto utiliza `.gitignore` para evitar subir archivos innecesarios o sensibles.

Entre ellos:

```text
.venv/
__pycache__/
*.py[cod]
.env
db.sqlite3
staticfiles/
```

---

# 28. Despliegue

El proyecto fue preparado para ejecutarse en un entorno de producción utilizando las configuraciones correspondientes de Django y PostgreSQL.

Para producción se deben configurar correctamente:

- Variables de entorno.
- Base de datos PostgreSQL.
- `ALLOWED_HOSTS`.
- `CSRF_TRUSTED_ORIGINS`.
- `SECRET_KEY`.
- HTTPS.
- Archivos estáticos.
- Servidor WSGI.

---

# 29. Objetivo académico

El proyecto tiene como objetivo aplicar conceptos de desarrollo backend utilizando Django y desarrollar una API RESTful funcional mediante Django REST Framework.

Se implementaron:

- Arquitectura basada en Django.
- Modelos y relaciones.
- Persistencia mediante PostgreSQL.
- Operaciones CRUD.
- API REST.
- Serialización de datos.
- Autenticación.
- Autorización.
- Validación de datos.
- Manejo de errores HTTP.
- JSON.
- Paginación.
- Control de versiones mediante Git.
- Documentación del proyecto.

---

# 30. Estado del proyecto

Actualmente el proyecto cuenta con:

```text
✓ Django configurado
✓ PostgreSQL configurado
✓ Eventos funcionando
✓ Encuestas funcionando
✓ Opciones funcionando
✓ API REST implementada
✓ CRUD de Events
✓ CRUD de Polls
✓ CRUD de Choices
✓ GET
✓ POST
✓ PUT
✓ PATCH
✓ DELETE
✓ JSON
✓ Serializers
✓ ViewSets
✓ Routers
✓ Paginación
✓ Token Authentication
✓ Session Authentication
✓ Permisos
✓ Validaciones
✓ Manejo de errores
✓ README documentado
✓ Git configurado
✓ Proyecto publicado en GitHub
```

---

## Autor

Proyecto desarrollado como parte del aprendizaje y aplicación práctica de tecnologías backend con **Python, Django, Django REST Framework y PostgreSQL**.