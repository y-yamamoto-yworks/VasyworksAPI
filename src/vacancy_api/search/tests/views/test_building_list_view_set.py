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


class BuildingListViewSetTest(TestCase):
    """
    居住用建物リストビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()
        self.company = Company.objects.get(pk=settings.COMPANY_ID)

    def test_get_view_set(self):
        url = reverse(
            'search_buildings',
            args=[
                self.company.api_key,
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['building_name'], 'サンプルマンション')

    def test_get_view_set_with_station(self):
        url = reverse(
            'search_buildings',
            args=[
                self.company.api_key,
            ],
        )
        url += "?stn=1210"      # 鞍馬口
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['building_name'], '表示項目確認用マンション')

    def test_get_view_set_with_city(self):
        url = reverse(
            'search_buildings',
            args=[
                self.company.api_key,
            ],
        )
        url += "?city=26102"      # 京都市上京区
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['building_name'], '表示項目確認用マンション')

    def test_get_view_set_with_area(self):
        url = reverse(
            'search_buildings',
            args=[
                self.company.api_key,
            ],
        )
        url += "?area=26018"      # 今出川
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['building_name'], '表示項目確認用マンション')

    def test_get_view_set_with_lat_lng(self):
        url = reverse(
            'search_buildings',
            args=[
                self.company.api_key,
            ],
        )
        url += "?north=35.049928&south=35.049926&east=135.76684&west=135.76682"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['building_name'], '表示項目確認用マンション')

    def test_get_view_set_with_upper_rent(self):
        url = reverse(
            'search_buildings',
            args=[
                self.company.api_key,
            ],
        )
        url += "?u_rnt=50000"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['building_name'], 'リストサンプルマンション1')

    def test_get_view_set_with_lower_rent(self):
        url = reverse(
            'search_buildings',
            args=[
                self.company.api_key,
            ],
        )
        url += "?l_rnt=65000"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['building_name'], '分譲賃貸サンプルマンション')

    def test_get_view_set_with_separate(self):
        url = reverse(
            'search_buildings',
            args=[
                self.company.api_key,
            ],
        )
        url += "?sep=true"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['building_name'], 'サンプルマンション')

    def test_get_view_set_with_pet(self):
        url = reverse(
            'search_buildings',
            args=[
                self.company.api_key,
            ],
        )
        url += "?pet=true"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['building_name'], '表示項目確認用マンション')

    def test_get_view_set_with_washstand(self):
        url = reverse(
            'search_buildings',
            args=[
                self.company.api_key,
            ],
        )
        url += "?wshstd=true"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        building_list = response.data['list']
        self.assertEqual(building_list[0]['building_name'], '分譲賃貸サンプルマンション')
