from rest_framework import viewsets
from .blog import Categoria, Post
from .serializers import CategoriaSerializer, PostSerializer

class CategoriaApiViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PostViewApiSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
