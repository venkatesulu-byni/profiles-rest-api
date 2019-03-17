from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """docstring for HelloSerialize."""
    name = serializers.CharField(max_length=10)
