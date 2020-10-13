"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class CondoFeesTypeSerializer(serializers.ModelSerializer):
    """共益費種別"""
    class Meta:
        model = CondoFeesType
        fields = ('id', 'name', 'is_money',)
