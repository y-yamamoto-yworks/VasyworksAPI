"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from users.models import VacancyUser
import warnings


class VacancyUserModelTest(TestCase):
    """
    空室情報ユーザモデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.user = VacancyUser.objects.get(username='yworks')

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_full_name(self):
        self.assertEqual(self.user.full_name, 'ワイワークス不動産')

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), 'ワイワークス不動産')

    def test_get_short_name(self):
        self.assertEqual(self.user.get_short_name(), 'ワイワークス不動産')
