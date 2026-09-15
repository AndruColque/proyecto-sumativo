""
from django.contrib import admin
from django.urls import include, path
from restaurante import views

app_urls = [
    path('', views.inicio, name='inicio'),
    path('detalle/<int:id>/', views.detalle, name='detalle'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((app_urls, 'app'), namespace='app')),
]
