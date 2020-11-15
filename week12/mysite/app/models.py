from django.db import models


# Create your models here.
class ZdmPhone(models.Model):
    brand = models.CharField(max_length=100, blank=True, null=True)
    article_title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'zdm_phone'


class PhoneComment(models.Model):
    article = models.ForeignKey('ZdmPhone', models.DO_NOTHING, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField()
    datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone_comment'
