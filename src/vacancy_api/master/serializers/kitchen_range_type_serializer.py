"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class KitchenRangeTypeSerializer(serializers.ModelSerializer):
    """キッチンレンジ種別"""
    class Meta:
        model = KitchenRangeType
        fields = ('id', 'name',)
