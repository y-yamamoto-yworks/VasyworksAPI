"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from .layout_type_category_serializer import LayoutTypeCategorySerializer


class LayoutTypeSerializer(serializers.ModelSerializer):
    category = LayoutTypeCategorySerializer(many=False)

    """間取種別"""
    class Meta:
        model = LayoutType
        fields = ('id', 'name', 'room_count', 'category',)
