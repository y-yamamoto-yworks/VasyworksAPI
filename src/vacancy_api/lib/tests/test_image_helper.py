"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.conf import settings
import warnings
import os
import shutil
from lib.image_helper import ImageHelper


class ImageHelperTest(TestCase):
    """
    画像ヘルパークラスのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

    def test_cache_image(self):
        src_path = os.path.join(settings.MEDIA_ROOT, 'test_data', 'sample_picture.jpg')
        cache_test_dir = os.path.join(settings.CACHE_FILE_DIR, 'test_data')
        os.makedirs(cache_test_dir)
        cache_path = os.path.join(cache_test_dir, 'cache_test_picture.jpg')
        ImageHelper.cache_image(src_path, cache_path, 'YWorks', settings.MEDIUM_IMAGE_SIZE)
        self.assertTrue(os.path.exists(cache_path))
        shutil.rmtree(cache_test_dir)

    def test_make_qrcode(self):
        dest = os.path.join(settings.MEDIA_ROOT, 'test_data', 'qrcode_test.jpg')
        ImageHelper.make_qrcode('QR Code Test', dest)
        self.assertTrue(os.path.exists(dest))
        os.remove(dest)
        self.assertFalse(os.path.exists(dest))
