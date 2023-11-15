from rest_framework import serializers


class CreateGoogleDocViewCreateSerializer(serializers.Serializer):
    """Сериализатор для ПОСТ запроса"""
    name = serializers.CharField(max_length=255)
    data = serializers.CharField()


