"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
import warnings
from lib.functions import *


class FunctionsTest(TestCase):
    """
    関数ライブラリのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

    def test_get_unique_filename(self):
        self.assertRegex(get_unique_filename('sample.jpg'), '\.jpg$')
        self.assertRegex(get_unique_filename('sample.pdf'), '\.pdf$')

    def test_base64_decode_id(self):
        self.assertEqual(base64_decode_id(0), 'MA')
        self.assertEqual(base64_decode_id(1), 'MQ')

    def test_base64_encode_id(self):
        self.assertEqual(base64_encode_id('MA'), 0)
        self.assertEqual(base64_encode_id('MQ'), 1)
        self.assertEqual(base64_encode_id('AB'), 0)

    def test_float_normalize(self):
        self.assertEqual(float_normalize(0), '0')
        self.assertEqual(float_normalize(11), '11')
        self.assertEqual(float_normalize(11.0), '11')
        self.assertEqual(float_normalize(11.1), '11.1')
        self.assertEqual(float_normalize(11.10), '11.1')
        self.assertEqual(float_normalize(11.11), '11.11')

