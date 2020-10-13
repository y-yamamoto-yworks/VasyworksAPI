"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""


def xstr(value):
    """ 文字列型に変換"""

    if value is None:
        return ""
    else:
        return str(value)


def xint(value):
    """ 整数型に変換 """

    if value is None:
        return 0
    else:
        try:
            return int(value)
        except:
            return 0


def xfloat(value):
    """ 浮動小数点型に変換 """

    if value is None:
        return float(0)
    else:
        try:
            return float(value)
        except:
            return float(0)


def int_to_bool(value):
    """ 整数型をブール型に変換"""

    if xint(value) == 0:
        return False
    else:
        return True
