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
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from lib.convert import *
from lib.functions import *
from rent_db.models import Company


class ApiHelper:
    """APIヘルパークラス"""
    @staticmethod
    def check_key(key: str):
        """APIキー確認"""
        ans = False
        company = Company.objects.get(pk=settings.COMPANY_ID)
        if company.api_key == key:
            ans = True

        return ans
