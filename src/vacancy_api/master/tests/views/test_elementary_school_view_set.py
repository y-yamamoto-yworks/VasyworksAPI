"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.conf import settings
from django.test import Client
from django.urls import reverse
import warnings
from rent_db.models import Company


class ElementarySchoolViewSetTest(TestCase):
    """
    小学校区ビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()
        self.company = Company.objects.get(pk=settings.COMPANY_ID)

    def test_get_view_set(self):
        url = reverse(
            'master_elementary_schools',
            args=[
                self.company.api_key,
                '26101',  # 京都市北区
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data_list = response.data['list']
        self.assertEqual(data_list[0]['name'], '大宮')
