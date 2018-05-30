from __future__ import unicode_literals

from django.db import models

# Create your models here.


class FileUpload(models.Model):

    attachment_file = models.FileField(upload_to='static/%Y/%m/%d',blank=True)
    name = models.CharField("Name", max_length=300,blank=True)
    created = models.DateTimeField(auto_now_add=True,blank=True)

    def __unicode__(self):
        return str(self.id)