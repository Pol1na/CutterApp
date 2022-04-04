from django.urls import path

from .views import *

urlpatterns = [
    path('', ImageView.as_view(), name='image'),
    path('upload', file_upload, name='upload-file'),
    #path('convert', file_convert, name='convert-file'),

]
