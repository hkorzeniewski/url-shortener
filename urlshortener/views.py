import json

import pyshorteners
import redis
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def encode_url(request, url):
    """
    Encodes long url to short url with shortened slug
    Gets url as a parameter and returns JsonResponse with original url and shortened url
    """
    shortened_url = cache.get(url)
    if shortened_url is None:
        shortener = pyshorteners.Shortener()
        shortened_url = shortener.chilpit.short(f"{url}")
        cache.set(url, shortened_url)
    data_to_dump = {
        "original_url": url,
        "shortened_url": shortened_url,
    }
    return JsonResponse(data_to_dump)


@csrf_exempt
def decode_url(request, url):
    """
    Decodes short url to original long url
    Gets url as a parameter and returns JsonResponse with original url and shortened url
    """
    original_url = cache.get(url)
    if original_url is None:
        shortener = pyshorteners.Shortener()
        original_url = shortener.chilpit.expand(f"{url}")
        cache.set(url, original_url)

    data_to_dump = {
        "shortened_url": url,
        "original_url": original_url,
    }
    return JsonResponse(data_to_dump)
