from rest_framework import serializers
from .models import Visualization, Download


class VisualizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visualization
        fields = [
            'id',
            'datetime',
            'image',
            'user'
        ]


class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = [
            'id',
            'datetime',
            'image',
            'user'
        ]
