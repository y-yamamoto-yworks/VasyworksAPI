"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class ToiletTypeSerializer(serializers.ModelSerializer):
    """トイレ種別"""
    class Meta:
        model = ToiletType
        fields = ('id', 'name',)
