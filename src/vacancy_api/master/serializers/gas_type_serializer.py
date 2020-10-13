"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class GasTypeSerializer(serializers.ModelSerializer):
    """ガス種別"""
    class Meta:
        model = GasType
        fields = ('id', 'name',)
