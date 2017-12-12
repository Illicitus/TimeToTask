from django.db import models


class Statistics(models.Model):
    """
    The class to keep an information about how many times each endpoint was
    accessed each day.
    """
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    access_count = models.IntegerField(default=0)
