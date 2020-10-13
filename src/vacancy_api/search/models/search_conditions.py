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


class SearchConditions(object):
    """検索条件"""
    no_limited = False          # 管理種別の限定無し（管理物件・専任物件以外も含む）
    stations = None             # 駅
    walk_time = None            # 駅徒歩時間
    cities = None               # 市区町村
    areas = None                # エリア
    landmarks = None            # ランドマーク（大学など）
    north = None                # 北緯
    south = None                # 南緯
    east = None                 # 東経
    west = None                 # 西経
    elementary_school = None    # 小学校区
    building_types = None       # 建物種別
    building_age = None         # 築年数
    with_garage = False         # 駐車場
    with_bike_parking = False   # 駐輪場

    rent_lower = None           # 賃料下限
    rent_upper = None           # 賃料上限
    include_condo_fees = False  # 共益費含む
    free_rent = False           # フリーレント有り
    without_deposit = None      # 敷金・礼金・保証金なし
    layout_types = None         # 間取タイプ
    only_first_floor = False    # 1階
    over_second_floor = False   # 2階以上
    only_top_floor = False      # 最上階・上階無し
    directions = None           # 開口向き
    gas_kitchen = False         # ガスキッチン
    separate = False            # バストイレ別
    free_internet = False       # インターネット無料
    indoor_washer = False       # 室内洗濯機可
    pet = False                 # ペット可
    instrument = False          # 楽器可
    live_together = False       # 同居可
    children = False            # 子供可
    room_share = False          # ルームシェア可
    non_japanese = False        # 外国人可
    new_student = False         # 新入生予約可
    office_use = False          # 事務所利用可

    system_kitchen = False      # システムキッチン
    washstand = False           # 独立洗面台（シャンプードレッサー含む）
    aircon = False              # エアコン
    auto_lock = False           # オートロック
    designers = False           # デザイナーズマンション
    elevator = False            # エレベータ
    delivery_box = False        # 宅配ボックス
    reheating_bath = False      # 追い焚き風呂
    washing_toilet = False      # 温水洗浄便座
    tv_intercom = False         # TV付インターフォン
    loft = False                # ロフト
    renovation = False          # リノベーション
    diy = False                 # DIY可
    walk_in_closet = False      # ウォークインクローゼット
    barrier_free = False        # バリアフリー
    garbage_box_24 = False      # 24時間ゴミ出し

    tenant_furnished_shop = False   # 居抜き店舗
    tenant_skeleton = False         # スケルトン
    tenant_restaurant = False       # 飲食可
    tenant_office = False           # 事務所向け
    tenant_first_floor = False      # 1階店舗
    tenant_soho = False             # SOHO
    tenant_residence = False        # 住宅付店舗

    odr = None                      # 並び順

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
        self.elementary_school = UrlParamHelper.get_id_param('schl', url_params)   # 小学校区ID
        self.building_types = UrlParamHelper.get_id_array_param('b_tp', url_params)    # 建物種別ID
        self.building_age = UrlParamHelper.get_int_param('b_age', url_params)   # 築年数
        self.with_garage = UrlParamHelper.get_bool_param('grg', url_params)     # 駐車場有り
        self.with_bike_parking = UrlParamHelper.get_bool_param('bike', url_params)      # 駐輪場有り
        self.rent_lower = UrlParamHelper.get_int_param('l_rnt', url_params)     # 賃料下限
        self.rent_upper = UrlParamHelper.get_int_param('u_rnt', url_params)      # 賃料上限
        self.include_condo_fees = UrlParamHelper.get_bool_param('in_cnd', url_params)   # 賃料条件に共益費含む
        self.free_rent = UrlParamHelper.get_bool_param('f_rnt', url_params)     # フリーレント有り
        self.without_deposit = UrlParamHelper.get_bool_param('no_dp', url_params)       # 敷金・礼金・保証金無し
        self.layout_types = UrlParamHelper.get_id_array_param('lay', url_params)       # 間取り種別ID
        self.only_first_floor = UrlParamHelper.get_bool_param('1_flr', url_params)      # 1階のみ
        self.over_second_floor = UrlParamHelper.get_bool_param('2_flr', url_params)     # 2階以上
        self.directions = UrlParamHelper.get_id_array_param('dir', url_params)     # 開口向きID
        self.gas_kitchen = UrlParamHelper.get_bool_param('g_kn', url_params)        # ガスキッチン
        self.separate = UrlParamHelper.get_bool_param('sep', url_params)        # バストイレ別
        self.free_internet = UrlParamHelper.get_bool_param('net_fr', url_params)        # インターネット無料
        self.indoor_washer = UrlParamHelper.get_bool_param('in_wsh', url_params)        # 室内洗濯機設置可
        self.pet = UrlParamHelper.get_bool_param('pet', url_params)        # ペット可
        self.instrument = UrlParamHelper.get_bool_param('inst', url_params)        # 楽器
        self.live_together = UrlParamHelper.get_bool_param('live_2', url_params)        # 同居可
        self.children = UrlParamHelper.get_bool_param('chld', url_params)        # 子供可
        self.room_share = UrlParamHelper.get_bool_param('r_shr', url_params)        # ルームシェア可
        self.non_japanese = UrlParamHelper.get_bool_param('no_jp', url_params)        # 外国人可
        self.new_student = UrlParamHelper.get_bool_param('new_std', url_params)        # 新入生予約可
        self.office_use = UrlParamHelper.get_bool_param('offc', url_params)        # 事務所利用可
        self.only_top_floor = UrlParamHelper.get_bool_param('t_flr', url_params)        # 最上階・上階無し
        self.system_kitchen = UrlParamHelper.get_bool_param('s_kn', url_params)        # システムキッチン
        self.washstand = UrlParamHelper.get_bool_param('wshstd', url_params)        # 独立洗面台（シャンプードレッサー含む）
        self.aircon = UrlParamHelper.get_bool_param('air', url_params)        # エアコン
        self.auto_lock = UrlParamHelper.get_bool_param('a_lck', url_params)        # オートロック
        self.designers = UrlParamHelper.get_bool_param('dsnr', url_params)        # デザイナーズ
        self.elevator = UrlParamHelper.get_bool_param('elv', url_params)        # エレベータ
        self.delivery_box = UrlParamHelper.get_bool_param('dlvr', url_params)        # 宅配ボックス
        self.reheating_bath = UrlParamHelper.get_bool_param('rh_bth', url_params)        # 追い焚き風呂
        self.washing_toilet = UrlParamHelper.get_bool_param('wsh_wc', url_params)        # 温水洗浄便座
        self.tv_intercom = UrlParamHelper.get_bool_param('tv_phn', url_params)        # TV付インターフォン
        self.loft = UrlParamHelper.get_bool_param('loft', url_params)        # ロフト
        self.renovation = UrlParamHelper.get_bool_param('reno', url_params)        # リノベーション
        self.diy = UrlParamHelper.get_bool_param('diy', url_params)        # DIY可
        self.walk_in_closet = UrlParamHelper.get_bool_param('wic', url_params)        # ウォークインクローゼット
        self.barrier_free = UrlParamHelper.get_bool_param('br_fr', url_params)        # バリアフリー
        self.garbage_box_24 = UrlParamHelper.get_bool_param('gbg24', url_params)        # 24時間ゴミ出し可
        self.tenant_furnished_shop = UrlParamHelper.get_bool_param('tnt_fnsh', url_params)        # 居抜き店舗
        self.tenant_skeleton = UrlParamHelper.get_bool_param('tnt_skl', url_params)        # スケルトン
        self.tenant_restaurant = UrlParamHelper.get_bool_param('tnt_rst', url_params)        # 飲食可
        self.tenant_office = UrlParamHelper.get_bool_param('tnt_offc', url_params)        # 事務所向け
        self.tenant_first_floor = UrlParamHelper.get_bool_param('tnt_fst', url_params)        # 1階店舗
        self.tenant_soho = UrlParamHelper.get_bool_param('tnt_soho', url_params)        # SOHO
        self.tenant_residence = UrlParamHelper.get_bool_param('tnt_rsdc', url_params)        # 住宅付店舗
        self.odr = UrlParamHelper.get_order_param('odr', url_params)      # 並び順

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

    @property
    def order_is_rent(self):
        """賃料順"""
        ans = False
        if self.odr == 'rent':
            ans = True
        return ans

    @property
    def order_is_rent_desc(self):
        """賃料の高い順"""
        ans = False
        if self.odr == 'rent_desc':
            ans = True
        return ans

    @property
    def order_is_large(self):
        """専有面積の広い順"""
        ans = False
        if self.odr == 'large':
            ans = True
        return ans

    @property
    def order_is_build(self):
        """築年月の新しい順"""
        ans = False
        if self.odr == 'build':
            ans = True
        return ans

    @property
    def order_is_new_arrival(self):
        """新着順"""
        ans = False
        if self.odr == 'new_arr':
            ans = True
        return ans

    """
    FROM句用SQL
    """
    def get_no_limit_sql(self, is_building):
        ans = None
        if not self.no_limited:
            ans = ' INNER JOIN management_type ON building.management_type_id = management_type.id'
            ans += ' AND ('
            ans += 'management_type.is_own = TRUE'
            ans += ' OR management_type.is_entrusted = TRUE'

            if is_building:
                ans += ' OR management_type.is_condo_management = TRUE'
            else:
                ans += ' OR (management_type.is_condo_management = TRUE'
                ans += ' AND (room.is_sublease = TRUE OR room.is_condo_management = TRUE OR room.is_entrusted=TRUE))'
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

    def __get_equipment_sql(self, equipment_ids, is_building, is_residential):
        """設備用内部メソッド"""
        target_table = 'room'
        target_field = 'room_id'
        if is_building:
            target_table = 'building'
            target_field = 'building_id'

        ans = ' INNER JOIN ('
        ans += 'SELECT room_equipment.{0}'.format(target_field)
        ans += ' FROM room_equipment'
        ans += ' INNER JOIN room ON room_equipment.room_id = room.id'
        ans += ' INNER JOIN room_status ON room.room_status_id = room_status.id AND room_status.for_rent = TRUE'

        ans += ' INNER JOIN rental_type ON room.rental_type_id = rental_type.id'
        if is_residential:
            ans += ' AND rental_type.is_residential = TRUE'
        else:
            ans += ' AND rental_type.is_non_residential = TRUE'

        ans += ' WHERE room_equipment.equipment_id IN ({0})'.format(','.join(map(str, equipment_ids)))
        ans += ' GROUP BY room_equipment.{0}'.format(target_field)
        ans += ') equipment_{0} ON equipment_{0}.{1} = {2}.id'.format(
            '_'.join(map(str, equipment_ids)),
            target_field,
            target_table
        )
        return ans

    def get_only_top_floor_sql(self, is_building, is_residential):
        """最上階・上階無し"""
        ans = None
        target_ids = (111060, 111061,)      # 最上階・上階無しは設備データから取得
        if self.only_top_floor:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_system_kitchen_sql(self, is_building, is_residential):
        """システムキッチン条件"""
        ans = None
        target_ids = (101010, )
        if self.system_kitchen:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_washstand_sql(self, is_building, is_residential):
        """独立洗面台条件"""
        ans = None
        target_ids = (103010, 103011, )
        if self.washstand:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_aircon_sql(self, is_building, is_residential):
        """エアコン"""
        ans = None
        target_ids = (105010, )
        if self.aircon:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_auto_lock_sql(self, is_building, is_residential):
        """オートロック"""
        ans = None
        target_ids = (113010, )
        if self.auto_lock:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_designers_sql(self, is_building, is_residential):
        """デザイナーズ"""
        ans = None
        target_ids = (202010, )
        if self.designers:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_elevator_sql(self, is_building, is_residential):
        """エレベータ"""
        ans = None
        target_ids = (201010, )
        if self.elevator:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_delivery_box_sql(self, is_building, is_residential):
        """宅配ボックス"""
        ans = None
        target_ids = (201020, )
        if self.delivery_box:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_reheating_bath_sql(self, is_building, is_residential):
        """追い焚き風呂"""
        ans = None
        target_ids = (102040, )
        if self.reheating_bath:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_washing_toilet_sql(self, is_building, is_residential):
        """温水洗浄便座"""
        ans = None
        target_ids = (104010, )
        if self.washing_toilet:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_tv_intercom_sql(self, is_building, is_residential):
        """TV付インターフォン"""
        ans = None
        target_ids = (107100, )
        if self.tv_intercom:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_loft_sql(self, is_building, is_residential):
        """ロフト"""
        ans = None
        target_ids = (110010, )
        if self.loft:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_renovation_sql(self, is_building, is_residential):
        """リノベーション"""
        ans = None
        target_ids = (111010, )
        if self.renovation:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_diy_sql(self, is_building, is_residential):
        """DIY可"""
        ans = None
        target_ids = (114020, )
        if self.diy:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_walk_in_closet_sql(self, is_building, is_residential):
        """ウォークインクローゼット"""
        ans = None
        target_ids = (109020, )
        if self.walk_in_closet:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_barrier_free_sql(self, is_building, is_residential):
        """バリアフリー"""
        ans = None
        target_ids = (111020, )
        if self.barrier_free:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_garbage_box_24_sql(self, is_building, is_residential):
        """24時間ゴミ出し可"""
        ans = None
        target_ids = (201100, )
        if self.garbage_box_24:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=is_residential,
            )
        return ans

    def get_tenant_furnished_shop_sql(self, is_building):
        """居抜き店舗"""
        ans = None
        target_ids = (301010, )
        if self.tenant_furnished_shop:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=False,
            )
        return ans

    def get_tenant_skeleton_sql(self, is_building):
        """スケルトン"""
        ans = None
        target_ids = (301020, )
        if self.tenant_skeleton:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=False,
            )
        return ans

    def get_tenant_restaurant_sql(self, is_building):
        """飲食可"""
        ans = None
        target_ids = (301040, )
        if self.tenant_restaurant:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=False,
            )
        return ans

    def get_tenant_office_sql(self, is_building):
        """事務所向け"""
        ans = None
        target_ids = (301050, )
        if self.tenant_office:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=False,
            )
        return ans

    def get_tenant_first_floor_sql(self, is_building):
        """1階店舗"""
        ans = None
        target_ids = (301030, )
        if self.tenant_first_floor:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=False,
            )
        return ans

    def get_tenant_soho_sql(self, is_building):
        """SOHO"""
        ans = None
        target_ids = (301060, )
        if self.tenant_soho:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=False,
            )
        return ans

    def get_tenant_residence_sql(self, is_building):
        """住宅付店舗"""
        ans = None
        target_ids = (301070, )
        if self.tenant_residence:
            ans = self.__get_equipment_sql(
                equipment_ids=target_ids,
                is_building=is_building,
                is_residential=False,
            )
        return ans

    def get_building_room_sql(self, is_residential):
        """建物並び順処理用"""
        ans = None
        if self.order_is_rent:
            ans = ' INNER JOIN ('
            ans += 'SELECT room.building_id'
            ans += ', MIN(room.rent) AS rent'
            ans += ' FROM room'
            ans += ' INNER JOIN room_status ON room.room_status_id = room_status.id'
            ans += ' INNER JOIN rental_type ON room.rental_type_id = rental_type.id'
            ans += ' WHERE room_status.for_rent = TRUE'
            if is_residential:
                ans += ' AND rental_type.is_residential = TRUE'
            else:
                ans += ' AND rental_type.is_non_residential = TRUE'
            ans += ' GROUP BY room.building_id'
            ans += ') room ON room.building_id = building.id'
        elif self.order_is_rent_desc:
            ans = ' INNER JOIN ('
            ans += 'SELECT room.building_id'
            ans += ', MAX(room.rent) AS rent'
            ans += ' FROM room'
            ans += ' INNER JOIN room_status ON room.room_status_id = room_status.id'
            ans += ' INNER JOIN rental_type ON room.rental_type_id = rental_type.id'
            ans += ' WHERE room_status.for_rent = TRUE'
            if is_residential:
                ans += ' AND rental_type.is_residential = TRUE'
            else:
                ans += ' AND rental_type.is_non_residential = TRUE'
            ans += ' GROUP BY room.building_id'
            ans += ') room ON room.building_id = building.id'
        elif self.order_is_large:
            ans = ' INNER JOIN ('
            ans += 'SELECT room.building_id'
            ans += ', MAX(room.room_area) AS room_area'
            ans += ' FROM room'
            ans += ' INNER JOIN room_status ON room.room_status_id = room_status.id'
            ans += ' INNER JOIN rental_type ON room.rental_type_id = rental_type.id'
            ans += ' WHERE room_status.for_rent = TRUE'
            if is_residential:
                ans += ' AND rental_type.is_residential = TRUE'
            else:
                ans += ' AND rental_type.is_non_residential = TRUE'
            ans += ' GROUP BY room.building_id'
            ans += ') room ON room.building_id = building.id'
        return ans

    def get_new_arrival_sql(self, is_building, is_residential):
        """新着日時"""
        ans = None
        if self.order_is_new_arrival:
            target_table = 'room'
            target_field = 'room_id'
            target_room_field = 'id'
            if is_building:
                target_table = 'building'
                target_field = 'building_id'
                target_room_field = 'building_id'

            ans = ' INNER JOIN ('
            ans += 'SELECT room.{0} AS {1}'.format(target_room_field, target_field)
            ans += ', MAX('
            ans += 'CASE WHEN room_status_log.created_at IS NULL THEN room.created_at'
            ans += ' ELSE room_status_log.created_at END'
            ans += ') AS arrival_at'        # 部屋状況履歴の最新作成日時が無い場合は部屋の作成日時
            ans += ' FROM room'
            ans += ' INNER JOIN room_status ON room.room_status_id = room_status_id'
            ans += ' AND room_status.for_rent=TRUE'
            ans += ' INNER JOIN rental_type ON room.rental_type_id = rental_type.id'
            if is_residential:
                ans += ' AND rental_type.is_residential = TRUE'
            else:
                ans += ' AND rental_type.is_non_residential = TRUE'
            ans += ' LEFT JOIN ('
            ans += 'SELECT room_status_log.room_id'
            ans += ', MAX(room_status_log.created_at) AS created_at'
            ans += ' FROM room_status_log'
            ans += ' INNER JOIN room_status ON room_status_log.room_status_id = room_status_id'
            ans += ' AND room_status.for_rent=TRUE'
            ans += ' GROUP BY room_status_log.room_id'
            ans += ') room_status_log ON room_status_log.room_id = room.id'
            ans += ' GROUP BY room.{0}'.format(target_room_field)
            ans += ') arrival_time ON arrival_time.{0} = {1}.id'.format(
                target_field,
                target_table,
            )

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

    def get_elementary_school_sql(self, params):
        """小学校区"""
        ans = None
        if self.elementary_school:
            ans = 'building.elementary_school_id = %(elementary_school)s'
            params['elementary_school'] = self.elementary_school
        return ans

    def get_building_types_sql(self, params):
        """建物種別"""
        ans = None
        if self.building_types:
            targets = self.__get_id_targets('building_type', self.building_types, params)
            ans = 'building.building_type_id IN ({0})'.format(targets)
        return ans

    def get_building_age_sql(self):
        """築年数"""
        ans = None
        if xint(self.building_age) > 0:
            build_year = datetime.date.today().year - self.building_age
            build_month = datetime.date.today().month
            ans = '(building.build_year > {0} OR building.build_year = {0} AND building.build_month > {1})'.format(
                build_year,
                build_month,
            )
        return ans

    def get_with_garage_sql(self):
        """駐車場有り"""
        ans = None
        if self.with_garage:
            ans = 'garage_type.is_exist = TRUE'
        return ans

    def get_with_bike_parking_sql(self):
        """駐輪場有り"""
        ans = None
        if self.with_bike_parking:
            ans = 'bike_parking_type.is_exist = TRUE'
        return ans

    def get_rent_sql(self, params):
        """賃料・共益費含む"""
        ans = None
        if self.include_condo_fees:
            if xint(self.rent_lower) > 0:
                ans = '(room.condo_fees_type_id = 10 AND (room.rent + room.condo_fees) >= %(rent_lower)s'
                ans += ' OR room.condo_fees_type_id != 10 AND room.rent >= %(rent_lower)s)'
                params['rent_lower'] = self.rent_lower
            if xint(self.rent_upper) > 0:
                ans = '(room.condo_fees_type_id = 10 AND (room.rent + room.condo_fees) <= %(rent_upper)s'
                ans += ' OR room.condo_fees_type_id != 10 AND room.rent <= %(rent_upper)s)'
                params['rent_upper'] = self.rent_upper
        else:
            if xint(self.rent_lower) > 0:
                ans = 'room.rent >= %(rent_lower)s'
                params['rent_lower'] = self.rent_lower
            if xint(self.rent_upper) > 0:
                ans = 'room.rent <= %(rent_upper)s'
                params['rent_upper'] = self.rent_upper
        return ans

    def get_free_rent_sql(self):
        """フリーレント有り"""
        ans = None
        if self.free_rent:
            ans = 'room.free_rent_type_id != 0'
        return ans

    def get_without_deposit_sql(self):
        """敷金・礼金・保証金無し"""
        ans = None
        if self.without_deposit:
            ans = '('
            ans += 'room.deposit_notation_id1 = 1'      # 保証金表記1が「無し」
            ans += ' AND room.deposit_notation_id2 IN (0, 1)'      # 保証金表記2が「無し」か「不明」
            ans += ' AND room.key_money_notation_id1 = 1'      # 一時金表記1が「無し」
            ans += ' AND room.key_money_notation_id2 IN (0, 1)'      # 一時金表記2が「無し」か「不明」
            ans += ')'
        return ans

    def get_layout_types_sql(self, params):
        """間取り種別"""
        ans = None
        if self.layout_types:
            targets = self.__get_id_targets('layout_type', self.layout_types, params)
            ans = 'room.layout_type_id IN ({0})'.format(targets)
        return ans

    def get_only_first_floor_sql(self):
        """1階のみ"""
        ans = None
        if self.only_first_floor:
            ans = 'room.room_floor = 1'
        return ans

    def get_over_second_floor_sql(self):
        """2階以上"""
        ans = None
        if self.over_second_floor:
            ans = 'room.room_floor > 1'
        return ans

    def get_directions_sql(self, params):
        """開口向き"""
        ans = None
        if self.directions:
            targets = self.__get_id_targets('direction', self.directions, params)
            ans = 'room.direction_id IN ({0})'.format(targets)
        return ans

    def get_gas_kitchen_sql(self):
        """ガスキッチン"""
        ans = None
        if self.gas_kitchen:
            ans = 'room.kitchen_range_type_id = 10'
        return ans

    def get_separate_sql(self):
        """バストイレ別"""
        ans = None
        if self.separate:
            ans = 'room.bath_type_id = 3'
        return ans

    def get_free_internet_sql(self):
        """インターネット無料"""
        ans = None
        if self.free_internet:
            ans = 'room.internet_type_id = 1'
        return ans

    def get_indoor_washer_sql(self):
        """室内洗濯機設置可"""
        ans = None
        if self.indoor_washer:
            ans = 'room.washer_type_id = 10'
        return ans

    def get_pet_sql(self):
        """ペット可"""
        ans = None
        if self.pet:
            ans = 'pet_type.is_ok = TRUE'
        return ans

    def get_instrument_sql(self):
        """楽器可"""
        ans = None
        if self.instrument:
            ans = 'room.instrument_type_id = 1'
        return ans

    def get_live_together_sql(self):
        """同居可"""
        ans = None
        if self.live_together:
            ans = 'room.live_together_type_id = 1'
        return ans

    def get_children_sql(self):
        """子供可"""
        ans = None
        if self.children:
            ans = 'room.children_type_id = 1'
        return ans

    def get_room_share_sql(self):
        """ルームシェア可"""
        ans = None
        if self.room_share:
            ans = 'room.share_type_id = 1'
        return ans

    def get_non_japanese_sql(self):
        """外国人可"""
        ans = None
        if self.non_japanese:
            ans = 'room.non_japanese_type_id = 1'
        return ans

    def get_new_student_sql(self):
        """新入生予約可"""
        ans = None
        if self.new_student:
            ans = 'room.new_student_type_id = 1'
        return ans

    def get_office_use_sql(self):
        """事務所利用可"""
        ans = None
        if self.office_use:
            ans = 'room.office_use_type_id = 1'
        return ans

    """
    ORDER BY句用SQL
    """
    def get_order_by_sql(self):
        """並び順"""
        ans = None
        if self.order_is_rent:
            ans = 'room.rent'
        elif self.order_is_rent_desc:
            ans = 'room.rent DESC'
        elif self.order_is_large:
            ans = 'room.room_area DESC'
        elif self.order_is_build:
            ans = 'building.build_year DESC, building.build_month DESC'
        elif self.order_is_new_arrival:
            ans = 'arrival_time.arrival_at DESC'
        return ans

    """
    内部メソッド
    """
    @classmethod
    def __get_id_targets(cls, id_name, id_list, params):
        ans = ''
        if id_list:
            counter = 1
            for item in id_list:
                param_name = '{0}_{1}'.format(id_name, counter)
                if counter > 1:
                    ans += ','
                ans += '%({0})s'.format(param_name)
                params[param_name] = item
                counter += 1
        return ans
