"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import datetime
from lib.convert import *
from lib.functions import *
from lib.url_param_helper import UrlParamHelper


class SearchGarageConditions(object):
    """駐車場検索条件"""
    def __init__(self, *args, **kwargs):
        self.no_limited = False  # 管理種別の限定無し（管理物件・専任物件以外も含む）
        self.stations = None  # 駅
        self.walk_time = None  # 駅徒歩時間
        self.cities = None  # 市区町村
        self.areas = None  # エリア
        self.landmarks = None  # ランドマーク（大学など）
        self.north = None  # 北緯
        self.south = None  # 南緯
        self.east = None  # 東経
        self.west = None  # 西経

        super().__init__(*args, **kwargs)

    """
    メソッド
    """
    def set_conditions(self, url_params):
        """URLパラメータ（クエリストリング）の条件設定"""
        self.no_limited = UrlParamHelper.get_bool_param('no_lmt', url_params)     # 管理種別の限定無し（管理物件・専任物件以外も含む）
        self.stations = UrlParamHelper.get_id_array_param('stn', url_params)  # 駅ID
        self.walk_time = UrlParamHelper.get_int_param('wlk', url_params)    # 駅徒歩時間
        self.cities = UrlParamHelper.get_id_array_param('city', url_params)    # 市区町村ID
        self.areas = UrlParamHelper.get_id_array_param('area', url_params)     # エリアID
        self.landmarks = UrlParamHelper.get_id_array_param('ldmk', url_params)     # ランドマークID
        self.north = UrlParamHelper.get_float_param('north', url_params)      # 北緯
        self.south = UrlParamHelper.get_float_param('south', url_params)      # 南緯
        self.east = UrlParamHelper.get_float_param('east', url_params)      # 東経
        self.west = UrlParamHelper.get_float_param('west', url_params)      # 西経

    """
    プロパティ
    """
    @property
    def latlng_is_valid(self):
        """有効な緯度経度条件の確認"""
        ans = False
        if 0 < xfloat(self.south) < xfloat(self.north) and 0 < xfloat(self.west) < xfloat(self.east):
            ans = True
        return ans

    """
    FROM句用SQL
    """
    def get_no_limit_sql(self):
        ans = None
        if not self.no_limited:
            ans = ' INNER JOIN management_type ON building.management_type_id = management_type.id'
            ans += ' AND ('
            ans += 'management_type.is_own = TRUE'
            ans += ' OR management_type.is_entrusted = TRUE'
            ans += ')'

        return None

    def get_landmarks_sql(self, params):
        ans = None
        if self.landmarks:
            targets = ','.join(map(str, conditions.landmarks))
            ans = ' INNER JOIN ('
            ans += 'SELECT building_landmark.building_id'
            ans += ' FROM building_landmark'
            ans += ' WHERE building_landmark.landmark_id IN (%(landmarks)s)'
            ans += ' GROUP BY building_landmark.building_id'
            ans += ') landmark ON landmark.building_id = building.id'
            params['landmarks'] = targets
        return ans

    """
    WHERE句用SQL
    """
    def get_stations_sql(self, params):
        """駅・徒歩時間"""
        ans = None
        if self.stations and xint(self.walk_time) > 0:
            targets = self.__get_id_targets('station', self.stations, params)
            ans = '('
            ans += 'building.station_id1 IN ({0})'.format(targets)
            ans += ' AND building.arrival_type_id1 = 1 AND building.station_time1 <= %(walk_time)s'
            ans += ' OR building.station_id2 IN ({0})'.format(targets)
            ans += ' AND building.arrival_type_id2 = 1 AND building.station_time2 <= %(walk_time)s'
            ans += ' OR building.station_id3 IN ({0})'.format(targets)
            ans += ' AND building.arrival_type_id3 = 1 AND building.station_time3 <= %(walk_time)s'
            ans += ')'
            params['walk_time'] = self.walk_time
        elif self.stations:
            targets = self.__get_id_targets('station', self.stations, params)
            ans = '('
            ans += 'building.station_id1 IN ({0})'.format(targets)
            ans += ' OR building.station_id2 IN ({0})'.format(targets)
            ans += ' OR building.station_id3 IN ({0})'.format(targets)
            ans += ')'
        elif xint(self.walk_time) > 0:
            ans = '('
            ans += 'building.station_id1 != 0'
            ans += ' AND building.arrival_type_id1 = 1 AND building.station_time1 <= %(walk_time)s'
            ans += ' OR building.station_id2 != 0'
            ans += ' AND building.arrival_type_id2 = 1 AND building.station_time2 <= %(walk_time)s'
            ans += ' OR building.station_id3 != 0'
            ans += ' AND building.arrival_type_id3 = 1 AND building.station_time3 <= %(walk_time)s'
            ans += ')'
            params['walk_time'] = self.walk_time
        return ans

    def get_cities_sql(self, params):
        """市区町村"""
        ans = None
        if self.cities:
            targets = self.__get_id_targets('city', self.cities, params)
            ans = 'building.city_id IN ({0})'.format(targets)
        return ans

    def get_areas_sql(self, params):
        """エリア"""
        ans = None
        if self.areas:
            targets = self.__get_id_targets('area', self.areas, params)
            ans = 'building.area_id IN ({0})'.format(targets)
        return ans

    def get_latlng_sql(self, params):
        """緯度経度（東西南北）"""
        ans = None
        if self.latlng_is_valid:
            ans = 'building.lat > %(south)s'
            ans += ' AND building.lat < %(north)s'
            ans += ' AND building.lng > %(west)s'
            ans += ' AND building.lng < %(east)s'
            params['south'] = self.south
            params['north'] = self.north
            params['west'] = self.west
            params['east'] = self.east
        return ans

    """
    内部メソッド
    """
    @classmethod
    def __get_id_targets(cls, id_name, id_list, params):
        ans = ''
        if id_list:
            count = 0
            for item in id_list:
                param_name = '{0}_{1}'.format(id_name, count)
                if ans != '':
                    ans += ','
                ans += '%({0})s'.format(param_name)
                params[param_name] = item
                count += 1
        return ans
