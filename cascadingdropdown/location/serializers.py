from rest_framework import serializers

from .models import Village

class VillageModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Village
        fields = ['pk', 'name',]