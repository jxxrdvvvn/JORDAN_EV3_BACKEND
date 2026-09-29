from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from core import views
from core.api_views import RegistroViewSet  # Asegúrate de haber creado core/api_views.py

# Configuración del Router de DRF para los Endpoints de la API
router = DefaultRouter()
router.register(r"registros", RegistroViewSet, basename="registro")

urlpatterns = [
    # Redirección raíz y Panel de Administración
    path("", lambda request: redirect("lista")),  # Redirige la raíz a /registros/
    path("admin/", admin.site.urls),

    # --- ENDPOINTS DE LA API RESTful (ES3) ---
    path("api/", include(router.urls)),                      # Genera automáticamente /api/registros/
    path("api/token/", obtain_auth_token, name="api_token"), # Endpoint para solicitar el Token

    # --- PANTALLAS HTML ORIGINALES (ES2) ---
    path("login/", views.vista_login, name="login"),
    path("logout/", views.vista_logout, name="logout"),
    path("registros/", views.lista, name="lista"),
    path("registros/crear/", views.crear, name="crear"),
    path("registros/<int:pk>/editar/", views.editar, name="editar"),
    path("registros/<int:pk>/eliminar/", views.eliminar, name="eliminar"),
]