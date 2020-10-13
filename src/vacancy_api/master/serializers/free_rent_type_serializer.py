"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class FreeRentTypeSerializer(serializers.ModelSerializer):
    """フリーレント種別"""
    class Meta:
        model = FreeRentType
        fields = ('id', 'name', 'limit_is_span', 'limit_is_month',)
