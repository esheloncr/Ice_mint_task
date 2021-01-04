from django.db import models


class Url(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.URLField(null=False)

    def __str__(self):
        return self.url


class ParsingInfo(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content