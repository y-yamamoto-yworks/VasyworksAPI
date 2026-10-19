"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.conf import settings
from django.test import Client
from django.urls import reverse
import warnings
from rent_db.models import Company


class InternetTypeViewSetTest(TestCase):
    """
    インターネット種別ビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()
        self.company = Company.objects.get(pk=settings.COMPANY_ID)

    def test_get_view_set(self):
        url = reverse(
            'master_internet_types',
        )
        response = self.client.get(url, HTTP_X_API_KEY=self.company.api_key)
        self.assertEqual(response.status_code, 200)
        data_list = response.data['list']
        self.assertEqual(data_list[0]['name'], 'インターネット無料')

        response_invalid = self.client.get(url, HTTP_X_API_KEY='AABBCCDDEEFF')
        self.assertEqual(response_invalid.status_code, 403)
