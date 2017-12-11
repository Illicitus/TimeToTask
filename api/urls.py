from django.urls import path
from api.views import Reverse, WordCounts


urlpatterns = [
    path('string-operations/reverses/$', Reverse.as_view(), name='reverse'),
    path('string-operations/word-counts/$', WordCounts.as_view(), name='word_counts'),
]
