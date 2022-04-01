from django.db import models


class Image(models.Model):
    upload = models.ImageField(upload_to='media/upload_img')

    def __str__(self):
        return str(self.pk)
