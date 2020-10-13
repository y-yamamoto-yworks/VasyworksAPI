"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""

import uuid
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .convert import *


def get_unique_filename(filename):
    """元ファイル名からユニークファイル名に変換"""
    ext = filename.split('.')[-1]
    ans = "%s.%s" % (uuid.uuid4(), ext)
    ans = ans.replace('-', '')
    return ans


def base64_decode_id(id: int):
    """整数をBase64に変換"""
    return urlsafe_base64_encode(force_bytes(id))


def base64_encode_id(idb64: str):
    """Base64を整数に変換"""
    ans = 0

    try:
        id = force_text(urlsafe_base64_decode(idb64))
        if id.isdecimal():
            ans = xint(id)
    except ValueError:
        ans = 0

    return ans


def float_normalize(value: float):
    """小数点以下の最後の0を取り除く"""
    ans = None
    value_str = xstr(value)
    parts = value_str.split('.')
    if len(parts) == 1:
        ans = parts[0]
    elif len(parts) == 2:
        left_part = parts[0]
        right_part = parts[1]
        while right_part[-1:] == '0' and len(right_part) > 0:
            right_part = right_part[:-1]

        ans = left_part
        if right_part != '':
            ans += '.{0}'.format(right_part)

    return ans
