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


class StaffViewSetTest(TestCase):
    """
    スタッフビューセットのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.client = Client()
        self.company = Company.objects.get(pk=settings.COMPANY_ID)

    def test_get_view_set(self):
        url = reverse(
            'company_staffs',
            args=[
                self.company.api_key,
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        staff_list = response.data['list']
        self.assertEqual(staff_list[0]['full_name'], '管理 太郎')

    def test_get_view_set_with_department(self):
        url = reverse(
            'company_staffs',
            args=[
                self.company.api_key,
                2,      # 賃貸管理部
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        staff_list = response.data['list']
        self.assertEqual(staff_list[0]['full_name'], '管理 太郎')
