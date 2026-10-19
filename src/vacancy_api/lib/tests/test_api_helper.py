"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.conf import settings
from urllib.parse import urljoin
from django.test import RequestFactory
import warnings
import os
from lib.api_helper import ApiHelper
from rent_db.models import Company


class ApiHelperTest(TestCase):
    """
    APIヘルパークラスのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

    def test_check_key(self):
        factory = RequestFactory()
        company = Company.objects.get(pk=settings.COMPANY_ID)

        request_valid = factory.get('/', HTTP_X_API_KEY=company.api_key)
        self.assertTrue(ApiHelper.check_key(request_valid))

        request_invalid = factory.get('/', HTTP_X_API_KEY='AABBCCDDEEFF')
        self.assertFalse(ApiHelper.check_key(request_invalid))

        request_no_header = factory.get('/')
        self.assertFalse(ApiHelper.check_key(request_no_header))