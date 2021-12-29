"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.conf import settings
from urllib.parse import urljoin
import warnings
import os
from lib.api_helper import ApiHelper


class ApiHelperTest(TestCase):
    """
    APIヘルパークラスのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

    def test_check_key(self):
        self.assertTrue(ApiHelper.check_key('107a0f11c12c465891ab47b39ea15e30'))
        self.assertFalse(ApiHelper.check_key('753099815daf45ab993d0ecbe0e9b05f'))
