"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class GarageTypeSerializer(serializers.ModelSerializer):
    """駐車場種別"""
    class Meta:
        model = GarageType
        fields = ('id', 'name', 'is_exist', 'is_free', 'is_paid',)
