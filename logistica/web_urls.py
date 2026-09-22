from django.urls import path
from .views import (
    dashboard_web,
    lista_productos_web,
)

urlpatterns = [
    path('', dashboard_web, name='dashboard'),
    path('productos/', lista_productos_web, name='lista_productos_web'),
]