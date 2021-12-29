"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.conf import settings
from urllib.parse import urljoin
import warnings
import os
from lib.data_helper import DataHelper
from rent_db.models import *


class DataHelperHelperTest(TestCase):
    """
    データヘルパークラスのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

    def test_get_address_text(self):
        self.assertIsNone(
            DataHelper.get_address_text(
                Pref.objects.get(pk=0),    # 不明
                City.objects.get(pk=26104),      # 京都市中京区
                '上本能寺前町',      # 町名
                '488番地',        # 番地
                '',     # 棟名
            ),
        )
        self.assertEqual(
            DataHelper.get_address_text(
                Pref.objects.get(pk=26),    # 京都府
                City.objects.get(pk=0),      # 不明
                '上本能寺前町',      # 町名
                '488番地',        # 番地
                '',     # 棟名
            ),
            '京都府',
        )
        self.assertEqual(
            DataHelper.get_address_text(
                Pref.objects.get(pk=26),    # 京都府
                City.objects.get(pk=26104),      # 京都市中京区
                '上本能寺前町',      # 町名
                '488番地',        # 番地
                '',     # 棟名
            ),
            '京都府京都市中京区上本能寺前町488番地',
        )
        self.assertEqual(
            DataHelper.get_address_text(
                Pref.objects.get(pk=26),    # 京都府
                City.objects.get(pk=26104),      # 京都市中京区
                '上本能寺前町',  # 町名
                '488番地',  # 番地
                'A棟',  # 棟名
            ),
            '京都府京都市中京区上本能寺前町488番地 A棟',
        )

    def test_get_area_text(self):
        self.assertIsNone(
            DataHelper.get_area_text(
                Area.objects.get(pk=0),
            ),
        )
        self.assertEqual(
            DataHelper.get_area_text(
                Area.objects.get(pk=26001),
            ),
            '上賀茂',
        )

    def test_get_nearest_station_text(self):
        self.assertIsNone(
            DataHelper.get_nearest_station_text(
                ArrivalType.objects.get(pk=1),      # 徒歩
                Station.objects.get(pk=0),       # 不明
                5,      # 駅到着時間
                None,   # バス停名
                None,   # バス停到着時間
            ),
        )
        self.assertEqual(
            DataHelper.get_nearest_station_text(
                ArrivalType.objects.get(pk=1),      # 徒歩
                Station.objects.get(pk=1310),       # 地下鉄東西線　京都市役所前
                5,      # 駅到着時間
                None,  # バス停名
                None,  # バス停到着時間
            ),
            '地下鉄東西線 京都市役所前駅まで徒歩5分',
        )
        self.assertEqual(
            DataHelper.get_nearest_station_text(
                ArrivalType.objects.get(pk=2),      # バス
                Station.objects.get(pk=1310),       # 地下鉄東西線　京都市役所前
                10,      # 駅到着時間
                '河原町今出川',  # バス停名
                3,  # バス停到着時間
            ),
            '地下鉄東西線 京都市役所前駅までバス10分（バス停 河原町今出川まで徒歩3分）',
        )

    def test_get_rent_text(self):
        self.assertIsNone(
            DataHelper.get_rent_text(
                False,      # 賃料非表示ならTrue
                0,
                0,
                TaxType.objects.get(pk=3),   # 非課税
            ),
        )
        self.assertEqual(
            DataHelper.get_rent_text(
                True,  # 賃料非表示ならTrue
                0,
                0,
                TaxType.objects.get(pk=3),  # 非課税
            ),
            '相談',
        )
        self.assertEqual(
            DataHelper.get_rent_text(
                False,  # 賃料非表示ならTrue
                52000,
                0,
                TaxType.objects.get(pk=3),  # 非課税
            ),
            '52,000円',
        )
        self.assertEqual(
            DataHelper.get_rent_text(
                False,  # 賃料非表示ならTrue
                52000,
                52000,
                TaxType.objects.get(pk=3),  # 非課税
            ),
            '52,000円',
        )
        self.assertEqual(
            DataHelper.get_rent_text(
                False,  # 賃料非表示ならTrue
                52000,
                55000,
                TaxType.objects.get(pk=3),  # 非課税
            ),
            '52,000円 ～ 55,000円',
        )
        self.assertEqual(
            DataHelper.get_rent_text(
                False,  # 賃料非表示ならTrue
                52000,
                55000,
                TaxType.objects.get(pk=1),    # 税別
            ),
            '52,000円 ～ 55,000円（税別）',
        )

    def test_get_condo_fees_text(self):
        self.assertIsNone(
            DataHelper.get_condo_fees_text(
                CondoFeesType.objects.get(pk=0),    # 不明
                0,
                TaxType.objects.get(pk=3),  # 非課税
            )
        )
        self.assertEqual(
            DataHelper.get_condo_fees_text(
                CondoFeesType.objects.get(pk=10),   # 共益費金額
                5000,
                TaxType.objects.get(pk=3),  # 非課税
            ),
            '5,000円'
        )
        self.assertEqual(
            DataHelper.get_condo_fees_text(
                CondoFeesType.objects.get(pk=10),   # 共益費金額
                5000,
                TaxType.objects.get(pk=1),  # 税別
            ),
            '5,000円（税別）'
        )
        self.assertEqual(
            DataHelper.get_condo_fees_text(
                CondoFeesType.objects.get(pk=20),   # 共益費込み
                0,
                TaxType.objects.get(pk=3),  # 非課税
            ),
            '込み'
        )

    def test_get_water_cost_text(self):
        self.assertIsNone(
            DataHelper.get_water_cost_text(
                WaterCostType.objects.get(pk=0),    # 不明
                0,
                TaxType.objects.get(pk=0),  # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_water_cost_text(
                WaterCostType.objects.get(pk=10),   # 実費
                0,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '実費',
        )
        self.assertEqual(
            DataHelper.get_water_cost_text(
                WaterCostType.objects.get(pk=20),   # 金額
                2000,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '2,000円',
        )
        self.assertEqual(
            DataHelper.get_water_cost_text(
                WaterCostType.objects.get(pk=20),   # 金額
                2000,
                TaxType.objects.get(pk=2),  # 税込
            ),
            '2,000円（税込）',
        )
        self.assertEqual(
            DataHelper.get_water_cost_text(
                WaterCostType.objects.get(pk=30),   # 共益費込
                0,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '共益費込',
        )

    def test_get_payment_type_text(self):
        self.assertIsNone(
            DataHelper.get_payment_type_text(
                PaymentType.objects.get(pk=0),      # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_payment_type_text(
                PaymentType.objects.get(pk=1),
            ),
            '振込',
        )

    def test_get_payment_fee_type_text(self):
        self.assertIsNone(
            DataHelper.get_payment_fee_type_text(
                PaymentFeeType.objects.get(pk=0),      # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_payment_fee_type_text(
                PaymentFeeType.objects.get(pk=10),
            ),
            '振込手数料',
        )

    def test_get_payment_fee_text(self):
        self.assertIsNone(
            DataHelper.get_payment_fee_text(
                PaymentFeeType.objects.get(pk=0),  # 不明
                0,
                TaxType.objects.get(pk=1),  # 税別
            ),
        )
        self.assertEqual(
            DataHelper.get_payment_fee_text(
                PaymentFeeType.objects.get(pk=10),
                300,
                TaxType.objects.get(pk=1),  # 税別
            ),
            '300円（税別）',
        )

    def test_get_free_rent_text(self):
        self.assertIsNone(
            DataHelper.get_free_rent_text(
                FreeRentType.objects.get(pk=0),     # 無し
                0,
                0,
                0,
            ),
        )
        self.assertEqual(
            DataHelper.get_free_rent_text(
                FreeRentType.objects.get(pk=1),     # 月数
                1,
                2000,
                3,
            ),
            '1ヶ月',
        )
        self.assertEqual(
            DataHelper.get_free_rent_text(
                FreeRentType.objects.get(pk=2),     # 期限月
                1,
                2000,
                3,
            ),
            '2000年3月まで',
        )

    def test_get_cost_text(self):
        self.assertIsNone(
            DataHelper.get_cost_text(
                None,   # 名称無し
                3000,
                TaxType.objects.get(pk=1),    # 税別
            ),
        )
        self.assertIsNone(
            DataHelper.get_cost_text(
                'インターネット利用料',   # 名称無し
                0,
                TaxType.objects.get(pk=1),    # 税別
            ),
        )
        self.assertEqual(
            DataHelper.get_cost_text(
                'インターネット利用料',   # 名称無し
                3000,
                TaxType.objects.get(pk=0),    # 不明
            ),
            '3,000円',
        )
        self.assertEqual(
            DataHelper.get_cost_text(
                'インターネット利用料',   # 名称無し
                3000,
                TaxType.objects.get(pk=1),    # 税別
            ),
            '3,000円（税別）',
        )

    def test_get_is_exist_text(self):
        self.assertIsNone(
            DataHelper.get_is_exists_text(
                Existence.objects.get(pk=0),    # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_is_exists_text(
                Existence.objects.get(pk=1),    # 有り
            ),
            '有り',
        )
        self.assertIsNone(
            DataHelper.get_is_exists_text(
                Existence.objects.get(pk=2),    # 無し
            ),
        )

    def test_get_existence_cost_text(self):
        self.assertIsNone(
            DataHelper.get_existence_cost_text(
                Existence.objects.get(pk=0),    # 不明
                1000,
                TaxType.objects.get(pk=1),  # 税別
            ),
        )
        self.assertEqual(
            DataHelper.get_existence_cost_text(
                Existence.objects.get(pk=1),    # 有り
                1000,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '1,000円',
        )
        self.assertEqual(
            DataHelper.get_existence_cost_text(
                Existence.objects.get(pk=1),    # 有り
                1000,
                TaxType.objects.get(pk=1),  # 税別
            ),
            '1,000円（税別）',
        )
        self.assertIsNone(
            DataHelper.get_existence_cost_text(
                Existence.objects.get(pk=2),    # 無し
                1000,
                TaxType.objects.get(pk=1),  # 税別
            ),
        )

    def test_get_deposit_type_text(self):
        self.assertIsNone(
            DataHelper.get_deposit_type_text(
                DepositType.objects.get(pk=0),      # 指定無し
            ),
        )
        self.assertEqual(
            DataHelper.get_deposit_type_text(
                DepositType.objects.get(pk=10),
            ),
            '敷金',
        )

    def test_get_deposit_text(self):
        self.assertIsNone(
            DataHelper.get_deposit_text(
                DepositType.objects.get(pk=0),      # 指定無し
                DepositNotation.objects.get(pk=2),   # 金額
                58000,
                TaxType.objects.get(pk=3),  # 非課税
            ),
        )
        self.assertIsNone(
            DataHelper.get_deposit_text(
                DepositType.objects.get(pk=10),      # 敷金
                DepositNotation.objects.get(pk=0),   # 不明
                58000,
                TaxType.objects.get(pk=3),  # 非課税
            ),
        )
        self.assertEqual(
            DataHelper.get_deposit_text(
                DepositType.objects.get(pk=10),      # 敷金
                DepositNotation.objects.get(pk=2),   # 金額
                58000,
                TaxType.objects.get(pk=3),  # 非課税
            ),
            '58,000円',
        )
        self.assertEqual(
            DataHelper.get_deposit_text(
                DepositType.objects.get(pk=10),      # 敷金
                DepositNotation.objects.get(pk=2),   # 金額
                58000,
                TaxType.objects.get(pk=1),  # 税別
            ),
            '58,000円（税別）',
        )
        self.assertEqual(
            DataHelper.get_deposit_text(
                DepositType.objects.get(pk=20),      # 保証金
                DepositNotation.objects.get(pk=3),   # 賃料nヶ月
                2,
                TaxType.objects.get(pk=3),  # 非課税
            ),
            '賃料 2ヶ月',
        )
        self.assertEqual(
            DataHelper.get_deposit_text(
                DepositType.objects.get(pk=20),      # 保証金
                DepositNotation.objects.get(pk=5),   # 変動
                0,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '変動',
        )

    def test_get_key_money_type_text(self):
        self.assertIsNone(
            DataHelper.get_key_money_type_text(
                KeyMoneyType.objects.get(pk=0),      # 指定無し
            ),
        )
        self.assertEqual(
            DataHelper.get_key_money_type_text(
                KeyMoneyType.objects.get(pk=10),
            ),
            '礼金',
        )

    def test_get_key_money_text(self):
        self.assertIsNone(
            DataHelper.get_key_money_text(
                KeyMoneyType.objects.get(pk=0),      # 指定無し
                KeyMoneyNotation.objects.get(pk=2),   # 金額
                58000,
                TaxType.objects.get(pk=3),  # 非課税
            ),
        )
        self.assertIsNone(
            DataHelper.get_key_money_text(
                KeyMoneyType.objects.get(pk=10),      # 礼金
                KeyMoneyNotation.objects.get(pk=0),   # 不明
                58000,
                TaxType.objects.get(pk=3),  # 非課税
            ),
        )
        self.assertEqual(
            DataHelper.get_key_money_text(
                KeyMoneyType.objects.get(pk=10),      # 礼金
                KeyMoneyNotation.objects.get(pk=2),   # 金額
                58000,
                TaxType.objects.get(pk=3),  # 非課税
            ),
            '58,000円',
        )
        self.assertEqual(
            DataHelper.get_key_money_text(
                KeyMoneyType.objects.get(pk=10),      # 礼金
                KeyMoneyNotation.objects.get(pk=2),   # 金額
                58000,
                TaxType.objects.get(pk=1),  # 税別
            ),
            '58,000円（税別）',
        )
        self.assertEqual(
            DataHelper.get_key_money_text(
                KeyMoneyType.objects.get(pk=20),      # 解約引
                KeyMoneyNotation.objects.get(pk=3),   # 賃料nヶ月
                2,
                TaxType.objects.get(pk=3),  # 非課税
            ),
            '賃料 2ヶ月',
        )
        self.assertEqual(
            DataHelper.get_key_money_text(
                KeyMoneyType.objects.get(pk=20),      # 解約引
                KeyMoneyNotation.objects.get(pk=5),   # 変動
                0,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '変動',
        )

    def test_get_building_type_text(self):
        self.assertIsNone(
            DataHelper.get_building_type_text(
                BuildingType.objects.get(pk=0),     # 不明
                '',
            ),
        )
        self.assertEqual(
            DataHelper.get_building_type_text(
                BuildingType.objects.get(pk=10),
                '',
            ),
            'マンション',
        )
        self.assertEqual(
            DataHelper.get_building_type_text(
                BuildingType.objects.get(pk=31),
                'タウンハウス',
            ),
            'テラスハウス（タウンハウス）',
        )

    def test_get_build_year_month_text(self):
        self.assertIsNone(
            DataHelper.get_build_year_month_text(0, 0),
        )
        self.assertIsNone(
            DataHelper.get_build_year_month_text(0, 1),
        )
        self.assertEqual(
            DataHelper.get_build_year_month_text(2000, 0),
            '2000年築',
        )
        self.assertEqual(
            DataHelper.get_build_year_month_text(2000, 3),
            '2000年3月築',
        )

    def test_get_structure_text(self):
        self.assertIsNone(
            DataHelper.get_structure_text(
                Structure.objects.get(pk=0),    # 不明
                '',
            ),
        )
        self.assertEqual(
            DataHelper.get_structure_text(
                Structure.objects.get(pk=10),   # 鉄骨鉄筋コンクリート造
                '',
            ),
            '鉄骨鉄筋コンクリート造',
        )
        self.assertEqual(
            DataHelper.get_structure_text(
                Structure.objects.get(pk=10),   # 鉄骨鉄筋コンクリート造
                '一部鉄筋コンクリート造',
            ),
            '鉄骨鉄筋コンクリート造（一部鉄筋コンクリート造）',
        )

    def test_get_school_text(self):
        self.assertIsNone(
            DataHelper.get_school_text(
                ElementarySchool.objects.get(pk=0),     # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_school_text(
                ElementarySchool.objects.get(pk=1),
            ),
            '葵',
        )
        self.assertIsNone(
            DataHelper.get_school_text(
                JuniorHighSchool.objects.get(pk=0),     # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_school_text(
                JuniorHighSchool.objects.get(pk=1),
            ),
            '旭丘',
        )

    def test_get_school_distance_text(self):
        self.assertIsNone(
            DataHelper.get_school_distance_text(
                ElementarySchool.objects.get(pk=0),  # 不明
                1000,
            ),
        )
        self.assertIsNone(
            DataHelper.get_school_distance_text(
                ElementarySchool.objects.get(pk=1),     # 葵
                0,
            ),
        )
        self.assertEqual(
            DataHelper.get_school_distance_text(
                ElementarySchool.objects.get(pk=1),     # 葵
                1000,
            ),
            '1000m',
        )
        self.assertIsNone(
            DataHelper.get_school_distance_text(
                JuniorHighSchool.objects.get(pk=0),  # 不明
                1000,
            ),
        )
        self.assertIsNone(
            DataHelper.get_school_distance_text(
                JuniorHighSchool.objects.get(pk=1),     # 旭丘
                0,
            ),
        )
        self.assertEqual(
            DataHelper.get_school_distance_text(
                JuniorHighSchool.objects.get(pk=1),     # 旭丘
                1000
            ),
            '1000m'
        )

    def test_get_staff_text(self):
        self.assertIsNone(
            DataHelper.get_staff_text(
                Staff.objects.get(pk=0),
            ),
        )
        self.assertEqual(
            DataHelper.get_staff_text(
                Staff.objects.get(pk=2),     # 管理 太郎
            ),
            '管理（賃貸管理部）',
        )

    def test_get_room_floor_text(self):
        self.assertIsNone(
            DataHelper.get_room_floor_text(0),
        )
        self.assertEqual(
            DataHelper.get_room_floor_text(5),
            '5階',
        )
        self.assertEqual(
            DataHelper.get_room_floor_text(-1),
            '地下1階',
        )

    def test_get_direction_text(self):
        self.assertIsNone(
            DataHelper.get_direction_text(
                Direction.objects.get(pk=0),    # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_direction_text(
                Direction.objects.get(pk=5),
            ),
            '南',
        )

    def test_get_room_status_text(self):
        self.assertIsNone(
            DataHelper.get_room_status_text(
                RoomStatus.objects.get(pk=0),   # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_room_status_text(
                RoomStatus.objects.get(pk=1),
            ),
            '空室',
        )

    def test_get_vacancy_status_text(self):
        self.assertIsNone(
            DataHelper.get_vacancy_status_text(
                RoomStatus.objects.get(pk=0),       # 不明
                VacancyStatus.objects.get(pk=10),   # 即入居可
            ),
        )
        self.assertIsNone(
            DataHelper.get_vacancy_status_text(
                RoomStatus.objects.get(pk=1),       # 空室
                VacancyStatus.objects.get(pk=0),    # 不明
            ),
        )
        self.assertIsNone(
            DataHelper.get_vacancy_status_text(
                RoomStatus.objects.get(pk=1),       # 空室
                VacancyStatus.objects.get(pk=90),   # その他
            ),
        )
        self.assertIsNone(
            DataHelper.get_vacancy_status_text(
                RoomStatus.objects.get(pk=2),       # 契約済
                VacancyStatus.objects.get(pk=10),    # 即入居可
            ),
        )
        self.assertEqual(
            DataHelper.get_vacancy_status_text(
                RoomStatus.objects.get(pk=1),       # 空室
                VacancyStatus.objects.get(pk=10),    # 即入居可
            ),
            '即入居可',
        )

    def test_get_room_area_text(self):
        self.assertEqual(DataHelper.get_room_area_text(0), '0')
        self.assertEqual(DataHelper.get_room_area_text(15), '15')
        self.assertEqual(DataHelper.get_room_area_text(15.0), '15')
        self.assertEqual(DataHelper.get_room_area_text(15.5), '15.5')
        self.assertEqual(DataHelper.get_room_area_text(15.25), '15.25')
        self.assertEqual(DataHelper.get_room_area_text('0'), '0')
        self.assertEqual(DataHelper.get_room_area_text('15'), '15')
        self.assertEqual(DataHelper.get_room_area_text('15.0'), '15')
        self.assertEqual(DataHelper.get_room_area_text('15.00'), '15')
        self.assertEqual(DataHelper.get_room_area_text('15.5'), '15.5')
        self.assertEqual(DataHelper.get_room_area_text('15.25'), '15.25')

    def test_get_balcony_type_text(self):
        self.assertIsNone(
            DataHelper.get_balcony_type_text(
                BalconyType.objects.get(pk=0),  # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_balcony_type_text(
                BalconyType.objects.get(pk=2),
            ),
            'ベランダ',
        )

    def test_get_balcony_area_text(self):
        self.assertIsNone(
            DataHelper.get_balcony_area_text(
                BalconyType.objects.get(pk=0),
                8.5
            ),
        )

        balcony_type = BalconyType.objects.get(pk=2)  # ベランダ
        self.assertEqual(DataHelper.get_balcony_area_text(balcony_type, 0), '0')
        self.assertEqual(DataHelper.get_balcony_area_text(balcony_type, 8), '8')
        self.assertEqual(DataHelper.get_balcony_area_text(balcony_type, 8.0), '8')
        self.assertEqual(DataHelper.get_balcony_area_text(balcony_type, 8.5), '8.5')
        self.assertEqual(DataHelper.get_balcony_area_text(balcony_type, 8.25), '8.25')
        self.assertEqual(DataHelper.get_balcony_area_text(balcony_type, '0'), '0')
        self.assertEqual(DataHelper.get_balcony_area_text(balcony_type, '8'), '8')
        self.assertEqual(DataHelper.get_balcony_area_text(balcony_type, '8.0'), '8')
        self.assertEqual(DataHelper.get_balcony_area_text(balcony_type, '8.00'), '8')
        self.assertEqual(DataHelper.get_balcony_area_text(balcony_type, '8.5'), '8.5')
        self.assertEqual(DataHelper.get_balcony_area_text(balcony_type, '8.25'), '8.25')

    def test_get_layout_type_text(self):
        self.assertIsNone(
            DataHelper.get_layout_type_text(
                LayoutType.objects.get(pk=0),   # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_layout_type_text(
                LayoutType.objects.get(pk=330),
            ),
            '3LDK',
        )

    def test_get_layout_detail_text(self):
        self.assertIsNone(DataHelper.get_layout_detail_text(None))
        self.assertEqual(
            DataHelper.get_layout_detail_text(
                Room.objects.get(pk=3)  # 表示確認用マンション DEMO1 号室
            ),
            '洋6帖×和6帖×DK4.5帖',
        )

    def test_get_reform_year_month(self):
        self.assertIsNone(
            DataHelper.get_reform_year_month(0, 0),
        )
        self.assertIsNone(
            DataHelper.get_reform_year_month(0, 1),
        )
        self.assertEqual(
            DataHelper.get_reform_year_month(2000, 0),
            '2000年',
        )
        self.assertEqual(
            DataHelper.get_reform_year_month(2000, 3),
            '2000年3月',
        )

    def test_get_electric_text(self):
        self.assertIsNone(
            DataHelper.get_electric_text(
                ElectricType.objects.get(pk=0),     # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_electric_text(
                ElectricType.objects.get(pk=20),
            ),
            '関西電力',
        )

    def test_get_gas_text(self):
        self.assertIsNone(
            DataHelper.get_gas_text(
                GasType.objects.get(pk=0),      # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_gas_text(
                GasType.objects.get(pk=10),
            ),
            '都市ガス',
        )

    def test_get_bath_text(self):
        self.assertIsNone(
            DataHelper.get_bath_text(
                BathType.objects.get(pk=0),    # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_bath_text(
                BathType.objects.get(pk=3),
            ),
            'バストイレ別',
        )

    def test_get_toilet_text(self):
        self.assertIsNone(
            DataHelper.get_toilet_text(
                ToiletType.objects.get(pk=0),    # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_toilet_text(
                ToiletType.objects.get(pk=1),
            ),
            '洋式',
        )

    def test_get_kitchen_range_text(self):
        self.assertIsNone(
            DataHelper.get_kitchen_range_text(
                KitchenRangeType.objects.get(pk=0),    # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_kitchen_range_text(
                KitchenRangeType.objects.get(pk=10),
            ),
            'ガスキッチン',
        )

    def test_get_internet_text(self):
        self.assertIsNone(
            DataHelper.get_internet_text(
                InternetType.objects.get(pk=0),    # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_internet_text(
                InternetType.objects.get(pk=1),
            ),
            'インターネット無料',
        )

    def test_get_washer_text(self):
        self.assertIsNone(
            DataHelper.get_washer_text(
                WasherType.objects.get(pk=0),    # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_washer_text(
                WasherType.objects.get(pk=10),
            ),
            '室内設置可',
        )

    def test_get_pet_text(self):
        self.assertIsNone(
            DataHelper.get_pet_text(
                PetType.objects.get(pk=0),    # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_pet_text(
                PetType.objects.get(pk=33),
            ),
            '犬猫可',
        )

    def test_get_equipments_text(self):
        self.assertIsNone(DataHelper.get_equipments_text(None))
        self.assertEqual(
            DataHelper.get_equipments_text(
                Room.objects.get(pk=3).equipments  # 表示確認用マンション DEMO1 号室
            ),
            '2口コンロ付・高温差し湯式・エアコン・防犯カメラ・24時間ゴミ出し可',
        )

    def test_get_equipments_short_text(self):
        self.assertIsNone(DataHelper.get_equipments_short_text(None))
        self.assertEqual(
            DataHelper.get_equipments_short_text(
                Room.objects.get(pk=3).equipments  # 表示確認用マンション DEMO1 号室
            ),
            '2口コンロ付・高温差し湯・エアコン・防犯カメラ・24時間ゴミ出し可',
        )

    def test_get_allow_type_text(self):
        self.assertIsNone(
            DataHelper.get_allow_type_text(
                AllowType.objects.get(pk=0),    # 指定無し
            ),
        )
        self.assertEqual(
            DataHelper.get_allow_type_text(
                AllowType.objects.get(pk=1),
            ),
            '可',
        )

    def test_get_date_string(self):
        day = MonthDay.objects.get(pk=102)  # 上旬
        self.assertIsNone(DataHelper.get_date_string(0, 1, day))
        self.assertIsNone(DataHelper.get_date_string(2000, 0, day))
        self.assertEqual(DataHelper.get_date_string(2000, 3, None), '2000年3月')
        self.assertEqual(DataHelper.get_date_string(2000, 3, day), '2000年3月上旬')

    def test_get_rental_type_text(self):
        self.assertIsNone(
            DataHelper.get_rental_type_text(
                RentalType.objects.get(pk=0),    # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_rental_type_text(
                RentalType.objects.get(pk=12),
            ),
            '普通借家（自社所有）',
        )

    def test_get_rental_type_short_text(self):
        self.assertIsNone(
            DataHelper.get_rental_type_short_text(
                RentalType.objects.get(pk=0),    # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_rental_type_short_text(
                RentalType.objects.get(pk=12),
            ),
            '普通借家',
        )

    def test_get_contract_span_text(self):
        self.assertIsNone(DataHelper.get_contract_span_text(0, 0, False))
        self.assertEqual(DataHelper.get_contract_span_text(2, 0, False), '2年')
        self.assertEqual(DataHelper.get_contract_span_text(0, 18, False), '18ヶ月')
        self.assertEqual(DataHelper.get_contract_span_text(1, 6, False), '1年6ヶ月')
        self.assertEqual(DataHelper.get_contract_span_text(2, 0, True), '2年（自動更新）')

    def test_get_renewal_fee_text(self):
        self.assertIsNone(
            DataHelper.get_renewal_fee_text(
                RenewalFeeNotation.objects.get(pk=0),   # 不明
                63000,
                TaxType.objects.get(pk=3),  # 非課税
            ),
        )
        self.assertEqual(
            DataHelper.get_renewal_fee_text(
                RenewalFeeNotation.objects.get(pk=1),   # 無し
                0,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '無し',
        )
        self.assertEqual(
            DataHelper.get_renewal_fee_text(
                RenewalFeeNotation.objects.get(pk=2),   # 金額
                63000,
                TaxType.objects.get(pk=3),  # 非課税
            ),
            '63,000円',
        )
        self.assertEqual(
            DataHelper.get_renewal_fee_text(
                RenewalFeeNotation.objects.get(pk=2),   # 金額
                63000,
                TaxType.objects.get(pk=2),  # 税込
            ),
            '63,000円（税込）',
        )
        self.assertEqual(
            DataHelper.get_renewal_fee_text(
                RenewalFeeNotation.objects.get(pk=4),   # 新賃料nヶ月
                2,
                TaxType.objects.get(pk=3),  # 非課税
            ),
            '新賃料の2ヶ月',
        )
        self.assertEqual(
            DataHelper.get_renewal_fee_text(
                RenewalFeeNotation.objects.get(pk=4),   # 新賃料nヶ月
                2,
                TaxType.objects.get(pk=1),  # 税別
            ),
            '新賃料の2ヶ月（税別）',
        )
        self.assertEqual(
            DataHelper.get_renewal_fee_text(
                RenewalFeeNotation.objects.get(pk=6),   # 実費
                0,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '実費',
        )

    def test_get_cancel_notice_limit_text(self):
        self.assertIsNone(DataHelper.get_cancel_notice_limit_text(0))
        self.assertEqual(DataHelper.get_cancel_notice_limit_text(2), '2ヶ月前')

    def test_get_cleaning_cost_text(self):
        self.assertIsNone(
            DataHelper.get_cleaning_cost_text(
                CleaningType.objects.get(pk=0),     # 不明
                15000,
                TaxType.objects.get(pk=1),  # 税別
            ),
        )
        self.assertIsNone(
            DataHelper.get_cleaning_cost_text(
                CleaningType.objects.get(pk=1),     # 無し
                15000,
                TaxType.objects.get(pk=1),  # 税別
            ),
        )
        self.assertEqual(
            DataHelper.get_cleaning_cost_text(
                CleaningType.objects.get(pk=2),     # 無し
                15000,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '契約時支払 15,000円',
        )
        self.assertEqual(
            DataHelper.get_cleaning_cost_text(
                CleaningType.objects.get(pk=2),     # 無し
                15000,
                TaxType.objects.get(pk=1),  # 税別
            ),
            '契約時支払 15,000円（税別）',
        )

    def test_get_insurance_type_text(self):
        self.assertIsNone(
            DataHelper.get_insurance_type_text(
                InsuranceType.objects.get(pk=0),    # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_insurance_type_text(
                InsuranceType.objects.get(pk=2),    # オーナー指定
            ),
            '指定',
        )
        self.assertEqual(
            DataHelper.get_insurance_type_text(
                InsuranceType.objects.get(pk=4),    # 相談
            ),
            '相談',
        )

    def test_get_insurance_company_text(self):
        self.assertIsNone(
            DataHelper.get_insurance_company_text(
                InsuranceType.objects.get(pk=0),    # 不明
                '損保ジャパン'
            ),
        )
        self.assertEqual(
            DataHelper.get_insurance_company_text(
                InsuranceType.objects.get(pk=2),    # オーナー指定
                '損保ジャパン'
            ),
            '損保ジャパン',
        )
        self.assertIsNone(
            DataHelper.get_insurance_company_text(
                InsuranceType.objects.get(pk=9),    # 指定無し
                '損保ジャパン'
            ),
        )

    def test_get_insurance_text(self):
        self.assertIsNone(
            DataHelper.get_insurance_text(
                InsuranceType.objects.get(pk=0),    # 不明
                2,
                15000,
                TaxType.objects.get(pk=1),  # 税別
            ),
        )
        self.assertIsNone(
            DataHelper.get_insurance_text(
                InsuranceType.objects.get(pk=9),    # 指定無し
                2,
                15000,
                TaxType.objects.get(pk=1),  # 税別
            ),
        )
        self.assertEqual(
            DataHelper.get_insurance_text(
                InsuranceType.objects.get(pk=2),    # オーナー指定
                2,
                15000,
                TaxType.objects.get(pk=1),  # 税別
            ),
            '2年 15,000円（税別）',
        )

    def test_get_guarantee_type_text(self):
        self.assertIsNone(
            DataHelper.get_guarantee_type_text(
                GuaranteeType.objects.get(pk=0),    # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_guarantee_type_text(
                GuaranteeType.objects.get(pk=1),
            ),
            '必須',
        )

    def test_get_garage_type_text(self):
        self.assertEqual(
            DataHelper.get_garage_type_text(
                GarageType.objects.get(pk=0),    # 無し
            ),
            '無し',
        )
        self.assertEqual(
            DataHelper.get_garage_type_text(
                GarageType.objects.get(pk=1),
            ),
            '有料',
        )

    def test_get_garage_status_text(self):
        self.assertIsNone(
            DataHelper.get_garage_status_text(
                GarageStatus.objects.get(pk=0),    # 指定無し
            ),
        )
        self.assertEqual(
            DataHelper.get_garage_status_text(
                GarageStatus.objects.get(pk=1),
            ),
            '空き有',
        )

    def test_get_building_garage_status_text(self):
        self.assertIsNone(
            DataHelper.get_building_garage_status_text(
                GarageType.objects.get(pk=0),    # 無し
                GarageStatus.objects.get(pk=1),  # 空き有
            ),
        )
        self.assertIsNone(
            DataHelper.get_building_garage_status_text(
                GarageType.objects.get(pk=1),    # 有料
                GarageStatus.objects.get(pk=0),  # 指定無し
            ),
        )
        self.assertEqual(
            DataHelper.get_building_garage_status_text(
                GarageType.objects.get(pk=1),    # 有料
                GarageStatus.objects.get(pk=1),  # 空き有
            ),
            '空き有',
        )

    def test_get_building_garage_distance_text(self):
        self.assertIsNone(
            DataHelper.get_building_garage_status_text(
                GarageType.objects.get(pk=0),    # 無し
                800,
            ),
        )
        self.assertEqual(
            DataHelper.get_building_garage_distance_text(
                GarageType.objects.get(pk=2),    # 近隣確保
                800,
            ),
            '800m',
        )

    def test_get_building_garage_fee_text(self):
        self.assertIsNone(
            DataHelper.get_building_garage_fee_text(
                GarageType.objects.get(pk=0),    # 無し
                15000,
                0,
                TaxType.objects.get(pk=1),  # 税別
            ),
        )
        self.assertIsNone(
            DataHelper.get_building_garage_fee_text(
                GarageType.objects.get(pk=4),    # 駐車場付き
                15000,
                0,
                TaxType.objects.get(pk=1),  # 税別
            ),
        )
        self.assertEqual(
            DataHelper.get_building_garage_fee_text(
                GarageType.objects.get(pk=1),    # 有料
                15000,
                0,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '15,000円',
        )
        self.assertEqual(
            DataHelper.get_building_garage_fee_text(
                GarageType.objects.get(pk=1),    # 有料
                15000,
                15000,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '15,000円',
        )
        self.assertEqual(
            DataHelper.get_building_garage_fee_text(
                GarageType.objects.get(pk=1),    # 有料
                15000,
                18000,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '15,000円 ～ 18,000円',
        )
        self.assertEqual(
            DataHelper.get_building_garage_fee_text(
                GarageType.objects.get(pk=1),    # 有料
                15000,
                18000,
                TaxType.objects.get(pk=1),  # 税別
            ),
            '15,000円 ～ 18,000円（税別）',
        )

    def test_get_building_garage_charge_text(self):
        self.assertIsNone(
            DataHelper.get_building_garage_charge_text(
                0,
                0,
                TaxType.objects.get(pk=1),  # 税別
            ),
        )
        self.assertEqual(
            DataHelper.get_building_garage_charge_text(
                15000,
                0,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '15,000円',
        )
        self.assertEqual(
            DataHelper.get_building_garage_charge_text(
                15000,
                15000,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '15,000円',
        )
        self.assertEqual(
            DataHelper.get_building_garage_charge_text(
                15000,
                18000,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '15,000円 ～ 18,000円',
        )
        self.assertEqual(
            DataHelper.get_building_garage_charge_text(
                15000,
                18000,
                TaxType.objects.get(pk=1),  # 税別
            ),
            '15,000円 ～ 18,000円（税別）',
        )

    def test_get_bike_parking_type_text(self):
        self.assertIsNone(
            DataHelper.get_bike_parking_type_text(
                BikeParkingType.objects.get(pk=0),    # 不明
            ),
        )
        self.assertEqual(
            DataHelper.get_bike_parking_type_text(
                BikeParkingType.objects.get(pk=10),
            ),
            '無し',
        )
        self.assertEqual(
            DataHelper.get_bike_parking_type_text(
                BikeParkingType.objects.get(pk=30),
            ),
            '原付可（無料）',
        )

    def test_get_bike_parking_roof_text(self):
        self.assertIsNone(
            DataHelper.get_bike_parking_roof_text(
                BikeParkingType.objects.get(pk=0),    # 不明
                True,
            ),
        )
        self.assertIsNone(
            DataHelper.get_bike_parking_roof_text(
                BikeParkingType.objects.get(pk=30),    # 原付可（無料）
                False,
            ),
        )
        self.assertEqual(
            DataHelper.get_bike_parking_roof_text(
                BikeParkingType.objects.get(pk=30),    # 原付可（無料）
                True,
            ),
            '屋根付き',
        )

    def test_get_bike_parking_fee_text(self):
        self.assertIsNone(
            DataHelper.get_bike_parking_fee_text(
                BikeParkingType.objects.get(pk=0),    # 不明
                1000,
                0,
                TaxType.objects.get(pk=1),  # 税別
            ),
        )
        self.assertIsNone(
            DataHelper.get_bike_parking_fee_text(
                BikeParkingType.objects.get(pk=10),    # 無し
                1000,
                0,
                TaxType.objects.get(pk=1),  # 税別
            ),
        )
        self.assertIsNone(
            DataHelper.get_bike_parking_fee_text(
                BikeParkingType.objects.get(pk=30),    # 原付可（無料）
                1000,
                0,
                TaxType.objects.get(pk=1),  # 税別
            ),
        )
        self.assertEqual(
            DataHelper.get_bike_parking_fee_text(
                BikeParkingType.objects.get(pk=31),     # 原付可（有料）
                1000,
                0,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '1,000円',
        )
        self.assertEqual(
            DataHelper.get_bike_parking_fee_text(
                BikeParkingType.objects.get(pk=31),     # 原付可（有料）
                1000,
                1000,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '1,000円',
        )
        self.assertEqual(
            DataHelper.get_bike_parking_fee_text(
                BikeParkingType.objects.get(pk=31),     # 原付可（有料）
                1000,
                1500,
                TaxType.objects.get(pk=0),  # 不明
            ),
            '1,000円 ～ 1,500円',
        )
        self.assertEqual(
            DataHelper.get_bike_parking_fee_text(
                GarageType.objects.get(pk=1),    # 有料
                1000,
                1500,
                TaxType.objects.get(pk=1),  # 税別
            ),
            '1,000円 ～ 1,500円（税別）',
        )

    def test_get_garage_size_text(self):
        self.assertIsNone(DataHelper.get_garage_size_text(0, 0, 0))
        self.assertEqual(DataHelper.get_garage_size_text(3, 5, 0), '幅3m×奥行5m')
        self.assertEqual(DataHelper.get_garage_size_text(3, 0, 2), '幅3m×高さ2m')
        self.assertEqual(DataHelper.get_garage_size_text(3, 5, 2), '幅3m×奥行5m×高さ2m')
        self.assertEqual(DataHelper.get_garage_size_text(3.0, 5.0, 2.0), '幅3m×奥行5m×高さ2m')
        self.assertEqual(DataHelper.get_garage_size_text(3.5, 5.5, 2.5), '幅3.5m×奥行5.5m×高さ2.5m')
        self.assertEqual(DataHelper.get_garage_size_text(3.25, 5.25, 2.25), '幅3.25m×奥行5.25m×高さ2.25m')
        self.assertIsNone(DataHelper.get_garage_size_text('0', '0', '0'))
        self.assertEqual(DataHelper.get_garage_size_text('3', '5', '2'), '幅3m×奥行5m×高さ2m')
        self.assertEqual(DataHelper.get_garage_size_text('3.0', '5.0', '2.0'), '幅3m×奥行5m×高さ2m')
        self.assertEqual(DataHelper.get_garage_size_text('3.5', '5.5', '2.5'), '幅3.5m×奥行5.5m×高さ2.5m')
        self.assertEqual(DataHelper.get_garage_size_text('3.50', '5.50', '2.50'), '幅3.5m×奥行5.5m×高さ2.5m')
        self.assertEqual(DataHelper.get_garage_size_text('3.25', '5.25', '2.25'), '幅3.25m×奥行5.25m×高さ2.25m')
