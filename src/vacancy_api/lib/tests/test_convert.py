"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
import warnings
from lib.convert import *


class ConvertTest(TestCase):
    """
    コンバートライブラリのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

    def test_xstr(self):
        self.assertEqual(xstr(None), '')
        self.assertEqual(xstr(''), '')
        self.assertEqual(xstr('abc123'), 'abc123')
        self.assertEqual(xstr(12345), '12345')

    def test_xint(self):
        self.assertEqual(xint(None), 0)
        self.assertEqual(xint(0), 0)
        self.assertEqual(xint(12345), 12345)
        self.assertEqual(xint(-12345), -12345)
        self.assertEqual(xint('0'), 0)
        self.assertEqual(xint('012345'), 12345)
        self.assertEqual(xint('-012345'), -12345)
        self.assertEqual(xint('a12345'), 0)

    def test_xfloat(self):
        self.assertEqual(xfloat(None), 0)
        self.assertEqual(xfloat(0), 0)
        self.assertEqual(xfloat(1), 1)
        self.assertEqual(xfloat(1.5), 1.5)
        self.assertEqual(xfloat(-1), -1)
        self.assertEqual(xfloat(-1.5), -1.5)
        self.assertEqual(xfloat('0'), 0)
        self.assertEqual(xfloat('1'), 1)
        self.assertEqual(xfloat('1.5'), 1.5)
        self.assertEqual(xfloat('-1'), -1)
        self.assertEqual(xfloat('-1.5'), -1.5)
        self.assertEqual(xfloat('a123'), 0)

    def test_int_to_bool(self):
        self.assertEqual(int_to_bool(0), False)
        self.assertEqual(int_to_bool(1), True)
        self.assertEqual(int_to_bool(-1), True)
        self.assertEqual(int_to_bool('1'), True)
        self.assertEqual(int_to_bool('-1'), True)
        self.assertEqual(int_to_bool('a'), False)

