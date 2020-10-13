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
from .searched_garage_detail_serializer import SearchedGarageDetailSerializer
from .searched_garage_picture_serializer import SearchedGaragePictureSerializer


class SearchedGarageSerializer(serializers.ModelSerializer):
    """検索駐車場"""
    agency_department = DepartmentSerializer(many=False)
    area = AreaSerializer(many=False)
    arrival_type1 = ArrivalTypeSerializer(many=False)
    arrival_type2 = ArrivalTypeSerializer(many=False)
    arrival_type3 = ArrivalTypeSerializer(many=False)
    building_type = BuildingTypeSerializer(many=False)
    city = CitySerializer(many=False)
    department = DepartmentSerializer(many=False)
    garage_status = GarageStatusSerializer(many=False)
    pref = PrefSerializer(many=False)
    station1 = StationSerializer(many=False)
    station2 = StationSerializer(many=False)
    station3 = StationSerializer(many=False)

    details = SearchedGarageDetailSerializer(many=True)
    garage_picture = SearchedGaragePictureSerializer(many=False)

    class Meta:
        model = SearchedGarage
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
            'garage_status_text',
            'garage_status',
            'web_catch_copy',
            'web_appeal',
            'details',
            'garage_picture',
        )
