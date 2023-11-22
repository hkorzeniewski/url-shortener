# URL Shortener Documentation

## Introduction

The URL Shortener is a Django web application that provides two main functions: encoding a long URL to a short URL and decoding a short URL back to its original long URL. This is achieved using the pyshorteners library for URL shortening and caching with Django's cache framework.

## Functions

### 1. `encode_url(request, url)`

Encodes a long URL to a short URL with a shortened slug.

#### Parameters
- `request`: The Django request object.
- `url` (str): The original long URL to be encoded.

#### Response
- `JsonResponse`: A JSON response containing the original URL and the shortened URL.

#### Example
```python
# Request
POST /encode-url/

# Request Body
{
    "url": "https://www.example.com/long-url-to-be-shortened"
}

# Response
{
    "original_url": "https://www.example.com/long-url-to-be-shortened",
    "shortened_url": "https://short.url/abc123"
}
```

### 2. `decode_url(request, url)`

Decodes a short URL back to its original long URL.

#### Parameters
- `request`: The Django request object.
- `url` (str): The short URL to be decoded.

#### Response
- `JsonResponse`: A JSON response containing the short URL and the original URL.

#### Example
```python
# Request
POST /decode-url/

# Request Body
{
    "url": "https://short.url/abc123"
}

# Response
{
    "shortened_url": "https://short.url/abc123",
    "original_url": "https://www.example.com/long-url-to-be-shortened"
}
```

## Notes

- Both functions are decorated with `@csrf_exempt` to disable CSRF protection for simplicity.
- The shortening and expanding of URLs are handled using the pyshorteners library.
- Caching is implemented using Django's cache framework to improve performance by avoiding redundant API calls for the same URL.

Please note that this documentation assumes you have a Django web application set up and configured with the necessary dependencies, including pyshorteners. Ensure proper error handling and security measures are implemented before deploying this application in a production environment.
