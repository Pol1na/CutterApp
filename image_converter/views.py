import sys
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.http import HttpResponse, JsonResponse
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image as IMG


class ImageView(TemplateView):
    template_name = "image_converter.html"


def file_upload(request):
    if request.method == "POST" and request.FILES.get('file') != None:
        my_file = request.FILES.get('file')
        img_name = str(my_file).split('.')[0]
        global pk
        pk = Image.objects.create(name=img_name, upload=my_file).pk
        return HttpResponse('200')
    else:
        my_file = Image.objects.get(pk=pk)
        format = request.POST.get('formats')
        print(format)
        image = IMG.open(my_file.upload)
        image = image.convert('RGB')
        output = io.BytesIO()
        image.save(output, format=format, quality=85)
        output.seek(0)
        converted_img = InMemoryUploadedFile(file=output, content_type=f'image/{format}',
                                             field_name=None,
                                             name=f'f{my_file.name}.{format}',
                                             size=image.tell(),
                                             charset=sys.getsizeof(output), content_type_extra=None)
        print(converted_img)
        my_file.converted = converted_img
        my_file.save()
        return HttpResponse('200')
