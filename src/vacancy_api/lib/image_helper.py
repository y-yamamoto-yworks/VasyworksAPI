"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import sys
import qrcode
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont


class ImageHelper:
    """ 画像ヘルパークラス"""

    @staticmethod
    def cache_image(src_path, cache_path, water_mark, max_size):
        """ 画像をキャッシュ """

        img = Image.open(src_path)
        w, h = img.size

        if w > max_size or h > max_size:
            if w < h:
                img_base = img.resize((int(w / h * max_size), max_size)).convert('RGBA')
            else:
                img_base = img.resize((max_size, int(h / w * max_size))).convert('RGBA')
        else:
            img_base = img.convert('RGBA')

        img_cache = img_base.convert("RGB")
        if water_mark:
            font_size = settings.WATER_MARK_FONT_SIZE
            if max_size >= settings.LARGE_IMAGE_SIZE:
                font_size = font_size * 4
            elif max_size >= settings.MEDIUM_IMAGE_SIZE:
                font_size = font_size * 2
            opacity = settings.WATER_MARK_OPACITY
            color = (255, 255, 255)

            if sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
                font_path = "C:\\WINDOWS\Fonts\\MSGOTHIC.ttc"
            elif sys.platform.startswith('darwin'):
                font_path = "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc"
            else:
                font_path = "/usr/share/fonts/ipa-gothic/ipag.ttf"

            # テキストを描画する画像オブジェクトを作成します。
            txt = Image.new('RGBA', img_base.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(txt)

            # フォントを取得します。
            fnt = ImageFont.truetype(font=font_path, size=font_size)

            # 透かし文字の横幅、縦幅を取得します。
            textw, texth = draw.textsize(water_mark, font=fnt)

            # 透かし文字を中央に入れます。
            draw.text(((img_base.width - textw) / 2, (img_base.height - texth) / 2), water_mark, font=fnt, fill=color + (opacity,))

            # 画像オブジェクトを重ねます。
            img_cache = Image.alpha_composite(img_base, txt).convert("RGB")

        # 画像を出力します。
        img_cache.save(cache_path, quality=95, optimize=True)

    @staticmethod
    def make_qrcode(data, file_path, force=False):
        """QRコード画像の作成"""
        if os.path.exists(file_path):
            if force:
                os.remove(file_path)
            else:
                return

        file_dir = os.path.dirname(file_path)
        if not os.path.isdir(file_dir):
            os.makedirs(file_dir)

        img = qrcode.make(data)
        img.save(file_path)
