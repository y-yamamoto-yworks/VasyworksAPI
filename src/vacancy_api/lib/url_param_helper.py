"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.utils import timezone
from Crypto.Util.Padding import pad, unpad
from lib.convert import *
from lib.functions import *


class UrlParamHelper:
    """URLパラメータヘルパークラス"""
    @staticmethod
    def get_param(key: str, url_params):
        return url_params.get(key, None)

    @staticmethod
    def get_int_param(key: str, url_params):
        ans = None
        data = url_params.get(key)
        if data:
            ans = xint(data)
            if ans == 0:
                ans = None
        return ans

    @staticmethod
    def get_id_param(key: str, url_params):
        return UrlParamHelper.get_int_param(key, url_params)

    @staticmethod
    def get_float_param(key: str, url_params):
        ans = None
        data = url_params.get(key)
        if data:
            ans = xfloat(data)
            if ans == 0:
                ans = None
        return ans

    @staticmethod
    def get_id_array_param(key: str, url_params):
        ans = None
        data = url_params.get(key)
        if data:
            id_list = data.split(',')
            ids = []
            for item in id_list:
                item_data = xint(item)
                if item_data != 0 and item_data not in ids:
                    ids.append(item_data)
            if len(ids) > 0:
                ans = tuple(ids)
        return ans

    @staticmethod
    def get_bool_param(key: str, url_params):
        ans = False
        data = url_params.get(key)
        if data:
            if data == '1' or data.lower() == 'true':
                ans = True
        return ans

    @staticmethod
    def get_order_param(key: str, url_params):
        ans = False
        data = url_params.get(key)
        if data:
            if data in ('rent', 'rent_desc', 'large', 'build', 'new_arr'):
                ans = data
        return ans
