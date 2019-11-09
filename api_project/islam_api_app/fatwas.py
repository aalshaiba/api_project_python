from django.db import models
from rest_framework import serializers
from .models import Fatwas
from .models import Droosuae


class FatwaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatwas
        fields = ['title', 'url', 'muftee']


class DroosUAESerializer(serializers.ModelSerializer):
    class Meta:
        model = Droosuae
        fields = ['title', 'url', 'shaikh']
