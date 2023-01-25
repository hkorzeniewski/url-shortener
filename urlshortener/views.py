from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.cache import cache


from rest_framework.decorators import api_view
from rest_framework.response import Response

import pyshorteners
import json
import redis


redis_instance = redis.StrictRedis(settings.REDIS_URL, db=0)
# Create your views here.

# @api_view(['POST'])
@csrf_exempt
def encode_url(request, url):
    
    shortened_url = redis_instance.get(url).decode("utf-8")
    if shortened_url is None:
        shortener = pyshorteners.Shortener()
        shortened_url = shortener.chilpit.short(f'{url}')
        redis_instance.set(url, shortened_url)    
    data_to_dump = {
        'original_url': url,
        'shortened_url': shortened_url,
    }
    # print(shortened_url)
    return HttpResponse(json.dumps(data_to_dump), content_type='application/json')



@csrf_exempt
def decode_url(request, url):

    original_url = redis_instance.get(url).decode("utf-8")
    if original_url is None:
        shortener = pyshorteners.Shortener()
        original_url = shortener.chilpit.expand(f'{url}')
        redis_instance.set(url, original_url)

    data_to_dump = {
        'shortened_url': url,
        'original_url': original_url,
    }
    return HttpResponse(json.dumps(data_to_dump), content_type='application/json')
