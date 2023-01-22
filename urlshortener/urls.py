from django.urls import path

from . import views

urlpatterns = [
    path('decode/<path:url>', views.decode_url, name='decode-url'),
    path('encode/<path:url>', views.encode_url, name='encode-url'),
]
