"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.urls import include, path
from .views import *

urlpatterns = [
    path('vacancy_rooms/<str:key>', VacancyRoomViewSet.as_view({'get': 'list'}), name='data_link_vacancy_rooms'),
]
