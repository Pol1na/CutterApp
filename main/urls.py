from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),

    # path('video/', Index.as_view(), name='video')
    # path('audio/', Index.as_view(), name='audio')
    # path('document/', Index.as_view(), name='document')
    # path('archive/', Index.as_view(), name='archive')
]