Declaración de Uso de Inteligencia Artificial - ES3

1. Descripción del Proyecto y Alcance

En esta Evaluación Sumativa 3 (ES3), se integró Django REST Framework (DRF) sobre el proyecto base desarrollado en la ES1 y ES2. Se implementó una arquitectura de API RESTful con autenticación basada en tokens, control de acceso mediante permisos personalizados y la integración automática de la lógica de negocio decidir().

2. Herramientas de IA Utilizadas

Modelo de Lenguaje / Asistente Virtual: Asistencia interactiva durante el desarrollo y depuración.

3. Prompts Clave Utilizados

Configuración de DRF: "¿Cómo configurar REST_FRAMEWORK en settings.py para usar autenticación por Token y exigir IsAuthenticated de manera global?"

Persistencia de Lógica de Negocio: "¿Cómo sobrescribir perform_create en un ViewSet de DRF para ejecutar decidir() automáticamente al guardar?"

Permisos Personalizados: "Crea una clase de permisos personalizada SoloStaffBorra que restrinja el método DELETE exclusivamente a usuarios is_staff."

Resolución de Errores en Laboratorio: "Solución a ModuleNotFoundError: No module named 'tabulate' al ejecutar python manage.py migrate en entorno de laboratorio restringido."

Comandos cURL: "Genera los comandos cURL compatibles con Windows CMD y PowerShell para probar Token, GET, POST y DELETE."

4. Validación y Pruebas

Todas las respuestas y códigos generados por la IA fueron validados manualmente en el entorno local mediante:

Comandos python manage.py check y python manage.py migrate.

Pruebas de integración con curl.exe en CMD verificando códigos de estado HTTP (200 OK, 201 Created, 401 Unauthorized, 204 No Content).

Verificación del comportamiento del frontend de ES2 y compatibilidad total con la lógica original de la ES1.