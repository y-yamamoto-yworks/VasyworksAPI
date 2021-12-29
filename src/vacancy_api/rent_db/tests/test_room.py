"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from datetime import date
from django.db import transaction
from django.conf import settings
from rent_db.models import Room
import warnings


class RoomModelTest(TestCase):
    """
    部屋モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.room = Room.objects.get(pk=3)      # 表示項目確認用マンション DEMO1号室

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_room_equipments(self):
        room_equipment = self.room.equipments.first()
        self.assertEqual(room_equipment.equipment.name, '2口コンロ付')

    def test_room_movies(self):
        movie = self.room.movies.first()
        self.assertEqual(movie.movie_type.name, '室内')

    def test_room_panoramas(self):
        panorama = self.room.panoramas.first()
        self.assertEqual(panorama.panorama_type.name, '居室（洋室）')

    def test_room_pictures(self):
        picture = self.room.pictures.first()
        self.assertEqual(picture.picture_type.name, '間取図')

    def test_room_floor_text(self):
        self.assertEqual(self.room.room_floor_text, '1階')

    def test_rent_text(self):
        self.assertEqual(self.room.rent_text, '52,000円 ～ 53,000円')

    def test_condo_fees_text(self):
        self.assertEqual(self.room.condo_fees_text, '3,000円')

    def test_water_cost_text(self):
        self.assertEqual(self.room.water_cost_text, '2,000円（税込）')

    def test_payment_type_text(self):
        self.assertEqual(self.room.payment_type_text, '振替')

    def test_payment_fee_type_text(self):
        self.assertEqual(self.room.payment_fee_type_text, '振替手数料')

    def test_payment_fee_text(self):
        self.assertEqual(self.room.payment_fee_text, '300円（税別）')

    def test_free_rent_text(self):
        self.assertEqual(self.room.free_rent_text, '1ヶ月')

    def test_monthly_cost_texts(self):
        self.assertEqual(self.room.monthly_cost_text1, '1,000円（税別）')
        self.assertEqual(self.room.monthly_cost_text2, '500円（税込）')
        self.assertEqual(self.room.monthly_cost_text3, '2,000円（税別）')
        self.assertIsNone(self.room.monthly_cost_text4)
        self.assertIsNone(self.room.monthly_cost_text5)
        self.assertIsNone(self.room.monthly_cost_text6)
        self.assertIsNone(self.room.monthly_cost_text7)
        self.assertIsNone(self.room.monthly_cost_text8)
        self.assertIsNone(self.room.monthly_cost_text9)
        self.assertIsNone(self.room.monthly_cost_text10)

    def test_deposit_type_texts(self):
        self.assertEqual(self.room.deposit_type_text1, '敷金')
        self.assertIsNone(self.room.deposit_type_text2)

    def test_deposit_texts(self):
        self.assertEqual(self.room.deposit_text1, '賃料 1ヶ月')
        self.assertIsNone(self.room.deposit_text2)

    def test_key_money_type_texts(self):
        self.assertEqual(self.room.key_money_type_text1, '礼金')
        self.assertIsNone(self.room.key_money_type_text2)

    def test_key_money_texts(self):
        self.assertEqual(self.room.key_money_text1, '賃料 1ヶ月')
        self.assertIsNone(self.room.key_money_text2)

    def test_insurance_type_text(self):
        self.assertEqual(self.room.insurance_type_text, '指定')

    def test_insurance_company_text(self):
        self.assertEqual(self.room.insurance_company_text, '部屋火災保険会社DEMO')

    def test_insurance_text(self):
        self.assertEqual(self.room.insurance_text, '2年 15,000円（税込）')

    def test_guarantee_type_text(self):
        self.assertEqual(self.room.guarantee_type_text, '必須')

    def test_document_cost_text(self):
        self.assertEqual(self.room.document_cost_text, '8,000円（税込）')

    def test_key_change_cost_text(self):
        self.assertEqual(self.room.key_change_cost_text, '15,000円（税別）')

    def test_initial_cost_texts(self):
        self.assertEqual(self.room.initial_cost_text1, '5,000円（税別）')
        self.assertEqual(self.room.initial_cost_text2, '10,000円（税別）')
        self.assertEqual(self.room.initial_cost_text3, '500円（税別）')
        self.assertIsNone(self.room.initial_cost_text4)
        self.assertIsNone(self.room.initial_cost_text5)
        self.assertIsNone(self.room.initial_cost_text6)
        self.assertIsNone(self.room.initial_cost_text7)
        self.assertIsNone(self.room.initial_cost_text8)
        self.assertIsNone(self.room.initial_cost_text9)
        self.assertIsNone(self.room.initial_cost_text10)

    def test_rental_type_text(self):
        self.assertEqual(self.room.rental_type_text, '普通借家')

    def test_rental_type_short_text(self):
        self.assertEqual(self.room.rental_type_short_text, '普通借家')

    def test_contract_span_text(self):
        self.assertEqual(self.room.contract_span_text, '2年')

    def test_renewal_fee_text(self):
        self.assertEqual(self.room.renewal_fee_text, '新賃料の1ヶ月')

    def test_renewal_charge_text(self):
        self.assertEqual(self.room.renewal_charge_text, '10,000円（税別）')

    def test_recontract_fee_text(self):
        self.assertIsNone(self.room.recontract_fee_text)

    def test_cancel_notice_limit_text(self):
        self.assertEqual(self.room.cancel_notice_limit_text, '2ヶ月前')

    def test_cleaning_cost_text(self):
        self.assertEqual(self.room.cleaning_cost_text, '敷金相殺 15,000円（税別）')

    def test_room_area_text(self):
        self.assertEqual(self.room.room_area_text, '40.55')

    def test_balcony_type_text(self):
        self.assertEqual(self.room.balcony_type_text, 'ベランダ')

    def test_balcony_area_text(self):
        self.assertEqual(self.room.balcony_area_text, '7')

    def test_layout_type_text(self):
        self.assertEqual(self.room.layout_type_text, '3DK')

    def test_layout_detail_text(self):
        self.assertEqual(self.room.layout_detail_text, '洋6帖×和6帖×DK4.5帖')

    def test_direction_text(self):
        self.assertEqual(self.room.direction_text, '南')

    def test_room_status_text(self):
        self.assertEqual(self.room.room_status_text, '空室')

    def test_vacancy_status_text(self):
        self.assertEqual(self.room.vacancy_status_text, '空き予定')

    def test_live_start_date_text(self):
        self.assertIsNone(self.room.live_start_date_text)

    def test_cancel_scheduled_date_text(self):
        self.assertIsNone(self.room.cancel_scheduled_date_text)

    def test_reform_year_month(self):
        self.assertEqual(self.room.reform_year_month, '2020年9月')

    def test_electric_text(self):
        self.assertEqual(self.room.electric_text, '関西電力')

    def test_gas_text(self):
        self.assertEqual(self.room.gas_text, '都市ガス')

    def test_bath_text(self):
        self.assertEqual(self.room.bath_text, 'バストイレ別')

    def test_toilet_text(self):
        self.assertEqual(self.room.toilet_text, '洋式')

    def test_kitchen_range_text(self):
        self.assertEqual(self.room.kitchen_range_text, 'ガスキッチン')

    def test_internet_text(self):
        self.assertEqual(self.room.internet_text, 'インターネット無料')

    def test_washer_text(self):
        self.assertEqual(self.room.washer_text, '室内設置可')

    def test_pet_text(self):
        self.assertEqual(self.room.pet_text, '犬猫可')

    def test_equipments_text(self):
        self.assertEqual(self.room.equipments_text, '2口コンロ付・高温差し湯式・エアコン・防犯カメラ・24時間ゴミ出し可')

    def test_equipments_short_text(self):
        self.assertEqual(self.room.equipments_short_text, '2口コンロ付・高温差し湯・エアコン・防犯カメラ・24時間ゴミ出し可')

    def test_instrument_type_text(self):
        self.assertEqual(self.room.instrument_type_text, '応相談')

    def test_live_together_type_text(self):
        self.assertEqual(self.room.live_together_type_text, '可')

    def test_children_type_text(self):
        self.assertEqual(self.room.children_type_text, '可')

    def test_share_type_text(self):
        self.assertEqual(self.room.share_type_text, '応相談')

    def test_non_japanese_type_text(self):
        self.assertEqual(self.room.non_japanese_type_text, '応相談')

    def test_only_woman_type_text(self):
        self.assertIsNone(self.room.only_woman_type_text)

    def test_only_man_type_text(self):
        self.assertIsNone(self.room.only_man_type_text)

    def test_corp_contract_type_text(self):
        self.assertEqual(self.room.corp_contract_type_text, '応相談')

    def test_student_type_text(self):
        self.assertEqual(self.room.student_type_text, '応相談')

    def test_new_student_type_text(self):
        self.assertEqual(self.room.new_student_type_text, '応相談')

    def test_office_use_type_text(self):
        self.assertEqual(self.room.office_use_type_text, '不可')

    def test_updated_date(self):
        self.assertTrue(isinstance(self.room.updated_date, date))

    def test_get_vacancy_room_condition(self):
        query = Room.get_vacancy_room_condition(False, True, False)
        rooms = self.room.building.rooms.filter(query).all()
        self.assertEqual(len(rooms), 3)
        query = Room.get_vacancy_room_condition(True, True, False)
        rooms = self.room.building.rooms.filter(query).all()
        self.assertEqual(len(rooms), 3)
        query = Room.get_vacancy_room_condition(False, False, True)
        rooms = self.room.building.rooms.filter(query).all()
        self.assertEqual(len(rooms), 1)
        query = Room.get_vacancy_room_condition(True, False, True)
        rooms = self.room.building.rooms.filter(query).all()
        self.assertEqual(len(rooms), 1)
