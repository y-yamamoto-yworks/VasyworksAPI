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
from rent_db.models import Room


class RoomViewSetTest(TestCase):
    """
    部屋ビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()
        self.company = Company.objects.get(pk=settings.COMPANY_ID)
        self.room = Room.objects.get(pk=3)      # 表示項目確認用マンション DEMO1 号室

    def test_get_view_set(self):
        url = reverse(
            'room_detail',
            args=[
                self.company.api_key,
                self.room.oid,
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        room = response.data
        self.assertEqual(room['room_no'], self.room.room_no)
        self.assertEqual(room['building']['building_name'], self.room.building.building_name)
