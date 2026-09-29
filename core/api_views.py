from rest_framework import viewsets
from .models import Registro
from .serializers import RegistroSerializer
from .permissions import SoloStaffBorra
from solucion import decidir  # Tu regla original de la ES1 sin reescribir

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.filter(eliminado=False).order_by("-fecha")
    serializer_class = RegistroSerializer
    permission_classes = [SoloStaffBorra]

    def perform_create(self, serializer):
        cantidad = serializer.validated_data.get("cantidad")
        estado = serializer.validated_data.get("estado")
        # El resultado se calcula a través de la regla de negocio
        resultado = decidir(cantidad, estado)
        serializer.save(resultado=resultado)

    def perform_update(self, serializer):
        cantidad = serializer.validated_data.get("cantidad", serializer.instance.cantidad)
        estado = serializer.validated_data.get("estado", serializer.instance.estado)
        # Se recalcula la regla al editar
        resultado = decidir(cantidad, estado)
        serializer.save(resultado=resultado)