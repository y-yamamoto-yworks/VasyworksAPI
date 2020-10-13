"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from master.serializers import *
from company.serializers import *
from search.models import *
from .searched_building_exterior_picture_serializer import SearchedBuildingExteriorPictureSerializer
from .searched_room_interior_picture_serializer import SearchedRoomInteriorPictureSerializer
from .searched_room_layout_picture_serializer import SearchedRoomLayoutPictureSerializer


class SearchedRoomSerializer(serializers.ModelSerializer):
    """検索部屋"""
    agency_department = DepartmentSerializer(many=False)
    area = AreaSerializer(many=False)
    arrival_type1 = ArrivalTypeSerializer(many=False)
    arrival_type2 = ArrivalTypeSerializer(many=False)
    arrival_type3 = ArrivalTypeSerializer(many=False)
    bike_parking_type = BikeParkingTypeSerializer(many=False)
    building_type = BuildingTypeSerializer(many=False)
    city = CitySerializer(many=False)
    department = DepartmentSerializer(many=False)
    garage_type = GarageTypeSerializer(many=False)
    pref = PrefSerializer(many=False)
    station1 = StationSerializer(many=False)
    station2 = StationSerializer(many=False)
    station3 = StationSerializer(many=False)
    structure = StructureSerializer(many=False)

    exterior_picture = SearchedBuildingExteriorPictureSerializer(many=False)
    interior_picture = SearchedRoomInteriorPictureSerializer(many=False)
    layout_picture = SearchedRoomLayoutPictureSerializer(many=False)

    class Meta:
        model = SearchedRoom
        fields = (
            'id',
            'oid',
            'building_code',
            'building_name',
            'building_kana',
            'building_old_name',
            'postal_code',
            'address',
            'pref',
            'city',
            'town_address',
            'town_name',
            'house_no',
            'building_no',
            'lat',
            'lng',
            'area_text',
            'area',
            'department',
            'agency_department',
            'nearest_station1',
            'arrival_type1',
            'station1',
            'station_time1',
            'bus_stop1',
            'bus_stop_time1',
            'nearest_station2',
            'arrival_type2',
            'station2',
            'station_time2',
            'bus_stop2',
            'bus_stop_time2',
            'nearest_station3',
            'arrival_type3',
            'station3',
            'station_time3',
            'bus_stop3',
            'bus_stop_time3',
            'building_type_text',
            'building_type',
            'structure_text',
            'structure',
            'building_rooms',
            'building_floors',
            'building_undergrounds',
            'build_year_month',
            'build_year',
            'build_month',
            'bike_parking_type_text',
            'bike_parking_type',
            'garage_type_text',
            'garage_type',
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
            'web_catch_copy',
            'web_appeal',
            'exterior_picture',
            'interior_picture',
            'layout_picture',
            'has_panoramas',
            'has_movies',
        )
