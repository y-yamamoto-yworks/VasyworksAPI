"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from master.serializers import *
from .building_serializer import BuildingSerializer
from .room_equipment_serializer import RoomEquipmentSerializer
from .room_movie_serializer import RoomMovieSerializer
from .room_panorama_serializer import RoomPanoramaSerializer
from .room_picture_serializer import RoomPictureSerializer


class RoomSerializer(serializers.ModelSerializer):
    """部屋"""
    building = BuildingSerializer(many=False)
    rental_type = RentalTypeSerializer(many=False)
    room_status = RoomStatusSerializer(many=False)
    vacancy_status = VacancyStatusSerializer(many=False)
    layout_type = LayoutTypeSerializer(many=False)
    kitchen_type1 = KitchenTypeSerializer(many=False)
    kitchen_type2 = KitchenTypeSerializer(many=False)
    kitchen_type3 = KitchenTypeSerializer(many=False)
    direction = DirectionSerializer(many=False)
    balcony_type = BalconyTypeSerializer(many=False)
    rent_tax_type = TaxTypeSerializer(many=False)
    condo_fees_type = CondoFeesTypeSerializer(many=False)
    condo_fees_tax_type = TaxTypeSerializer(many=False)
    free_rent_type = FreeRentTypeSerializer(many=False)
    water_cost_type = WaterCostTypeSerializer(many=False)
    water_cost_tax_type = TaxTypeSerializer(many=False)
    payment_type = PaymentTypeSerializer(many=False)
    payment_fee_type = PaymentFeeTypeSerializer(many=False)
    payment_fee_tax_type = TaxTypeSerializer(many=False)
    monthly_cost_tax_type1 = TaxTypeSerializer(many=False)
    monthly_cost_tax_type2 = TaxTypeSerializer(many=False)
    monthly_cost_tax_type3 = TaxTypeSerializer(many=False)
    monthly_cost_tax_type4 = TaxTypeSerializer(many=False)
    monthly_cost_tax_type5 = TaxTypeSerializer(many=False)
    monthly_cost_tax_type6 = TaxTypeSerializer(many=False)
    monthly_cost_tax_type7 = TaxTypeSerializer(many=False)
    monthly_cost_tax_type8 = TaxTypeSerializer(many=False)
    monthly_cost_tax_type9 = TaxTypeSerializer(many=False)
    monthly_cost_tax_type10 = TaxTypeSerializer(many=False)
    deposit_type1 = DepositTypeSerializer(many=False)
    deposit_notation1 = DepositNotationSerializer(many=False)
    deposit_tax_type1 = TaxTypeSerializer(many=False)
    deposit_type2 = DepositTypeSerializer(many=False)
    deposit_notation2 = DepositNotationSerializer(many=False)
    deposit_tax_type2 = TaxTypeSerializer(many=False)
    key_money_type1 = KeyMoneyTypeSerializer(many=False)
    key_money_notation1 = KeyMoneyNotationSerializer(many=False)
    key_money_tax_type1 = TaxTypeSerializer(many=False)
    key_money_type2 = KeyMoneyTypeSerializer(many=False)
    key_money_notation2 = KeyMoneyNotationSerializer(many=False)
    key_money_tax_type2 = TaxTypeSerializer(many=False)
    renewal_fee_notation = RenewalFeeNotationSerializer(many=False)
    renewal_fee_tax_type = TaxTypeSerializer(many=False)
    renewal_charge_existence = ExistenceSerializer(many=False)
    renewal_charge_tax_type = TaxTypeSerializer(many=False)
    recontract_fee_existence = ExistenceSerializer(many=False)
    recontract_fee_tax_type = TaxTypeSerializer(many=False)
    insurance_type = InsuranceTypeSerializer(many=False)
    insurance_fee_tax_type = TaxTypeSerializer(many=False)
    guarantee_type = GuaranteeTypeSerializer(many=False)
    document_cost_existence = ExistenceSerializer(many=False)
    document_cost_tax_type = TaxTypeSerializer(many=False)
    key_change_cost_existence = ExistenceSerializer(many=False)
    key_change_cost_tax_type = TaxTypeSerializer(many=False)
    initial_cost_tax_type1 = TaxTypeSerializer(many=False)
    initial_cost_tax_type2 = TaxTypeSerializer(many=False)
    initial_cost_tax_type3 = TaxTypeSerializer(many=False)
    initial_cost_tax_type4 = TaxTypeSerializer(many=False)
    initial_cost_tax_type5 = TaxTypeSerializer(many=False)
    initial_cost_tax_type6 = TaxTypeSerializer(many=False)
    initial_cost_tax_type7 = TaxTypeSerializer(many=False)
    initial_cost_tax_type8 = TaxTypeSerializer(many=False)
    initial_cost_tax_type9 = TaxTypeSerializer(many=False)
    initial_cost_tax_type10 = TaxTypeSerializer(many=False)
    cleaning_type = CleaningTypeSerializer(many=False)
    cleaning_cost_tax_type = TaxTypeSerializer(many=False)
    electric_type = ElectricTypeSerializer(many=False)
    gas_type = GasTypeSerializer(many=False)
    bath_type = BathTypeSerializer(many=False)
    toilet_type = ToiletTypeSerializer(many=False)
    kitchen_range_type = KitchenRangeTypeSerializer(many=False)
    internet_type = InternetTypeSerializer(many=False)
    washer_type = WasherTypeSerializer(many=False)
    pet_type = PetTypeSerializer(many=False)
    instrument_type = AllowTypeSerializer(many=False)
    live_together_type = AllowTypeSerializer(many=False)
    children_type = AllowTypeSerializer(many=False)
    share_type = AllowTypeSerializer(many=False)
    non_japanese_type = AllowTypeSerializer(many=False)
    only_woman_type = AllowTypeSerializer(many=False)
    only_man_type = AllowTypeSerializer(many=False)
    corp_contract_type = AllowTypeSerializer(many=False)
    student_type = AllowTypeSerializer(many=False)
    new_student_type = AllowTypeSerializer(many=False)
    office_use_type = AllowTypeSerializer(many=False)

    equipments = RoomEquipmentSerializer(many=True)
    movies = RoomMovieSerializer(many=True)
    panoramas = RoomPanoramaSerializer(many=True)
    pictures = RoomPictureSerializer(many=True)

    class Meta:
        model = Room
        fields = (
            'id',
            'oid',
            'room_no',
            'building',
            'room_floor',
            'rental_type',
            'is_sublease',
            'is_condo_management',
            'is_entrusted',
            'room_status',
            'vacancy_status',
            'vacancy_status_note',
            'layout_type',
            'layout_detail_text',
            'western_style_room1',
            'western_style_room2',
            'western_style_room3',
            'western_style_room4',
            'western_style_room5',
            'western_style_room6',
            'western_style_room7',
            'western_style_room8',
            'western_style_room9',
            'western_style_room10',
            'japanese_style_room1',
            'japanese_style_room2',
            'japanese_style_room3',
            'japanese_style_room4',
            'japanese_style_room5',
            'japanese_style_room6',
            'japanese_style_room7',
            'japanese_style_room8',
            'japanese_style_room9',
            'japanese_style_room10',
            'kitchen_type1',
            'kitchen1',
            'kitchen_type2',
            'kitchen2',
            'kitchen_type3',
            'kitchen3',
            'store_room1',
            'store_room2',
            'store_room3',
            'loft1',
            'loft2',
            'sun_room1',
            'sun_room2',
            'layout_note',
            'room_area',
            'direction',
            'balcony_type',
            'balcony_area',
            'rent',
            'rent_upper',
            'rent_tax_type',
            'rent_hidden',
            'condo_fees_type',
            'condo_fees',
            'condo_fees_tax_type',
            'free_rent_text',
            'free_rent_type',
            'free_rent_months',
            'free_rent_limit_year',
            'free_rent_limit_month',
            'water_cost_text',
            'water_cost_type',
            'water_cost',
            'water_cost_tax_type',
            'payment_type_text',
            'payment_type',
            'payment_fee_type_text',
            'payment_fee_type',
            'payment_fee_text',
            'payment_fee',
            'payment_fee_tax_type',
            'monthly_cost_name1',
            'monthly_cost_text1',
            'monthly_cost1',
            'monthly_cost_tax_type1',
            'monthly_cost_name2',
            'monthly_cost_text2',
            'monthly_cost2',
            'monthly_cost_tax_type2',
            'monthly_cost_name3',
            'monthly_cost_text3',
            'monthly_cost3',
            'monthly_cost_tax_type3',
            'monthly_cost_name4',
            'monthly_cost_text4',
            'monthly_cost4',
            'monthly_cost_tax_type4',
            'monthly_cost_name5',
            'monthly_cost_text5',
            'monthly_cost5',
            'monthly_cost_tax_type5',
            'monthly_cost_name6',
            'monthly_cost_text6',
            'monthly_cost6',
            'monthly_cost_tax_type6',
            'monthly_cost_name7',
            'monthly_cost_text7',
            'monthly_cost7',
            'monthly_cost_tax_type7',
            'monthly_cost_name8',
            'monthly_cost_text8',
            'monthly_cost8',
            'monthly_cost_tax_type8',
            'monthly_cost_name9',
            'monthly_cost_text9',
            'monthly_cost9',
            'monthly_cost_tax_type9',
            'monthly_cost_name10',
            'monthly_cost_text10',
            'monthly_cost10',
            'monthly_cost_tax_type10',
            'monthly_cost_note',
            'deposit_type_text1',
            'deposit_text1',
            'deposit_type1',
            'deposit_notation1',
            'deposit_value1',
            'deposit_tax_type1',
            'deposit_comment1',
            'deposit_type_text2',
            'deposit_text2',
            'deposit_type2',
            'deposit_notation2',
            'deposit_value2',
            'deposit_tax_type2',
            'deposit_comment2',
            'key_money_type_text1',
            'key_money_text1',
            'key_money_type1',
            'key_money_notation1',
            'key_money_value1',
            'key_money_tax_type1',
            'key_money_comment1',
            'key_money_type_text2',
            'key_money_text2',
            'key_money_type2',
            'key_money_notation2',
            'key_money_value2',
            'key_money_tax_type2',
            'key_money_comment2',
            'contract_years',
            'contract_months',
            'renewal_fee_text',
            'renewal_fee_notation',
            'renewal_fee_value',
            'renewal_fee_tax_type',
            'renewal_charge_text',
            'renewal_charge_existence',
            'renewal_charge',
            'renewal_charge_tax_type',
            'is_auto_renewal',
            'renewal_note',
            'recontract_fee_text',
            'recontract_fee_existence',
            'recontract_fee',
            'recontract_fee_tax_type',
            'recontract_note',
            'insurance_type_text',
            'insurance_text',
            'insurance_type',
            'insurance_years',
            'insurance_fee',
            'insurance_fee_tax_type',
            'guarantee_type_text',
            'guarantee_type',
            'guarantee_fee',
            'document_cost_text',
            'document_cost_existence',
            'document_cost',
            'document_cost_tax_type',
            'document_cost_comment',
            'key_change_cost_text',
            'key_change_cost_existence',
            'key_change_cost',
            'key_change_cost_tax_type',
            'key_change_comment',
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
            'initial_cost_name4',
            'initial_cost_text4',
            'initial_cost4',
            'initial_cost_tax_type4',
            'initial_cost_name5',
            'initial_cost_text5',
            'initial_cost5',
            'initial_cost_tax_type5',
            'initial_cost_name6',
            'initial_cost_text6',
            'initial_cost6',
            'initial_cost_tax_type6',
            'initial_cost_name7',
            'initial_cost_text7',
            'initial_cost7',
            'initial_cost_tax_type7',
            'initial_cost_name8',
            'initial_cost_text8',
            'initial_cost8',
            'initial_cost_tax_type8',
            'initial_cost_name9',
            'initial_cost_text9',
            'initial_cost9',
            'initial_cost_tax_type9',
            'initial_cost_name10',
            'initial_cost_text10',
            'initial_cost10',
            'initial_cost_tax_type10',
            'initial_cost_note',
            'cleaning_cost_text',
            'cleaning_type',
            'cleaning_cost',
            'cleaning_cost_tax_type',
            'cleaning_note',
            'electric_type',
            'electric_comment',
            'gas_type',
            'gas_comment',
            'bath_type',
            'bath_comment',
            'toilet_type',
            'toilet_comment',
            'kitchen_range_type',
            'kitchen_range_comment',
            'internet_type',
            'internet_comment',
            'washer_type',
            'washer_comment',
            'pet_type',
            'pet_comment',
            'equipments_text',
            'equipments',
            'instrument_type',
            'live_together_type',
            'children_type',
            'share_type',
            'non_japanese_type',
            'only_woman_type',
            'only_man_type',
            'corp_contract_type',
            'student_type',
            'new_student_type',
            'office_use_type',
            'constraint_note',
            'reform_comment',
            'reform_year',
            'reform_month',
            'web_catch_copy',
            'web_appeal',
            'web_note',
            'pictures',
            'movies',
            'panoramas',
        )
