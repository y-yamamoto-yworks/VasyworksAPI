"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from rent_db.models import Staff
import warnings


class StaffModelTest(TestCase):
    """
    スタッフモデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.staff = Staff.objects.get(pk=2)      # 管理 太郎

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_full_name(self):
        self.assertEqual(self.staff.full_name, '管理 太郎')

    def test_staff_name(self):
        self.assertEqual(self.staff.staff_name, '管理 太郎 (部署:賃貸管理部)')
