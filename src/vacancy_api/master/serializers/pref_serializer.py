"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class PrefSerializer(serializers.ModelSerializer):
    """都道府県"""
    class Meta:
        model = Pref
        fields = ('id', 'name',)
