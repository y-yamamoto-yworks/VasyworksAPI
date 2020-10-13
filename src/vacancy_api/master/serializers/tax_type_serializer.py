"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class TaxTypeSerializer(serializers.ModelSerializer):
    """税種別"""
    class Meta:
        model = TaxType
        fields = ('id', 'name', 'is_excluding', 'is_including')
