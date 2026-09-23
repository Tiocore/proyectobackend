# Proyecto Backend Django - Sistema de Venta de Tickets

## 1. Descripción del proyecto

Proyecto backend desarrollado con Django para la gestión y venta de tickets para eventos.

El sistema permite administrar eventos, consultar su información, visualizar imágenes, responder encuestas asociadas a cada evento y consultar los resultados de las encuestas con sus respectivos porcentajes.

El proyecto fue desarrollado como parte de una evaluación de desarrollo backend y contempla desarrollo local, control de versiones, pruebas y despliegue en producción.

---

## 2. Tecnologías utilizadas

* Python 3.11.9
* Django 5.2.17
* Pillow 12.3.0
* HTML5
* CSS3
* JavaScript
* SQLite para desarrollo local
* PostgreSQL para producción
* Gunicorn
* WhiteNoise
* dj-database-url
* psycopg
* Visual Studio Code
* Git
* GitHub
* Railway
* Inteligencia Artificial como apoyo al desarrollo y documentación

---

## 3. Estructura principal del proyecto

```text
proyectobackend/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── events/
│   ├── migrations/
│   ├── templates/
│   │   └── events/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── seed_data.py
│
├── polls/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   └── ...
│
├── media/
├── staticfiles/
├── manage.py
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md
```

---

## 4. Aplicaciones Django

El proyecto utiliza principalmente dos aplicaciones:

### Events

La aplicación `events` administra los eventos disponibles.

Permite:

* Listar eventos.
* Mostrar información detallada de cada evento.
* Mostrar nombre.
* Mostrar descripción.
* Mostrar fecha.
* Mostrar ubicación.
* Mostrar precio.
* Mostrar capacidad.
* Mostrar imágenes.
* Acceder a la encuesta asociada.
* Acceder a los resultados de la encuesta.

### Polls

La aplicación `polls` administra las encuestas y sus alternativas.

Cada evento puede tener una encuesta asociada y cada encuesta posee diferentes alternativas de respuesta.

---

## 5. Modelos

### Modelo Event

El modelo `Event` contiene:

* `name`
* `description`
* `date`
* `location`
* `price`
* `capacity`
* `image`

El campo `price` utiliza `DecimalField` para manejar valores monetarios.

El campo `image` utiliza `ImageField`, permitiendo almacenar imágenes asociadas a los eventos.

### Modelo Poll

El modelo `Poll` contiene:

* `event`
* `question`

La relación con `Event` utiliza `OneToOneField`.

### Modelo Choice

El modelo `Choice` contiene:

* `poll`
* `choice_text`
* `votes`

La relación con `Poll` utiliza `ForeignKey`.

La estructura permite:

```text
Event
  │
  └── Poll
        │
        ├── Choice
        ├── Choice
        ├── Choice
        └── Choice
```

---

## 6. Funcionalidades principales

### Gestión de eventos

Los eventos pueden ser administrados desde el panel de administración de Django.

El sistema permite crear, modificar y consultar eventos.

### Imágenes

Las imágenes de los eventos son administradas mediante Pillow y Django `ImageField`.

Configuración utilizada:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

### Encuestas

Cada evento puede tener una encuesta con diferentes alternativas.

El usuario puede seleccionar una alternativa y enviar su voto mediante una solicitud `POST`.

### Resultados

El sistema calcula automáticamente el porcentaje correspondiente a cada alternativa.

La fórmula utilizada es:

```text
porcentaje = (votos de la alternativa / total de votos) × 100
```

El resultado se redondea a dos decimales.

También se contempla el caso en que todavía no existan votos, evitando una división por cero.

---

## 7. Datos de prueba

El proyecto incluye un script:

```text
events/seed_data.py
```

Este script permite generar datos de prueba utilizando `update_or_create`.

Se utilizaron 8 eventos de prueba:

1. Festival de Música Santiago
2. Campeonato de Fútbol
3. Festival de Rock
4. Feria Tecnológica
5. Concierto Nacional
6. Festival de Cine
7. Evento de Gaming
8. Stand Up Comedy

Cada evento posee una encuesta con cuatro alternativas:

* Excelente
* Bueno
* Regular
* Malo

Los datos fueron utilizados para realizar pruebas de funcionamiento y demostrar el comportamiento del sistema.

---

## 8. Panel de administración

Django Admin permite administrar los principales datos del sistema.

Desde:

```text
/admin/
```

se pueden gestionar los eventos, encuestas y alternativas.

También se creó un usuario administrador para realizar las pruebas de administración.

---

## 9. Configuración del entorno

El proyecto fue desarrollado utilizando un entorno virtual de Python:

```text
.venv
```

Python utilizado:

```text
Python 3.11.9
```

Django utilizado:

```text
Django 5.2.17
```

Las dependencias del proyecto se encuentran en:

```text
requirements.txt
```

---

## 10. Instalación local

Crear y activar el entorno virtual:

```powershell
python -m venv .venv
```

Activar:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

Aplicar migraciones:

```powershell
python manage.py migrate
```

Crear un superusuario:

```powershell
python manage.py createsuperuser
```

Ejecutar el servidor:

```powershell
python manage.py runserver
```

El proyecto estará disponible localmente en:

```text
http://127.0.0.1:8000/
```

---

## 11. Variables de entorno

Para producción se utilizan variables de entorno para evitar almacenar información sensible directamente en el código.

Entre ellas:

```text
DJANGO_DEBUG
DJANGO_SECRET_KEY
DJANGO_ALLOWED_HOSTS
DJANGO_CSRF_TRUSTED_ORIGINS
DATABASE_URL
```

La configuración permite utilizar SQLite durante el desarrollo local y PostgreSQL en producción.

---

## 12. Base de datos

### Desarrollo

Durante el desarrollo local se utiliza:

```text
SQLite
```

### Producción

En producción se utiliza:

```text
PostgreSQL
```

La conexión a la base de datos se gestiona mediante `dj-database-url`.

Esto permite que el proyecto utilice una base de datos PostgreSQL proporcionada por el servicio de hosting.

---

## 13. Despliegue

El proyecto fue desplegado utilizando Railway.

La aplicación se ejecuta mediante Gunicorn utilizando:

```text
web: gunicorn config.wsgi:application
```

Archivo utilizado:

```text
Procfile
```

La aplicación se encuentra publicada en:

```text
https://proyectobackend-production-6c46.up.railway.app
```

El proyecto utiliza HTTPS en producción.

---

## 14. Archivos estáticos

Para administrar los archivos estáticos en producción se utiliza WhiteNoise.

Configuración principal:

```python
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
```

Se ejecutó:

```powershell
python manage.py collectstatic --noinput
```

para preparar los archivos estáticos para producción.

---

## 15. Seguridad y producción

La configuración de producción utiliza:

* `DEBUG=False`
* Variable de entorno para `SECRET_KEY`
* `ALLOWED_HOSTS`
* `CSRF_TRUSTED_ORIGINS`
* HTTPS
* PostgreSQL
* Gunicorn
* WhiteNoise

La configuración CSRF permite realizar correctamente las solicitudes POST desde el dominio de producción.

---

## 16. Pruebas realizadas

Se realizaron pruebas de:

* Inicio del servidor Django.
* Comprobación del proyecto mediante `manage.py check`.
* Aplicación de migraciones.
* Creación de superusuario.
* Acceso al panel de administración.
* Visualización de eventos.
* Visualización del detalle de eventos.
* Visualización de imágenes.
* Visualización de encuestas.
* Envío de votos mediante POST.
* Protección CSRF.
* Visualización de resultados.
* Cálculo de porcentajes.
* Caso sin votos.
* Uso de datos de prueba.
* Funcionamiento de la aplicación desplegada en Railway.
* Conexión con PostgreSQL en producción.
* Acceso mediante HTTPS.

---

## 17. Uso de Inteligencia Artificial

Se utilizó Inteligencia Artificial como herramienta de apoyo durante el desarrollo del proyecto.

La IA fue utilizada principalmente para:

* Orientación sobre la estructura de Django.
* Explicación de conceptos de Python y Django.
* Apoyo en la creación y corrección de modelos.
* Apoyo en la creación de vistas y templates.
* Orientación para configurar imágenes con Pillow.
* Apoyo en la creación de encuestas y resultados.
* Corrección del cálculo de porcentajes.
* Orientación para configurar variables de entorno.
* Apoyo durante el despliegue en Railway.
* Diagnóstico de errores.
* Elaboración de documentación.
* Generación y organización de datos de prueba.

La implementación, ejecución de comandos, pruebas y validación final fueron realizadas sobre el proyecto.

---

## 18. Control de versiones

El proyecto utiliza Git para el control de versiones y GitHub como repositorio remoto.

Repositorio:

```text
https://github.com/Tiocore/proyectobackend
```

Los avances importantes fueron registrados mediante commits y enviados al repositorio remoto utilizando:

```powershell
git add .
git commit -m "mensaje"
git push
```

---

## 19. Cumplimiento de la rúbrica

El proyecto contempla los 12 indicadores evaluados:

1. Variables y operaciones.
2. Instrucciones, estructuras y operadores.
3. Utilización de paquetes externos.
4. Aplicación desarrollada con Django.
5. Arquitectura MVT/MVC.
6. Configuración del entorno Django.
7. Utilización de modelos.
8. Views y templates.
9. Tecnologías del lado del servidor.
10. Uso documentado de Inteligencia Artificial.
11. Generación y utilización de datos de prueba con apoyo de IA.
12. Protocolos, hosting y dominio/acceso web.

La evidencia y explicación de cada indicador se encuentran en:

```text
RUBRICA_BACKEND_Y_DOCUMENTACION_IA.txt
```

---

## 20. Estado final

El proyecto se encuentra funcional tanto en desarrollo local como en producción.

Actualmente permite gestionar eventos, mostrar información e imágenes, realizar encuestas, registrar votos, calcular porcentajes y consultar resultados.

La aplicación se encuentra desplegada mediante Railway, utiliza PostgreSQL en producción y dispone de acceso mediante HTTPS.

Repositorio:

```text
https://github.com/Tiocore/proyectobackend
```

Aplicación:

```text
https://proyectobackend-production-6c46.up.railway.app
```
