from django.conf.urls import url
from rest_framework.documentation import include_docs_urls
from api.views import Reverse, WordCounts


urlpatterns = [
    url('string-operations/reverses/$', Reverse.as_view(), name='reverse'),
    url('string-operations/word-counts/$', WordCounts.as_view(), name='word_counts'),
    url(r'^docs/', include_docs_urls(title='API', public=False))
]
