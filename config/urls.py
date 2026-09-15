""
from django.contrib import admin
from django.urls import path
from restaurante import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('detalle/<int:id>/', views.detalle, name='detalle'),
]
