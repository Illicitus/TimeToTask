from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import StringReverseSerializer

from utils import reverse_string, word_counts


class Reverse(APIView):
    """
    Accept POST request with JSON data and return JSON content with the string,
    where each word is reversed.
    """
    serializer_class = StringReverseSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        # Check if serializer is valid
        if serializer.is_valid():
            clear_data = serializer.validated_data

            # String reverses and return result
            reverse = reverse_string(clear_data.get('phrase'))
            result = {'result': reverse}

            return Response(result, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WordCounts(APIView):
    """
    Accept POST request with JSON data and return JSON content with the count of words
    in request phrase.
    """
    serializer_class = StringReverseSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        # Check if serializer is valid
        if serializer.is_valid():
            clear_data = serializer.validated_data

            # String reverses and return result
            count = word_counts(clear_data.get('phrase'))
            result = {'result': count}

            return Response(result, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
