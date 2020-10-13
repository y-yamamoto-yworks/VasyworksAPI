"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class BikeParkingTypeSerializer(serializers.ModelSerializer):
    """駐輪場種別"""
    class Meta:
        model = BikeParkingType
        fields = ('id', 'name', 'is_exist', 'is_paid',)
