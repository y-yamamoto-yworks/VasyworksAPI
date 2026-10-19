"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
"""
import hmac
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.utils import timezone
from Crypto.Util.Padding import pad, unpad
from lib.convert import *
from lib.functions import *
from rent_db.models import Company


class ApiHelper:
    """APIヘルパークラス"""
    @staticmethod
    def check_key(request):
        """APIキー確認"""
        ans = False

        api_key = request.META.get('HTTP_X_API_KEY')
        if not api_key:
            return False

        company = Company.objects.get(pk=settings.COMPANY_ID)

        if hmac.compare_digest(company.api_key, api_key):
            ans = True

        return ans
