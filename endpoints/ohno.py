from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from flask import send_file

from utils.endpoint import Endpoint
from utils.textutils import wrap


class Ohno(Endpoint):
    def generate(self, avatars, text, usernames):
        base = Image.open('assets/ohno/ohno.png').convert('RGBA')
        font = ImageFont.truetype(font='assets/fonts/sans.ttf', size=16 if len(text) > 38 else 32)
        canv = ImageDraw.Draw(base)

        text = wrap(font, text, 260)
        canv.text((340, 30), text, font=font, fill='Black')

        b = BytesIO()
        base.save(b, format='png')
        b.seek(0)
        return send_file(b, mimetype='image/png')


def setup():
    return Ohno()
