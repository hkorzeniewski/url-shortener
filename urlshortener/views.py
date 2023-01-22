from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


import pyshorteners
import json

# Create your views here.

def decode_url(request, url):

    shortener = pyshorteners.Shortener()
    shortened_url = shortener.chilpit.short(f'{url}')
    print(shortened_url)
    return HttpResponse(json.dumps(shortened_url), content_type='application/json')

def encode_url(request, url):

    shortener = pyshorteners.Shortener()
    expanded_url = shortener.chilpit.expand(f'{url}')
    return HttpResponse(json.dumps(expanded_url), content_type='application/json')
