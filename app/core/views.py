from rest_framework import generics
from .serializers import ImagemSerializer
from .models import Imagem

class ImagemViewSet(generics.ListCreateAPIView):

    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer