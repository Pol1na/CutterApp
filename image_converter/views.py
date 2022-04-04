from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.http import HttpResponse, JsonResponse
import io
from django.core.files.uploadedfile import InMemoryUploadedFile

from PIL import Image as IMG
from django.core.files.base import ContentFile


class ImageView(TemplateView):
    template_name = "image_converter.html"


def file_upload(request):
    if request.method == "POST" and request.FILES.get('file') != None:
        my_file = request.FILES.get('file')
        img_name = str(my_file).split('.')[0]
        global pk
        pk = Image.objects.create(name=img_name,upload=my_file).pk
        return HttpResponse('200')
    else:
        my_file = Image.objects.get(pk=pk)
        converted_img = create_image(my_file.upload, request.POST.get('formats'), name=my_file.name)
        my_file.converted = converted_img
        my_file.save()
            # image = IMG.open(my_file.upload)
        # answer = request.POST.get('formats')
        # if answer == "JPEG":
        #     image = image.convert("RGB")
        # image_bytes = io.BytesIO()
        # image.save(filename='asdasd',fp=image_bytes, format=answer)
        # print(image)
        # image_content_file = ContentFile(content=image.tobytes())
        # print(image_content_file)
        # my_file.converted = image_content_file
        # my_file.name = "asdasdasda"
        # my_file.save()
        # print(my_file.converted)
        return HttpResponse('200')

def create_image(image_field, format, name=None):
    """
    Resizes an image from a Model.ImageField and returns a new image as a ContentFile
    """

    img = IMG.open(image_field)
    if format == "JPEG":
        img = img.convert("RGB")
    buffer = io.BytesIO()
    img.save(fp=buffer, format=format)
    return ContentFile(buffer.getvalue())

# def file_convert(request):
#     if request.method == 'GET':
#         print('here')
#         my_file = Image.objects.get(upload=request.FILES.get('file'))
#         image = IMG.open(my_file.file)
#         answer = request.GET.get('formats')
#         image_bytes = io.BytesIO()
#         image.save(fp=image_bytes, format=answer)
#         image_content_file = ContentFile(content=image_bytes.getvalue())
#         Image.objects.update(upload=request.FILES.get('file'), convert=image_content_file)

# def convert_file(request):
