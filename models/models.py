from django.db import models


class SearchResult(models.Model):
    event_title = models.CharField(max_length=60)
    event_link = models.CharField()
    description = models.CharField()
