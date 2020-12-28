"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from master.serializers import *
from company.serializers import *
from .building_facility_serializer import BuildingFacilitySerializer
from .building_file_serializer import BuildingFileSerializer
from .building_garage_serializer import BuildingGarageSerializer
from .building_landmark_serializer import BuildingLandmarkSerializer
from .building_movie_serializer import BuildingMovieSerializer
from .building_panorama_serializer import BuildingPanoramaSerializer
from .building_picture_serializer import BuildingPictureSerializer
from .building_room_serializer import BuildingRoomSerializer


class BuildingSerializer(serializers.ModelSerializer):
    """建物"""
    agency_department = DepartmentSerializer(many=False)
    area = AreaSerializer(many=False)
    arrival_type1 = ArrivalTypeSerializer(many=False)
    arrival_type2 = ArrivalTypeSerializer(many=False)
    arrival_type3 = ArrivalTypeSerializer(many=False)
    bike_parking_type = BikeParkingTypeSerializer(many=False)
    bike_parking_fee_tax_type = TaxTypeSerializer(many=False)
    building_type = BuildingTypeSerializer(many=False)
    city = CitySerializer(many=False)
    department = DepartmentSerializer(many=False)
    elementary_school = ElementarySchoolSerializer(many=False)
    garage_charge_tax_type = TaxTypeSerializer(many=False)
    garage_fee_tax_type = TaxTypeSerializer(many=False)
    garage_status = GarageStatusSerializer(many=False)
    garage_type = GarageTypeSerializer(many=False)
    junior_high_school = JuniorHighSchoolSerializer(many=False)
    management_type = ManagementTypeSerializer(many=False)
    pref = PrefSerializer(many=False)
    staff1 = StaffSerializer(many=False)
    staff2 = StaffSerializer(many=False)
    station1 = StationSerializer(many=False)
    station2 = StationSerializer(many=False)
    station3 = StationSerializer(many=False)
    structure = StructureSerializer(many=False)

    facilities = BuildingFacilitySerializer(many=True)
    files = BuildingFileSerializer(many=True)
    garages = BuildingGarageSerializer(many=True)
    landmarks = BuildingLandmarkSerializer(many=True)
    movies = BuildingMovieSerializer(many=True)
    panoramas = BuildingPanoramaSerializer(many=True)
    pictures = BuildingPictureSerializer(many=True)
    vacancy_rooms = BuildingRoomSerializer(many=True)

    class Meta:
        model = Building
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
            'house_no',
            'building_no',
            'lat',
            'lng',
            'area_text',
            'area',
            'elementary_school_text',
            'elementary_school',
            'elementary_school_distance_text',
            'elementary_school_distance',
            'junior_high_school_text',
            'junior_high_school',
            'junior_high_school_distance_text',
            'junior_high_school_distance',
            'management_type',
            'department',
            'staff1_text',
            'staff1',
            'staff2_text',
            'staff2',
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
            'landmarks',
            'facilities',
            'around_note',
            'building_type_text',
            'building_type',
            'building_type_comment',
            'structure_text',
            'structure',
            'structure_comment',
            'building_rooms',
            'building_floors',
            'building_undergrounds',
            'build_year_month',
            'build_year',
            'build_month',
            'bike_parking_type_text',
            'bike_parking_type',
            'bike_parking_roof_text',
            'with_bike_parking_roof',
            'bike_parking_fee_text',
            'bike_parking_fee_lower',
            'bike_parking_fee_upper',
            'bike_parking_fee_tax_type',
            'bike_parking_note',
            'garage_type_text',
            'garage_type',
            'garage_status_text',
            'garage_status',
            'garage_distance_text',
            'garage_distance',
            'garage_fee_text',
            'garage_fee_lower',
            'garage_fee_upper',
            'garage_fee_tax_type',
            'garage_charge_text',
            'garage_charge_lower',
            'garage_charge_upper',
            'garage_charge_tax_type',
            'garage_note',
            'garages',
            'agreement_existence_text',
            'agreement_existence',
            'web_catch_copy',
            'web_appeal',
            'web_note',
            'pictures',
            'movies',
            'panoramas',
            'files',
            'vacancy_rooms',
        )
