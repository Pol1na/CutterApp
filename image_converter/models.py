from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse


class Image(models.Model):
    name = models.CharField(max_length=400, null= True)
    upload = models.ImageField(upload_to='media/upload_img',
                               validators=[FileExtensionValidator(['jpg', 'jpeg', 'png',
                                                                  'ico'])])
    converted = models.ImageField(upload_to='media/converted_img', null=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def get_absolute_url(self):
        return reverse('converted', kwargs={"pk": self.pk})
