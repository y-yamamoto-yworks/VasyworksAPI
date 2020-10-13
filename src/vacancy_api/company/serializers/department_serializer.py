"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from .company_serializer import CompanySerializer


class DepartmentSerializer(serializers.ModelSerializer):
    """部署"""

    class Meta:
        model = Department
        fields = (
            'id',
            'idb64',
            'department_name',
            'postal_code',
            'address',
            'tel',
            'fax',
            'mail',
        )
