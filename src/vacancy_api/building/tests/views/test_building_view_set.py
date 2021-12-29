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


class BuildingViewSetTest(TestCase):
    """
    建物ビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()
        self.company = Company.objects.get(pk=settings.COMPANY_ID)
        self.building = Building.objects.get(pk=2)      # 表示項目確認用マンション

    def test_get_view_set(self):
        url = reverse(
            'building_detail',
            args=[
                self.company.api_key,
                self.building.oid,
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        building = response.data
        self.assertEqual(building['building_name'], self.building.building_name)
