from rest_framework import serializers
from .blog import Categoria, Post

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'  # Puoi specificare i campi desiderati invece di '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # Puoi specificare i campi desiderati invece di '__all__'
