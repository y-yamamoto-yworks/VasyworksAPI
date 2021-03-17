"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from master.serializers import *


class RoomEquipmentSerializer(serializers.ModelSerializer):
    """部屋設備"""
    equipment = EquipmentSerializer(many=False)

    class Meta:
        model = RoomEquipment
        fields = (
            'building_oid',
            'room_oid',
            'equipment',
            'is_remained',
        )
