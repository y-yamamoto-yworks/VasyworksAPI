"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class LayoutTypeCategorySerializer(serializers.ModelSerializer):
    """間取種別カテゴリ"""
    class Meta:
        model = LayoutTypeCategory
        fields = ('id', 'name',)
