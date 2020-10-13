"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class DepositNotationSerializer(serializers.ModelSerializer):
    """保証金表記"""
    class Meta:
        model = DepositNotation
        fields = ('id', 'name', 'unit', 'is_money', 'is_month', 'is_rate',)
