from django.urls import path
from . import views

urlpatterns = [
    path('', views.ImagemViewSet.as_view(), name='lista-imagens')
]