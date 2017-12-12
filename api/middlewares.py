from django.urls import reverse_lazy

from api.models import Statistics

import datetime


class StatisticTrackingMiddleware(object):
    """
    This middleware check if client send request to 'word_counts' or 'reverse' urls
    and add access count of requests per date to each of them.
    Information add to Statistics model and you can see it in admin panel.
    """
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(StatisticTrackingMiddleware, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)

        return response

    @staticmethod
    def process_response(request, response):
        if request.path == reverse_lazy('word_counts') or request.path == reverse_lazy('reverse'):
            obj, created = Statistics.objects.get_or_create(date__exact=datetime.date.today(), url=request.path)
            obj.access_count += 1
            obj.save()

        return response
