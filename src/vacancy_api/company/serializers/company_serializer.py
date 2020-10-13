"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class CompanySerializer(serializers.ModelSerializer):
    """会社"""

    class Meta:
        model = Company
        fields = (
            'id',
            'idb64',
            'company_name',
            'shop_name',
            'postal_code',
            'address',
            'tel',
            'fax',
            'mail',
            'agency_no',
            'pm_no',
        )
