"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.urls import include, path
from .views import *

urlpatterns = [
    path('buildings/<str:key>', BuildingListViewSet.as_view({'get': 'list'}), name='search_buildings'),
    path('garages/<str:key>', GarageListViewSet.as_view({'get': 'list'}), name='search_garages'),
    path('rooms/<str:key>', RoomListViewSet.as_view({'get': 'list'}), name='search_rooms'),
    path('non_residential_buildings/<str:key>', NonResidentialBuildingListViewSet.as_view({'get': 'list'}), name='search_non_residential_buildings'),
    path('non_residential_rooms/<str:key>', NonResidentialRoomListViewSet.as_view({'get': 'list'}), name='search_non_residential_rooms'),
]
