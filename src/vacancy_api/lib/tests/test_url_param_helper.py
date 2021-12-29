"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.conf import settings
from urllib.parse import urljoin
from django.http import QueryDict
import warnings
import os
from lib.url_param_helper import UrlParamHelper


class UrlParamHelperHelperTest(TestCase):
    """
    URLパラメータヘルパークラスのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

        query_string = 'u_rnt=55000'    # 賃料 int
        query_string += '&stn=1140,1150,1160'       # 駅 id_array
        query_string += '&grg=true'  # 駐車場有り bool
        query_string += '&north=35.011823'  # 緯度上限 float
        query_string += '&schl=1'  # 小学校区 id
        query_string += '&odr=rent'  # 並び順
        self.query_params = QueryDict(query_string)

    def test_get_param(self):
        self.assertIsNone(UrlParamHelper.get_param('l_rnt', self.query_params))
        self.assertEqual(UrlParamHelper.get_param('u_rnt', self.query_params), '55000')

    def test_get_int_param(self):
        self.assertIsNone(UrlParamHelper.get_int_param('l_rnt', self.query_params))
        self.assertEqual(UrlParamHelper.get_int_param('u_rnt', self.query_params), 55000)

    def test_get_id_param(self):
        self.assertIsNone(UrlParamHelper.get_id_param('h_schl', self.query_params))
        self.assertEqual(UrlParamHelper.get_id_param('schl', self.query_params), 1)

    def test_get_float_param(self):
        self.assertIsNone(UrlParamHelper.get_float_param('south', self.query_params))
        self.assertEqual(UrlParamHelper.get_float_param('north', self.query_params), float(35.011823))

    def test_get_id_array_param(self):
        self.assertIsNone(UrlParamHelper.get_id_array_param('city', self.query_params))
        self.assertEqual(UrlParamHelper.get_id_array_param(
            'stn', self.query_params),
            (1140, 1150, 1160)
        )

    def test_get_bool_param(self):
        self.assertFalse(UrlParamHelper.get_bool_param('bike', self.query_params))
        self.assertTrue(UrlParamHelper.get_bool_param('grg', self.query_params))

    def test_get_order_param(self):
        self.assertEqual(UrlParamHelper.get_order_param('odr', self.query_params), 'rent')
