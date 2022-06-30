from django.test import TestCase
from django.urls import resolve

from boards.views import create


class TestUrls(TestCase):
    def test_create_url_is_resolved(self):
        url = resolve('/board/create')
        self.assertEqual(url.func,create) #url.func로 저 url에 맵핑되어있는 함수를 가져옴, 그리고 우측에 있는 저 함수와 같은지 비교 (Equal)

