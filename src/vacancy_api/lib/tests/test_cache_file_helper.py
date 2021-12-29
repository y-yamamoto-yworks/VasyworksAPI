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
from lib.cache_file_helper import CacheFileHelper


class CacheFileHelperTest(TestCase):
    """
    キャッシュファイルヘルパークラスのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.cache_file_url = urljoin(settings.BASE_URL, settings.CACHE_FILE_URL)

    def test_get_property_image_file_url(self):
        file_oid = '925bfcb584934673854b1bb94eeb157d'       # サンプルマンション
        org_file_name = '753099815daf45ab993d0ecbe0e9b05f.JPG'      # 建物外観画像
        cache_file_name = 'cache_test_image.jpg'
        url = CacheFileHelper.get_property_image_file_url(
            file_oid,
            org_file_name,
            cache_file_name,
            'YWorks',
            settings.MEDIUM_IMAGE_SIZE,
        )
        self.assertEqual(
            url,
            urljoin(self.cache_file_url, "./buildings/" + file_oid + "/" + cache_file_name),
        )
        cache_path = os.path.join(settings.CACHE_FILE_DIR, 'buildings', file_oid, cache_file_name)
        self.assertTrue(os.path.exists(cache_path))
        os.remove(cache_path)

    def test_get_property_panorama_file_url(self):
        file_oid = '925bfcb584934673854b1bb94eeb157d'       # サンプルマンション
        org_file_name = 'e29ea33fcb884b16b8b8357325539938.JPG'      # エントランスパノラマ
        cache_file_name = 'cache_test_panorama.jpg'
        url = CacheFileHelper.get_property_panorama_file_url(
            file_oid,
            org_file_name,
            cache_file_name,
        )
        self.assertEqual(
            url,
            urljoin(self.cache_file_url, './buildings/' + file_oid + '/' + cache_file_name),
        )
        cache_path = os.path.join(settings.CACHE_FILE_DIR, 'buildings', file_oid, cache_file_name)
        self.assertTrue(os.path.exists(cache_path))
        os.remove(cache_path)

    def test_get_property_movie_file_url(self):
        file_oid = '925bfcb584934673854b1bb94eeb157d'       # サンプルマンション
        org_file_name = '070c6698723b4383a77cd9701fb7e912.mp4'      # 屋内スペース動画
        cache_file_name = 'cache_test_move.mp4'
        url = CacheFileHelper.get_property_movie_file_url(
            file_oid,
            org_file_name,
            cache_file_name,
        )
        self.assertEqual(
            url,
            urljoin(self.cache_file_url, "./buildings/" + file_oid + "/" + cache_file_name),
        )
        cache_path = os.path.join(settings.CACHE_FILE_DIR, 'buildings', file_oid, cache_file_name)
        self.assertTrue(os.path.exists(cache_path))
        os.remove(cache_path)

    def test_get_building_file_url(self):
        file_oid = '925bfcb584934673854b1bb94eeb157d'   # サンプルマンション
        org_file_name = 'b1aeb2610b8e47ef99c66bfbd32f7d0f.pdf'      # 契約書
        cache_file_name = 'cache_test_file.pdf'
        url = CacheFileHelper.get_building_file_url(
            file_oid,
            org_file_name,
            cache_file_name,
        )
        self.assertEqual(
            url,
            urljoin(self.cache_file_url, "./buildings/" + file_oid + "/" + cache_file_name),
        )
        cache_path = os.path.join(settings.CACHE_FILE_DIR, 'buildings', file_oid, cache_file_name)
        self.assertTrue(os.path.exists(cache_path))
        os.remove(cache_path)

    def test_get_document_file_url(self):
        org_file_name = '9a331bc8f7744c179caa20df0c3649b6.pdf'  # 書類サンプル1
        cache_file_name = 'cache_test_document.pdf'
        url = CacheFileHelper.get_document_file_url(
            org_file_name,
            cache_file_name,
        )
        self.assertEqual(
            url,
            urljoin(self.cache_file_url, "./documents/" + cache_file_name),
        )
        cache_path = os.path.join(settings.CACHE_FILE_DIR, 'documents', cache_file_name)
        self.assertTrue(os.path.exists(cache_path))
        os.remove(cache_path)
