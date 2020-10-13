"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class RoomStatusSerializer(serializers.ModelSerializer):
    """部屋状況"""
    class Meta:
        model = RoomStatus
        fields = ('id', 'name', 'for_rent', 'is_pending', 'will_be_canceled',)
