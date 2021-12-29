"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from rent_db.models import DepositNotation
import warnings


class DepositNotationModelTest(TestCase):
    """
    保証金表記モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_is_money(self):
        self.assertFalse(DepositNotation.objects.get(pk=0).is_money)
        self.assertFalse(DepositNotation.objects.get(pk=1).is_money)
        self.assertTrue(DepositNotation.objects.get(pk=2).is_money)
        self.assertFalse(DepositNotation.objects.get(pk=3).is_money)
        self.assertFalse(DepositNotation.objects.get(pk=4).is_money)
        self.assertFalse(DepositNotation.objects.get(pk=5).is_money)
        self.assertFalse(DepositNotation.objects.get(pk=6).is_money)

    def test_is_month(self):
        self.assertFalse(DepositNotation.objects.get(pk=0).is_month)
        self.assertFalse(DepositNotation.objects.get(pk=1).is_month)
        self.assertFalse(DepositNotation.objects.get(pk=2).is_month)
        self.assertTrue(DepositNotation.objects.get(pk=3).is_month)
        self.assertFalse(DepositNotation.objects.get(pk=4).is_month)
        self.assertFalse(DepositNotation.objects.get(pk=5).is_month)
        self.assertFalse(DepositNotation.objects.get(pk=6).is_month)

    def test_is_rate(self):
        self.assertFalse(DepositNotation.objects.get(pk=0).is_rate)
        self.assertFalse(DepositNotation.objects.get(pk=1).is_rate)
        self.assertFalse(DepositNotation.objects.get(pk=2).is_rate)
        self.assertFalse(DepositNotation.objects.get(pk=3).is_rate)
        self.assertTrue(DepositNotation.objects.get(pk=4).is_rate)
        self.assertFalse(DepositNotation.objects.get(pk=5).is_rate)
        self.assertFalse(DepositNotation.objects.get(pk=6).is_rate)
