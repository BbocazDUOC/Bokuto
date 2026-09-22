from rest_framework import viewsets
from .models import Producto, LoteStock, Merma, Movimiento
from django.shortcuts import render
from .serializers import (
    ProductoSerializer, 
    LoteStockSerializer, 
    MermaSerializer, 
    MovimientoSerializer
)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'codigo_interno'

class LoteStockViewSet(viewsets.ModelViewSet):
    queryset = LoteStock.objects.all()
    serializer_class = LoteStockSerializer
    ordering = ['fecha_vencimiento']

class MermaViewSet(viewsets.ModelViewSet):
    queryset = Merma.objects.all()
    serializer_class = MermaSerializer

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
    
def dashboard_web(request):
    return render(request, 'dashboard.html')

def lista_productos_web(request):
    return render(request, 'lista_productos.html')
