from rest_framework import serializers
from .models import Label, ImageTag


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = [
            'id',
            'tag_name'
        ]


class ImageTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTag
        fields = [
            'id',
            'image',
            'label'
        ]
