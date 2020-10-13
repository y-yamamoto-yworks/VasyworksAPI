"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class PaymentFeeTypeSerializer(serializers.ModelSerializer):
    """支払手数料種別"""
    class Meta:
        model = PaymentFeeType
        fields = ('id', 'name', 'is_money',)
