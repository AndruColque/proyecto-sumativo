from django.urls import path

from restaurante import views

app_name = 'app'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('detalle/<int:id>/', views.detalle, name='detalle'),
]
