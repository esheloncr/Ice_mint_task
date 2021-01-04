from rest_framework import serializers
from . import models


class UrlSerialize(serializers.ModelSerializer):
    class Meta:
        model = models.Url
        fields = ("url",)