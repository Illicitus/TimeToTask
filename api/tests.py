from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Statistics
from api.serializers import StringReverseSerializer
from api.middlewares import StatisticTrackingMiddleware

import datetime

from mock import Mock

from utils import reverse_string, word_counts


# Serializers block
class ApiSerializersTestCase(APITestCase):
    """
    Test case for api serializers.
    """

    # Create basic data for serializer testing
    serializer = StringReverseSerializer
    urls = [reverse('reverse'), reverse('word_counts')]
    valid_data = {'phrase': 'I love hamburgers'}
    invalid_data = {'foo': 'Some words'}

    def test_valid_serializer(self):

        # Checks serializer validation with correct data
        serializer = self.serializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):

        # Checks serializer validation with wrong data
        serializer = self.serializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())


# Views block
class ApiTestCase(APITestCase):
    """
    Test case for api views.
    """

    # Create basic data for view testing
    urls = [reverse('reverse'), reverse('word_counts')]
    data = {'phrase': 'I love hamburgers'}
    invalid_data = {'foo': 'Some words'}
    reverse_result = {'result': reverse_string(data['phrase'])}
    count_result = {'result': word_counts(data['phrase'])}

    def test_valid_request_data_format(self):

        # We can work only with json data format.
        # Checks if response is correct.
        object_count = 1

        # For each of url, check status code and object count
        for url in self.urls:
            response = self.client.post(url, self.data, format='json')

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(Statistics.objects.count(), object_count)
            self.assertTrue(Statistics.objects.get(url__exact=url))
            object_count += 1

    def test_invalid_request_data_format(self):

        # We can work only with json data format.
        # Checks if response status is unsupported media type.
        object_count = 1

        # For each of url, check status code and object count
        for url in self.urls:
            response = self.client.post(url, self.data)

            self.assertEqual(response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
            self.assertEqual(Statistics.objects.count(), object_count)
            self.assertTrue(Statistics.objects.get(url__exact=url))
            object_count += 1

    def test_client_success_response_from_reverse(self):
        # Checks correct response from 'reverse' url.

        response = self.client.post(self.urls[0], self.data, format='json')
        self.assertEqual(response.data, self.reverse_result)

    def test_client_success_response_from_word_counts(self):
        # Checks correct response from 'word_counts' url.

        response = self.client.post(self.urls[1], self.data, format='json')
        self.assertEqual(response.data, self.count_result)

    def test_client_fail_response_from_reverse(self):
        # Checks invalid response from 'reverse' url.

        response = self.client.post(self.urls[0], self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_client_fails_response_from_word_counts(self):
        # Checks invalid response from 'word_counts' url.

        response = self.client.post(self.urls[1], self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# Middlewares block
class ApiMiddlewaresTestCase(ApiTestCase):
    """
    Test case for api middlewares.
    """

    # Create basic data for middleware testing
    middleware = StatisticTrackingMiddleware()
    urls = [reverse('reverse'), reverse('word_counts')]

    # Use mock data for generate request
    request = Mock()

    def test_add_statistics_to_reverse_url(self):
        # Checks if statistics tracking middleware create correct object.
        # Request to 'reverse' url.

        self.request.path = self.urls[0]
        response = self.client.post(self.urls[0], self.data, format='json')
        self.middleware.process_response(self.request, response)

        self.assertEqual(Statistics.objects.all().count(), 1)

    def test_add_statistic_to_word_counts_url(self):
        # Checks if statistics tracking middleware create correct object.
        # Request to 'word_counts' url.

        self.request.path = self.urls[1]
        response = self.client.post(self.urls[1], self.data, format='json')
        self.middleware.process_response(self.request, response)

        self.assertEqual(Statistics.objects.all().count(), 1)

    def test_add_statistic_to_current_date(self):
        # Checks correct adding tracking information to existing object.
        # Request to 'reverse' and 'word_counts' urls.

        # For each of url, check updated statistic object
        for url in self.urls:

            self.request.path = url
            response = self.client.post(url, self.data, format='json')
            self.middleware.process_response(self.request, response)

            statistics = Statistics.objects.get(date__exact=datetime.date.today(),
                                                url__exact=url)
            self.assertEquals(statistics.access_count, 2)


# Utils block
class ApiUtilsTestCase(ApiTestCase):
    """
    Test case for api utils.
    """

    # Create basic data for utils testing
    phrase = 'Some kind of phrase'

    def test_reverse_string(self):
        # Checks if response is reversed request words.
        # Words in request and response have the same position number.

        result = reverse_string(self.phrase)
        self.assertEqual(result, 'emoS dnik fo esarhp')

    def test_word_counts(self):
        # Checks if response is count of request words.

        result = word_counts(self.phrase)
        self.assertEqual(result, 4)
