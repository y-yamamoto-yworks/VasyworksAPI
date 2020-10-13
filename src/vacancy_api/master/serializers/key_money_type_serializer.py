"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class KeyMoneyTypeSerializer(serializers.ModelSerializer):
    """一時金種別"""
    class Meta:
        model = KeyMoneyType
        fields = ('id', 'name', 'coefficient',)
