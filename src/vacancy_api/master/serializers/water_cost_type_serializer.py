"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class WaterCostTypeSerializer(serializers.ModelSerializer):
    """水道費種別"""
    class Meta:
        model = WaterCostType
        fields = ('id', 'name', 'is_money',)
