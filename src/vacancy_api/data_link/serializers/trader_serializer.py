"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class TraderSerializer(serializers.ModelSerializer):
    """賃貸他業者"""
    class Meta:
        model = Trader
        fields = (
            'id',
            'trader_name',
            'tel1',
            'no_trading',
            'no_portal',
        )
