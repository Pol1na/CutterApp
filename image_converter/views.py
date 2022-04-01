from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.http import HttpResponse, JsonResponse


class ImageView(TemplateView):
    template_name = "image_converter.html"


def file_upload(request):
    if request.method == "POST":
        my_file = request.FILES.get('file')
        Image.objects.create(upload=my_file)
        return HttpResponse('')
