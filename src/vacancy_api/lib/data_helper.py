"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.utils import timezone
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from lib.convert import *
from lib.functions import *


class DataHelper:
    """データヘルパークラス"""
    """
    所在地関連
    """
    @staticmethod
    def get_address_text(pref, city, town_address, house_no, building_no):
        ans = None
        if pref:
            ans = xstr(pref.name)
            if pref.id != 0 and city:
                ans += xstr(city.name)
                if city.id != 0:
                    ans += xstr(town_address)
                    ans += xstr(house_no)
                    if building_no:
                        ans += ' ' + xstr(building_no)
        return ans

    @staticmethod
    def get_area_text(area):
        ans = None
        if area.id != 0:
            ans = area.name
        return ans

    @staticmethod
    def get_nearest_station_text(arrival_type, station, station_time, bus_stop, bus_stop_time):
        ans = None
        if station:
            if station.id != 0:
                ans = xstr(station.railway.name) + ' ' + xstr(station.name)
                ans += '駅まで' + xstr(arrival_type.name)
                ans += xstr(station_time) + '分'
                if xint(arrival_type.id) == 2:
                    ans += '（バス停 ' + xstr(bus_stop)
                    if xint(bus_stop_time) > 0:
                        ans += 'まで徒歩' + xstr(bus_stop_time) + '分'
                    ans += '）'
        return ans

    """
    費用関連
    """
    @staticmethod
    def get_rent_text(is_hidden, rent, rent_upper, tax_type):
        ans = None

        if is_hidden:
            ans = "相談"
        elif rent > 0:
            ans = '{:,} 円'.format(rent)
            if rent_upper:
                if rent_upper > rent:
                    ans += ' 〜 {:,} 円'.format(rent_upper)
            if tax_type.text:
                ans += '（{0}）'.format(tax_type.text)

        return ans

    @staticmethod
    def get_condo_fees_text(condo_fees_type, cost, tax_type):
        ans = None
        if condo_fees_type.id != 0:
            ans = condo_fees_type.name
            if condo_fees_type.is_money:
                ans = '{:,} 円'.format(cost)
                if tax_type.text:
                    ans += '（{0}）'.format(tax_type.text)
        return ans

    @staticmethod
    def get_water_cost_text(water_cost_type, cost, tax_type):
        ans = None
        if water_cost_type.id != 0:
            ans = water_cost_type.name
            if water_cost_type.is_money:
                ans = '{:,} 円'.format(cost)
                if tax_type.text:
                    ans += '（{0}）'.format(tax_type.text)
        return ans

    @staticmethod
    def get_payment_type_text(payment_type):
        ans = None
        if payment_type.id != 0:
            ans = payment_type.name
        return ans

    @staticmethod
    def get_payment_fee_type_text(payment_fee_type):
        ans = None
        if payment_fee_type.id != 0:
            ans = payment_fee_type.name
        return ans

    @staticmethod
    def get_payment_fee_text(payment_fee_type, fee, tax_type):
        ans = None
        if payment_fee_type.id != 0:
            if payment_fee_type.is_money and fee > 0:
                ans = '{:,} 円'.format(fee)
                if tax_type.text:
                    ans += '（{0}）'.format(tax_type.text)
        return ans

    @staticmethod
    def get_free_rent_text(free_rent_type, months, limit_year, limit_month):
        ans = None
        if free_rent_type.limit_is_span:
            if months > 0:
                ans = '{0}ヶ月'.format(months)
        elif free_rent_type.limit_is_month:
            if limit_year > 0 and limit_month > 0:
                ans = '{0}年{1}月まで'.format(limit_year, limit_month)
        return ans

    @staticmethod
    def get_cost_text(cost_name, cost, tax_type):
        ans = None
        if cost_name and cost > 0:
            ans = '{:,} 円'.format(cost)
            if tax_type.text:
                ans += '({0})'.format(tax_type.text)

        return ans

    @staticmethod
    def get_is_exist_text(existence):
        ans = None
        if existence.is_exist:
            ans = existence.name
        return ans

    @staticmethod
    def get_existence_cost_text(existence, cost, tax_type):
        ans = None
        if existence.is_exists:
            ans = '{0:,} 円'.format(cost)
            if tax_type.text:
                ans += '（{0}）'.format(tax_type.text)
        return ans

    @staticmethod
    def get_deposit_type_text(deposit_type):
        ans = None
        if deposit_type.id != 0:
            ans = deposit_type.name

        return ans

    @staticmethod
    def get_deposit_text(deposit_type, notation, value, tax_type):
        ans = None

        if deposit_type.id != 0:
            if notation.is_money:
                ans = '{0:,.0f} {1}'.format(value, notation.unit)
                if tax_type.text:
                    ans = '（{0}）'.format(tax_type.text)
            elif notation.is_month:
                ans = '賃料 {0} {1}'.format(float_normalize(xfloat(value)), notation.unit)
                if tax_type.text:
                    ans = '（{0}）'.format(tax_type.text)
            elif notation.is_rate:
                ans = '賃料の {0:.0f} {1}'.format(value, notation.unit)
                if tax_type.text:
                    ans = '（{0}）'.format(tax_type.text)
            else:
                ans = '{0}'.format(notation.name)

        return ans

    @staticmethod
    def get_key_money_type_text(key_money_type):
        ans = None
        if key_money_type.id != 0:
            ans = key_money_type.name

        return ans

    @staticmethod
    def get_key_money_text(key_money_type, notation, value, tax_type):
        ans = None

        if key_money_type.id != 0:
            if notation.is_money:
                ans = '{0:,.0f} {1}'.format(value, notation.unit)
                if tax_type.text:
                    ans = '（{0}）'.format(tax_type.text)
            elif notation.is_month:
                ans = '賃料 {0} {1}'.format(float_normalize(xfloat(value)), notation.unit)
                if tax_type.text:
                    ans = '（{0}）'.format(tax_type.text)
            elif notation.is_rate:
                ans = '賃料の {0:.0f} {1}'.format(value, notation.unit)
                if tax_type.text:
                    ans = '（{0}）'.format(tax_type.text)
            else:
                ans = '{0}'.format(notation.name)

        return ans

    """
    建物、部屋情報関連
    """
    @staticmethod
    def get_building_type_text(building_type, comment=None):
        ans = None
        if building_type.id != 0:
            ans = building_type.name
            if comment:
                ans += '（{0}）'.format(comment)
        return ans

    @staticmethod
    def get_build_year_month_text(build_year, build_month):
        ans = None
        if build_year:
            ans = xstr(build_year) + '年'
            if build_month:
                ans += xstr(build_month) + '月'
            ans += '築'
        return ans

    @staticmethod
    def get_structure_text(structure, comment=None):
        ans = None
        if structure.id != 0:
            ans = structure.name
            if comment:
                ans += '（{0}）'.format(comment)

        return ans

    @staticmethod
    def get_school_text(school):
        ans = None
        if school.id != 0:
            ans = school.name
        return ans

    @staticmethod
    def get_school_distance_text(school, distance):
        ans = None
        if school.id != 0 and distance > 0:
            ans = '{0} m'.format(distance)
        return ans

    @staticmethod
    def get_staff_text(staff):
        ans = None
        if staff.id != 0:
            ans = staff.last_name
            if staff.department.id != 0:
                ans += "（{0}）".format(staff.department.department_name)
        return ans

    @staticmethod
    def get_room_floor_text(room_floor):
        ans = None
        if room_floor > 0:
            ans = '{0}階'.format(room_floor)
        elif room_floor < 0:
            ans = '地下{0}階'.format(room_floor * -1)
        return ans

    @staticmethod
    def get_direction_text(direction):
        ans = None
        if direction.id != 0:
            ans = direction.name
        return ans

    @staticmethod
    def get_room_status_text(room_status):
        ans = None
        if room_status.id != 0:
            ans = room_status.name
        return ans

    @staticmethod
    def get_vacancy_status_text(room_status, vacancy_status):
        ans = None
        if room_status.for_rent:
            if vacancy_status.id not in [0, 90]:
                ans = vacancy_status.name

        return ans

    @staticmethod
    def get_room_area_text(area):
        return float_normalize(xfloat(area))

    @staticmethod
    def get_balcony_type_text(balcony_type):
        ans = None
        if 0 < balcony_type.id < 90:
            ans = balcony_type.name
        return ans

    @staticmethod
    def get_balcony_area_text(balcony_type, area):
        ans = None
        if 0 < balcony_type.id < 90:
            ans = float_normalize(xfloat(area))
        return ans

    @staticmethod
    def get_layout_type_text(layout_type):
        ans = None
        if layout_type.id != 0:
            ans = layout_type.name
        return ans

    @staticmethod
    def get_layout_detail_text(room):
        """間取詳細テキストの取得"""
        ans = None

        if room:
            # 洋室
            if room.western_style_room1 > 0:
                ans = DataHelper.__add_layout_room('洋', room.western_style_room1, ans)
            if room.western_style_room2 > 0:
                ans = DataHelper.__add_layout_room('洋', room.western_style_room2, ans)
            if room.western_style_room3 > 0:
                ans = DataHelper.__add_layout_room('洋', room.western_style_room3, ans)
            if room.western_style_room4 > 0:
                ans = DataHelper.__add_layout_room('洋', room.western_style_room4, ans)
            if room.western_style_room5 > 0:
                ans = DataHelper.__add_layout_room('洋', room.western_style_room5, ans)
            if room.western_style_room6 > 0:
                ans = DataHelper.__add_layout_room('洋', room.western_style_room6, ans)
            if room.western_style_room7 > 0:
                ans = DataHelper.__add_layout_room('洋', room.western_style_room7, ans)
            if room.western_style_room8 > 0:
                ans = DataHelper.__add_layout_room('洋', room.western_style_room8, ans)
            if room.western_style_room9 > 0:
                ans = DataHelper.__add_layout_room('洋', room.western_style_room9, ans)
            if room.western_style_room10 > 0:
                ans = DataHelper.__add_layout_room('洋', room.western_style_room10, ans)

            # 和室
            if room.japanese_style_room1 > 0:
                ans = DataHelper.__add_layout_room('和', room.japanese_style_room1, ans)
            if room.japanese_style_room2 > 0:
                ans = DataHelper.__add_layout_room('和', room.japanese_style_room2, ans)
            if room.japanese_style_room3 > 0:
                ans = DataHelper.__add_layout_room('和', room.japanese_style_room3, ans)
            if room.japanese_style_room4 > 0:
                ans = DataHelper.__add_layout_room('和', room.japanese_style_room4, ans)
            if room.japanese_style_room5 > 0:
                ans = DataHelper.__add_layout_room('和', room.japanese_style_room5, ans)
            if room.japanese_style_room6 > 0:
                ans = DataHelper.__add_layout_room('和', room.japanese_style_room6, ans)
            if room.japanese_style_room7 > 0:
                ans = DataHelper.__add_layout_room('和', room.japanese_style_room7, ans)
            if room.japanese_style_room8 > 0:
                ans = DataHelper.__add_layout_room('和', room.japanese_style_room8, ans)
            if room.japanese_style_room9 > 0:
                ans = DataHelper.__add_layout_room('和', room.japanese_style_room9, ans)
            if room.japanese_style_room10 > 0:
                ans = DataHelper.__add_layout_room('和', room.japanese_style_room10, ans)

            # キッチン
            if room.kitchen_type1.notation:
                ans = DataHelper.__add_layout_room(room.kitchen_type1.notation, room.kitchen1, ans)
            if room.kitchen_type2.notation:
                ans = DataHelper.__add_layout_room(room.kitchen_type1.notation, room.kitchen2, ans)
            if room.kitchen_type3.notation:
                ans = DataHelper.__add_layout_room(room.kitchen_type1.notation, room.kitchen3, ans)

            # その他スペース
            space = None

            # 納戸
            if room.store_room1 > 0:
                space = DataHelper.__add_layout_space('納戸', room.store_room1, space)
            if room.store_room2 > 0:
                space = DataHelper.__add_layout_space('納戸', room.store_room2, space)
            if room.store_room3 > 0:
                space = DataHelper.__add_layout_space('納戸', room.store_room3, space)

            # ロフト
            if room.loft1 > 0:
                space = DataHelper.__add_layout_space('ロフト', room.loft1, space)
            if room.loft2 > 0:
                space = DataHelper.__add_layout_space('ロフト', room.loft2, space)

            # サンルーム
            if room.sun_room1 > 0:
                space = DataHelper.__add_layout_space('サンルーム', room.sun_room1, space)
            if room.sun_room2 > 0:
                space = DataHelper.__add_layout_space('サンルーム', room.sun_room2, space)

            if space:
                ans += ' + {0}'.format(space)

        return ans

    @staticmethod
    def __add_layout_room(type_name, area, target):
        # 洋室・和室・キッチン
        ans = target
        if area > 0:
            if ans:
                ans += '×'
            else:
                ans = ''

            ans += '{0}{1}帖'.format(type_name, float_normalize(xfloat(area)))

        return ans

    @staticmethod
    def __add_layout_space(type_name, area, target):
        # 洋室・和室・キッチン以外
        ans = target
        if area > 0:
            if ans:
                ans += '・'
            else:
                ans = ''

            ans += '{0}{1}帖'.format(type_name, float_normalize(xfloat(area)))

        return ans

    @staticmethod
    def get_reform_year_month(reform_year, reform_month):
        ans = None
        if reform_year > 0:
            ans = '{0}年'.format(reform_year)
            if 1 <= reform_month <= 12:
                ans += '{0}月'.format(reform_month)
        return ans

    @staticmethod
    def get_electric_text(electric_type):
        ans = None
        if electric_type.id != 0:
            ans = electric_type.name
        return ans

    @staticmethod
    def get_gas_text(gas_type):
        ans = None
        if gas_type.id != 0:
            ans = gas_type.name
        return ans

    @staticmethod
    def get_bath_text(bath_type):
        ans = None
        if bath_type.id != 0:
            ans = bath_type.name
        return ans

    @staticmethod
    def get_toilet_text(toilet_type):
        ans = None
        if toilet_type.id != 0:
            ans = toilet_type.name
        return ans

    @staticmethod
    def get_kitchen_range_text(kitchen_range_type):
        ans = None
        if kitchen_range_type.id != 0:
            ans = kitchen_range_type.name
        return ans

    @staticmethod
    def get_internet_text(internet_type):
        ans = None
        if internet_type.id != 0:
            ans = internet_type.name
        return ans

    @staticmethod
    def get_washer_text(washer_type):
        ans = None
        if washer_type.id != 0:
            ans = washer_type.name
        return ans

    @staticmethod
    def get_pet_text(pet_type):
        ans = None
        if pet_type.id != 0:
            ans = pet_type.name
        return ans

    @staticmethod
    def get_equipments_text(equipments):
        ans = ''
        for item in equipments:
            if not item.is_remained:
                if ans != '':
                    ans += '・'
                ans += item.equipment.name

        if ans == '':
            ans = None
        return ans

    @staticmethod
    def get_equipments_short_text(equipments):
        ans = ''
        for item in equipments:
            if not item.is_remained:
                if ans != '':
                    ans += '・'
                ans += item.equipment.short_name

        if ans == '':
            ans = None
        return ans

    @staticmethod
    def get_allow_type_text(allow_type):
        ans = None
        if allow_type.id != 0:
            ans = allow_type.name
        return ans

    """
    年・日付関連
    """
    @staticmethod
    def get_date_string(year: int, month: int, day):
        ans = None
        if year > 0 and 1 <= month <= 12 and day:
            ans = '{0}年{1}月'.format(year, month, day.name)
            if day.id != 0:
                ans += day.name

        return ans

    """
    契約・更新関連
    """
    @staticmethod
    def get_rental_type_text(rental_type):
        ans = None
        if rental_type.id != 0:
            ans = rental_type.name
        return ans

    @staticmethod
    def get_rental_type_short_text(rental_type):
        ans = None
        if rental_type.id != 0:
            ans = rental_type.short_name
        return ans

    @staticmethod
    def get_contract_span_text(contract_years, contract_months, is_auto_renewal):
        ans = None
        if contract_years > 0 or contract_months > 0:
            ans = ''
            if contract_years > 0:
                ans += '{0}年'.format(contract_years)
            if contract_months > 0:
                ans += '{0}ヶ月'.format(contract_months)

            if is_auto_renewal:
                ans += '（自動更新）'
        return ans

    @staticmethod
    def get_renewal_fee_text(renewal_fee_notation, value, tax_type):
        ans = None
        if renewal_fee_notation.is_money:
            ans = '{0:,.0f} {1}'.format(
                value,
                renewal_fee_notation.unit,
            )
            if tax_type.text:
                ans += '{0}）'.format(tax_type.text)
        elif renewal_fee_notation.is_month:
            ans = '{0}の {1} {2}'.format(
                renewal_fee_notation.header,
                float_normalize(xfloat(value)),
                renewal_fee_notation.unit,
            )
            if tax_type.text:
                ans += '（{0}）'.format(tax_type.text)
        elif renewal_fee_notation.is_rate:
            ans = '{0}の {1:.0f} {2}'.format(
                renewal_fee_notation.header,
                float_normalize(xfloat(value)),
                renewal_fee_notation.unit,
            )
            if tax_type.text:
                ans += '（{0}）'.format(tax_type.text)
        elif renewal_fee_notation.id != 0:
            ans = '{0}'.format(renewal_fee_notation.name)
        return ans

    @staticmethod
    def get_cancel_notice_limit_text(limit_months):
        ans = None
        if limit_months > 0:
            ans = '{0}ヶ月前'.format(limit_months)
        return ans

    @staticmethod
    def get_cleaning_cost_text(cleaning_type, cost, tax_type):
        ans = None
        if cleaning_type.is_paid:
            ans = cleaning_type.name
            if cleaning_type.is_money:
                ans += ' {0:,} 円'.format(cost)
                if tax_type.text:
                    ans += '（{0}）'.format(tax_type.text)
        return ans

    """
    火災保険・保証会社関連
    """
    @staticmethod
    def get_insurance_type_text(insurance_type):
        ans = None
        if insurance_type.id != 0:
            if insurance_type.is_specified:
                ans = '指定'
            else:
                ans = insurance_type.name
        return ans

    @staticmethod
    def get_insurance_company_text(insurance_type, insurance_company):
        ans = None
        if insurance_type.is_specified and insurance_company:
            ans = insurance_company
        return ans

    @staticmethod
    def get_insurance_text(insurance_type, years, fee, tax_type):
        ans = ''
        if insurance_type.is_specified:
            if years > 0:
                ans += ' {0}年'.format(years)
            if fee > 0:
                ans += ' {0:,} 円'.format(fee)
                if tax_type.text:
                    ans += '（{0}）'.format(tax_type.text)
        if ans == '':
            ans = None
        return ans

    @staticmethod
    def get_guarantee_type_text(guarantee_type):
        ans = None
        if guarantee_type.id != 0:
            ans = guarantee_type.name
        return ans

    """
    駐車場・駐輪場
    """
    @staticmethod
    def get_garage_type_text(garage_type):
        return garage_type.name

    @staticmethod
    def get_garage_status_text(garage_status):
        ans = None
        if garage_status.id != 0:
            ans = garage_status.name
        return ans

    @staticmethod
    def get_building_garage_status_text(garage_type, garage_status):
        ans = None
        if garage_type.is_exist and garage_status.id != 0:
            ans = garage_status.name
        return ans

    @staticmethod
    def get_building_garage_distance_text(garage_type, distance):
        ans = None
        if garage_type.id != 0 and distance > 0:
            ans = '{0} m'.format(distance)
        return ans

    @staticmethod
    def get_building_garage_fee_text(garage_type, fee, fee_upper, tax_type):
        ans = None
        if garage_type.is_paid:
            if fee > 0 or fee_upper > 0:
                ans = ''
                if fee > 0:
                    ans += '{0:,} 円'.format(fee)
                if fee_upper > 0 and fee_upper > fee:
                    ans += ' 〜 {0:,} 円'.format(fee_upper)
                if tax_type.text:
                    ans += ' ' + tax_type.text

                if ans == '':
                    ans = None
        return ans

    @staticmethod
    def get_building_garage_charge_text(charge, charge_upper, tax_type):
        ans = None
        if charge > 0 or charge_upper > 0:
            ans = ''
            if charge > 0:
                ans += '{0:,} 円'.format(charge)
            if charge_upper > 0 and charge_upper > charge:
                ans += ' 〜 {0:,} 円'.format(charge_upper)
            if tax_type.text:
                ans += ' ' + tax_type.text

            if ans == '':
                ans = None
        return ans

    @staticmethod
    def get_bike_parking_type_text(bike_parking_type):
        ans = None
        if bike_parking_type.id != 0:
            ans = bike_parking_type.name
        return ans

    @staticmethod
    def get_bike_parking_roof_text(bike_parking_type, roof):
        ans = None
        if bike_parking_type.is_exist and roof:
            ans = '屋根付き'
        return ans

    @staticmethod
    def get_bike_parking_fee_text(bike_parking_type, fee, fee_upper, tax_type):
        ans = None
        if bike_parking_type.id != 0:
            if bike_parking_type.is_paid:
                ans = ''
                if fee > 0:
                    ans += '{0:,} 円'.format(fee)
                if fee_upper > 0 and fee_upper > fee:
                    ans += ' 〜 {0:,} 円'.format(fee_upper)
                if tax_type.text:
                    ans += ' ' + tax_type.text

                if ans == '':
                    ans = None
        return ans

    @staticmethod
    def get_garage_size_text(width, length, height):
        ans = ''
        if width > 0:
            ans = '幅{0}m'.format(float_normalize(xfloat(width)))
        if length > 0:
            if ans != '':
                ans += '×'
            ans += '奥行{0}m'.format(float_normalize(xfloat(length)))
        if height > 0:
            if ans != '':
                ans += '×'
            ans += '高さ{0}m'.format(float_normalize(xfloat(height)))
        if ans == '':
            ans = None
        return ans
