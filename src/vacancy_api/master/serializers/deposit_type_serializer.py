"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class DepositTypeSerializer(serializers.ModelSerializer):
    """保証金種別"""
    class Meta:
        model = DepositType
        fields = ('id', 'name', 'coefficient',)
