from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Todo lo que empiece por api/v1/ se va a las rutas de la API
    path('api/v1/', include('logistica.urls')),
    
    # 2. Las rutas web directas (como /productos/) irán aquí
    path('', include('logistica.web_urls')), 
]