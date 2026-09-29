Plan de Trabajo e Integración RESTful - ES3

🎯 Objetivo General

Extender el proyecto Django desarrollado en la ES1 y ES2 mediante la implementación de una API RESTful robusta utilizando Django REST Framework (DRF), garantizando la compatibilidad con el frontend existente y reutilizando la lógica de negocio original (decidir()).

📋 Fases del Plan de Trabajo

Fase 1: Configuración de Dependencias y Entorno

[x] Configurar requirements.txt con django, djangorestframework, python-decouple y tabulate.

[x] Crear el script de automatización setup.bat para restauración de paquetes en entornos restringidos de laboratorio.

[x] Registrar 'rest_framework' y 'rest_framework.authtoken' en INSTALLED_APPS dentro de settings.py.

Fase 2: Autenticación y Seguridad

[x] Configurar la autenticación por token predeterminada en REST_FRAMEWORK de settings.py.

[x] Exigir la política global IsAuthenticated.

[x] Implementar la vista predefinida obtain_auth_token en /api/token/.

[x] Desarrollar la clase de permiso personalizado SoloStaffBorra en core/permissions.py (o api_views.py).

Fase 3: Serialización y Lógica de Negocio

[x] Crear RegistroSerializer en core/serializers.py.

[x] Integrar invocación automática a la función decidir() dentro de perform_create() en el ViewSet.

[x] Configurar RegistroViewSet exponiendo las operaciones CRUD completas.

Fase 4: Enrutamiento de la API

[x] Implementar DefaultRouter en core/urls.py o miproyecto/urls.py.

[x] Registrar la ruta /api/registros/ y mapear los endpoints de token.

Fase 5: Validación, Evidencias y Entrega

[x] Ejecutar suite de pruebas curl en CMD para obtener códigos de respuesta HTTP (200, 201, 401, 204).

[x] Almacenar las 5 capturas en la carpeta /pruebas.

[x] Limpiar la base de datos local db.sqlite3 y entornos virtuales.

[x] Generar documentación final (ia.md, README.md, plan.md).