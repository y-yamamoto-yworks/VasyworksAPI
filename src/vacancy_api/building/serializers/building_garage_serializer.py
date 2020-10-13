"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from master.serializers import *


class BuildingGarageSerializer(serializers.ModelSerializer):
    """建物駐車場"""
    garage_fee_tax_type = TaxTypeSerializer(many=False)
    garage_charge_tax_type = TaxTypeSerializer(many=False)
    garage_deposit_tax_type = TaxTypeSerializer(many=False)
    certification_fee_tax_type = TaxTypeSerializer(many=False)
    initial_cost_tax_type1 = TaxTypeSerializer(many=False)
    initial_cost_tax_type2 = TaxTypeSerializer(many=False)
    initial_cost_tax_type3 = TaxTypeSerializer(many=False)
    garage_status = GarageStatusSerializer(many=False)

    class Meta:
        model = BuildingGarage
        fields = (
            'id',
            'building_oid',
            'garage_name',
            'garage_fee_text',
            'garage_fee',
            'garage_fee_tax_type',
            'garage_charge_text',
            'garage_charge',
            'garage_charge_tax_type',
            'garage_deposit_text',
            'garage_deposit',
            'garage_deposit_tax_type',
            'certification_fee_text',
            'certification_fee',
            'certification_fee_tax_type',
            'initial_cost_name1',
            'initial_cost_text1',
            'initial_cost1',
            'initial_cost_tax_type1',
            'initial_cost_name2',
            'initial_cost_text2',
            'initial_cost2',
            'initial_cost_tax_type2',
            'initial_cost_name3',
            'initial_cost_text3',
            'initial_cost3',
            'initial_cost_tax_type3',
            'garage_status_text',
            'garage_status',
            'allow_no_room_text',
            'allow_no_room',
            'garage_size_text',
            'width',
            'length',
            'height',
            'comment',
        )
