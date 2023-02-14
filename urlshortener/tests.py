import json
from urllib import response

import pyshorteners
from django.core.cache import cache
from django.test import TestCase
from django_fakeredis import FakeRedis

# Create your tests here.


class EncodingTest(TestCase):
    def setUp(self) -> None:
        shortener = pyshorteners.Shortener()
        self.url_to_encode = "test"
        self.shortened_url = shortener.clckru.short(f"{self.url_to_encode}")
        self.response_without_url = self.client.get("http://localhost:8000/encode/")
        self.response_with_url = self.client.get(
            f"http://localhost:8000/encode/{self.url_to_encode}"
        )
        self.data = json.loads(self.response_with_url.content)

        return super().setUp()

    def test_encode_without_url_endpoint(self):
        self.assertEqual(self.response_without_url.status_code, 404)

    def test_encode_with_url_endpoint(self):
        self.assertEqual(self.response_with_url.status_code, 200)

    def test_key_values_in_response(self):
        self.assertEqual("original_url" in self.data, True)
        self.assertEqual("shortened_url" in self.data, True)

    def test_is_correct_shortened(self):
        self.assertEqual(self.data["shortened_url"], self.shortened_url)

    def test_is_original_shortened(self):
        self.assertEqual(self.data["original_url"], self.url_to_encode)

    def test_is_encoded_cached_data(self):
        cached_data = cache.get(self.url_to_encode)
        self.assertEqual(cached_data, self.data["shortened_url"])


class DecodingTest(TestCase):
    def setUp(self) -> None:
        shortener = pyshorteners.Shortener()
        self.url_to_decode = "https://clck.ru/0q"
        self.expanded_url = shortener.clckru.expand(f"{self.url_to_decode}")
        self.response_without_url = self.client.get("http://localhost:8000/decode/")
        self.response_with_url = self.client.get(
            f"http://localhost:8000/decode/{self.url_to_decode}"
        )
        self.data = json.loads(self.response_with_url.content)

        return super().setUp()

    def test_decode_without_url_endpoint(self):
        self.assertEqual(self.response_without_url.status_code, 404)

    def test_decode_endpoint_works(self):
        self.assertEqual(self.response_with_url.status_code, 200)

    def test_key_values_in_response(self):
        self.assertTrue("original_url" in self.data)
        self.assertTrue("shortened_url" in self.data)

    def test_is_correct_shortened(self):
        self.assertEqual(self.data["original_url"], self.expanded_url)

    def test_is_original_shortened(self):
        self.assertEqual(self.data["shortened_url"], self.url_to_decode)

    def test_is_encoded_cached_data(self):
        cached_data = cache.get(self.url_to_decode)
        self.assertEqual(cached_data, self.data["original_url"])
