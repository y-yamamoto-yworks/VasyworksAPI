"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class RenewalFeeNotationSerializer(serializers.ModelSerializer):
    """更新料表記"""
    class Meta:
        model = RenewalFeeNotation
        fields = ('id', 'name', 'header', 'unit', 'is_money', 'is_month', 'is_rate',)
