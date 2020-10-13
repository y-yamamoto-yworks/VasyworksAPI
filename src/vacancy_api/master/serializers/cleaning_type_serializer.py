"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class CleaningTypeSerializer(serializers.ModelSerializer):
    """退去時清掃種別"""
    class Meta:
        model = CleaningType
        fields = ('id', 'name', 'is_paid',)
