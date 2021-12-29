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
from rent_db.models import Building


class NonResidentialBuildingListViewSetTest(TestCase):
    """
    非居住用建物リストビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()
        self.company = Company.objects.get(pk=settings.COMPANY_ID)

    def test_get_view_set(self):
        url = reverse(
            'search_non_residential_buildings',
            args=[
                self.company.api_key,
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['building_name'], '表示項目確認用マンション')

    def test_get_view_set_with_city(self):
        url = reverse(
            'search_non_residential_buildings',
            args=[
                self.company.api_key,
            ],
        )
        url += "?city=26105"      # 京都市東山区
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['building_name'], 'サンプルテナントビル01')

    def test_get_view_set_with_area(self):
        url = reverse(
            'search_non_residential_buildings',
            args=[
                self.company.api_key,
            ],
        )
        url += "?area=26051"      # 祇園
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['building_name'], 'サンプルテナントビル01')
