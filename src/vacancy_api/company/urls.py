"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.urls import include, path
from .views import *

urlpatterns = [
    path('<str:key>', CompanyViewSet.as_view({'get': 'retrieve'}), name='company_detail'),
    path('departments/<str:key>', DepartmentViewSet.as_view({'get': 'list'}), name='company_departments'),
    path('staffs/<str:key>', StaffViewSet.as_view({'get': 'list'}), name='company_staffs'),
    path('staffs/<str:key>/<int:department_id>', StaffViewSet.as_view({'get': 'list'}), name='company_staffs'),
]
