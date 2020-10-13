"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class WasherTypeSerializer(serializers.ModelSerializer):
    """洗濯機設置種別"""
    class Meta:
        model = WasherType
        fields = ('id', 'name', 'is_ok',)
