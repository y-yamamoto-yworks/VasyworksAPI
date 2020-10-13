"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import sys
import shutil
from django.conf import settings
from urllib.parse import urljoin
from lib.image_helper import ImageHelper


class CacheFileHelper:
    """キャッシュファイルヘルパークラス"""
    @staticmethod
    def __prepare_cache_dir():
        """ キャッシュ用ディレクトリの準備"""

        cache_path = os.path.join(settings.CACHE_FILE_DIR, "buildings")
        if not os.path.isdir(cache_path):
            os.makedirs(cache_path)

        cache_path = os.path.join(settings.CACHE_FILE_DIR, "documents")
        if not os.path.isdir(cache_path):
            os.makedirs(cache_path)

    @staticmethod
    def __copy_file(src, dest):
        """ファイルのコピー"""
        ans = False

        if os.path.exists(src) and not os.path.exists(dest):
            try:
                shutil.copy2(src, dest)
                ans = True
            except:
                ans = False

        return ans

    @staticmethod
    def __get_property_file_url(file_oid, file_dir, org_file_name, cache_file_name):
        """ 建物、部屋のファイルのURLの取得（画像ファイル以外） """

        CacheFileHelper.__prepare_cache_dir()
        cache_path = os.path.join(settings.CACHE_FILE_DIR, 'buildings', file_oid)
        cache_url = urljoin(settings.CACHE_FILE_URL, "./buildings/" + file_oid + "/")
        if not os.path.isdir(cache_path):
            os.makedirs(cache_path)

        cache_file_url = None
        org_file_path = os.path.join(settings.ORIGINAL_FILE_DIR, 'buildings', file_oid, file_dir, org_file_name)
        if os.path.isfile(org_file_path):
            cache_file_path = os.path.join(cache_path, cache_file_name)
            cache_file_url = urljoin(cache_url, cache_file_name)
            if not os.path.isfile(cache_file_path):
                CacheFileHelper.__copy_file(org_file_path, cache_file_path)

        return urljoin(settings.BASE_URL, cache_file_url)

    @staticmethod
    def get_property_image_file_url(file_oid, org_file_name, cache_file_name, water_mark, max_size):
        """ 建物、部屋の画像のURLの取得 """

        CacheFileHelper.__prepare_cache_dir()
        cache_path = os.path.join(settings.CACHE_FILE_DIR, 'buildings', file_oid)
        cache_url = urljoin(settings.CACHE_FILE_URL, "./buildings/" + file_oid + "/")
        if not os.path.isdir(cache_path):
            os.makedirs(cache_path)

        cache_file_url = None
        org_file_path = os.path.join(settings.ORIGINAL_FILE_DIR, 'buildings', file_oid, 'pictures', org_file_name)
        if os.path.isfile(org_file_path):
            cache_file_path = os.path.join(cache_path, cache_file_name)
            cache_file_url = urljoin(cache_url, cache_file_name)
            if not os.path.isfile(cache_file_path):
                ImageHelper.cache_image(org_file_path, cache_file_path, water_mark, max_size)

        return urljoin(settings.BASE_URL, cache_file_url)

    @staticmethod
    def get_property_panorama_file_url(file_oid, org_file_name, cache_file_name):
        """建物、部屋のパノラマのURL取得"""
        return CacheFileHelper.__get_property_file_url(file_oid, 'panoramas', org_file_name, cache_file_name)

    @staticmethod
    def get_property_movie_file_url(file_oid, org_file_name, cache_file_name):
        """建物、部屋の動画のURL取得"""
        return CacheFileHelper.__get_property_file_url(file_oid, 'movies', org_file_name, cache_file_name)

    @staticmethod
    def get_building_file_url(file_oid, org_file_name, cache_file_name):
        """建物ファイルのURL取得"""
        return CacheFileHelper.__get_property_file_url(file_oid, 'files', org_file_name, cache_file_name)

    @staticmethod
    def get_document_file_url(org_file_name, cache_file_name):
        """書類ファイルのURL取得"""
        CacheFileHelper.__prepare_cache_dir()
        cache_path = os.path.join(settings.CACHE_FILE_DIR, 'documents')
        cache_url = urljoin(settings.CACHE_FILE_URL, "./documents/")

        cache_file_url = None
        org_file_path = os.path.join(settings.ORIGINAL_FILE_DIR, 'documents', 'files', org_file_name)
        if os.path.isfile(org_file_path):
            cache_file_path = os.path.join(cache_path, cache_file_name)
            cache_file_url = urljoin(cache_url, cache_file_name)
            if not os.path.isfile(cache_file_path):
                CacheFileHelper.__copy_file(org_file_path, cache_file_path)

        return urljoin(settings.BASE_URL, cache_file_url)
