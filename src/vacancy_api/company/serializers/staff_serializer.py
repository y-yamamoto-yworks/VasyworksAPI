"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from .department_serializer import DepartmentSerializer


class StaffSerializer(serializers.ModelSerializer):
    """スタッフ"""
    department = DepartmentSerializer(many=False)

    class Meta:
        model = Staff
        fields = (
            'id',
            'idb64',
            'last_name',
            'first_name',
            'full_name',
            'staff_name',
            'tel1',
            'tel2',
            'mail',
            'department',
        )
