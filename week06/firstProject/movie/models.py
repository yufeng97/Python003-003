from django.db import models


class Ratings(models.Model):
    star = models.CharField(max_length=1)
    comment = models.TextField()
    comment_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'ratings'
