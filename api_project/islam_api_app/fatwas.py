from django.db import models
from rest_framework import serializers
from .models import Fatwas


class FatwaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatwas
        fields = ['title', 'url', 'muftee']
