"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class RentalTypeSerializer(serializers.ModelSerializer):
    """賃貸種別"""
    class Meta:
        model = RentalType
        fields = ('id', 'name', 'short_name', 'is_limited_rent', 'is_own')
