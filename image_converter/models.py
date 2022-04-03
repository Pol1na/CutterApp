from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse


class Image(models.Model):
    upload = models.ImageField(upload_to='media/upload_img',
                               validators=[FileExtensionValidator(['jpg', 'jpeg', 'png',
                                                                  'ico'])])
    converted = models.ImageField(upload_to='media/converted_img', null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def get_absolute_url(self):
        return reverse('convert', kwargs={"pk": self.pk})
