"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from rent_db.models import CondoFeesType
import warnings


class CondoFeesTypeModelTest(TestCase):
    """
    共益費種別モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_is_money(self):
        self.assertFalse(CondoFeesType.objects.get(pk=0).is_money)
        self.assertTrue(CondoFeesType.objects.get(pk=10).is_money)
        self.assertFalse(CondoFeesType.objects.get(pk=20).is_money)
        self.assertFalse(CondoFeesType.objects.get(pk=21).is_money)
        self.assertFalse(CondoFeesType.objects.get(pk=30).is_money)
