"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
"""
from django.urls import include, path
from .views import *

urlpatterns = [
    path('buildings/', BuildingListViewSet.as_view({'get': 'list'}), name='search_buildings'),
    path('garages/', GarageListViewSet.as_view({'get': 'list'}), name='search_garages'),
    path('rooms/', RoomListViewSet.as_view({'get': 'list'}), name='search_rooms'),
    path('non_residential_buildings/', NonResidentialBuildingListViewSet.as_view({'get': 'list'}), name='search_non_residential_buildings'),
    path('non_residential_rooms/', NonResidentialRoomListViewSet.as_view({'get': 'list'}), name='search_non_residential_rooms'),
]
