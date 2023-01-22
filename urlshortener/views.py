from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


import pyshorteners
import json

# Create your views here.

def decode_url(request, url):

    shortener = pyshorteners.Shortener()
    shortened_url = shortener.chilpit.short(f'{url}')
    data_to_dump = {
        'original_url': url,
        'shortened_url': shortened_url,
    }
    print(shortened_url)
    return HttpResponse(json.dumps(data_to_dump), content_type='application/json')

def encode_url(request, url):

    shortener = pyshorteners.Shortener()
    expanded_url = shortener.chilpit.expand(f'{url}')
    data_to_dump = {
        'original_url': url,
        'expanded_url': expanded_url,
    }
    return HttpResponse(json.dumps(data_to_dump), content_type='application/json')
