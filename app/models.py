from django.db import models


class GoodReadsAudit(models.Model):
    """ GoodReadsAudit data save here"""

    title            = models.CharField(max_length=50, null=True)
    average_rating   = models.CharField(max_length=50, null=True)
    ratings_count    = models.CharField(max_length=50, null=True)
    num_pages        = models.CharField(max_length=50, null=True)
    image_url        = models.CharField(max_length=50, null=True)
    publication_year = models.CharField(max_length=50, null=True)
    authors          = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title
        