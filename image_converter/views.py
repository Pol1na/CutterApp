from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.http import HttpResponse, JsonResponse
import io
from PIL import Image
from django.core.files.base import ContentFile

class ImageView(TemplateView):
    template_name = "image_converter.html"


def file_upload(request):

    if request.method == "POST":
        my_file = request.FILES.get('file')
        image = Image.open(my_file.file)
        answer = request.POST.get('formats')
        image_bytes = io.BytesIO()
        image.save(fp=image_bytes, format=answer)
        image_content_file = ContentFile(content=image_bytes.getvalue())
        Image.objects.create(upload=my_file)
        return HttpResponse('200')

def file_convert(request):
    if request.method == 'POST':


# def convert_file(request):

