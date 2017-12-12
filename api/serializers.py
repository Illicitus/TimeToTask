from rest_framework import serializers


class StringReverseSerializer(serializers.Serializer):
    """
    This serializer take phrase from request and validation in future.
    """

    phrase = serializers.CharField(allow_blank=True)
