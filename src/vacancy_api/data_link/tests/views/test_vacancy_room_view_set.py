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
from rent_db.models import Building


class VacancyRoomViewSetTest(TestCase):
    """
    空室ビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()
        self.company = Company.objects.get(pk=settings.COMPANY_ID)

    def test_get_view_set(self):
        url = reverse(
            'data_link_vacancy_rooms',
        )
        response = self.client.get(url, HTTP_X_API_KEY=self.company.api_key)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['room_no'], '101')
        self.assertEqual(building_list[0]['building']['building_name'], 'サンプルマンション')

        response_invalid = self.client.get(url, HTTP_X_API_KEY='AABBCCDDEEFF')
        self.assertEqual(response_invalid.status_code, 403)

    def test_get_view_set_only_residential(self):
        url = reverse(
            'data_link_vacancy_rooms',
        )
        url += "?only_res=true"
        response = self.client.get(url, HTTP_X_API_KEY=self.company.api_key)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['room_no'], '101')
        self.assertEqual(building_list[0]['building']['building_name'], 'サンプルマンション')

    def test_get_view_set_only_no_residential(self):
        url = reverse(
            'data_link_vacancy_rooms',
        )
        url += "?only_no_res=true"
        response = self.client.get(url, HTTP_X_API_KEY=self.company.api_key)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['room_no'], 'TENANT01')
        self.assertEqual(building_list[0]['building']['building_name'], '表示項目確認用マンション')
