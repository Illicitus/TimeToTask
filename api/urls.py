from django.conf.urls import url
from api.views import Reverse, WordCounts


urlpatterns = [
    url('string-operations/reverses/$', Reverse.as_view(), name='reverse'),
    url('string-operations/word-counts/$', WordCounts.as_view(), name='word_counts'),
]
