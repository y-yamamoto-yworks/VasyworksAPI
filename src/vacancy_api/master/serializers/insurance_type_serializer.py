"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class InsuranceTypeSerializer(serializers.ModelSerializer):
    """火災保険種別"""
    class Meta:
        model = InsuranceType
        fields = ('id', 'name', 'is_specified',)
