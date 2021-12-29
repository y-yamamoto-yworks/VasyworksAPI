"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from rent_db.models import Department
import warnings


class DepartmentModelTest(TestCase):
    """
    部署モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_publish_staffs(self):
        staff = Department.objects.get(pk=2).publish_staffs.first()
        self.assertEqual(staff.full_name, '管理 太郎')
