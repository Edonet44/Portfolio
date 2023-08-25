from rest_framework import serializers
from .contatti import Contatti



class ContattiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contatti
        fields = '__all__'
