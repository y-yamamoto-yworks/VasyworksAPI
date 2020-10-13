"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from lib.serializer_helper import SerializerHelper
from master.serializers import *
from company.serializers import *
from search.models import *
from .searched_room_interior_picture_serializer import SearchedRoomInteriorPictureSerializer
from .searched_room_layout_picture_serializer import SearchedRoomLayoutPictureSerializer


class SearchedBuildingRoomSerializer(serializers.ModelSerializer):
    """検索建物の部屋"""
    interior_picture = SearchedRoomInteriorPictureSerializer(many=False)
    layout_picture = SearchedRoomLayoutPictureSerializer(many=False)

    class Meta:
        model = SearchedBuildingRoom
        fields = (
            'id',
            'oid',
            'building_oid',
            'room_no',
            'rental_type_text',
            'rental_type_short_text',
            'room_status_text',
            'vacancy_status_text',
            'room_floor_text',
            'rent_text',
            'condo_fees_text',
            'water_cost_text',
            'free_rent_text',
            'deposit_type_text1',
            'deposit_text1',
            'deposit_type_text2',
            'deposit_text2',
            'key_money_type_text1',
            'key_money_text1',
            'key_money_type_text2',
            'key_money_text2',
            'contract_span_text',
            'renewal_fee_text',
            'layout_type_text',
            'layout_detail_text',
            'room_area_text',
            'direction_text',
            'bath_text',
            'kitchen_range_text',
            'internet_text',
            'washer_text',
            'pet_text',
            'equipments_text',
            'equipments_short_text',
            'web_catch_copy',
            'web_appeal',
            'interior_picture',
            'layout_picture',
            'has_panoramas',
            'has_movies',
        )
