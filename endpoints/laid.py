from io import BytesIO

from PIL import Image
from flask import send_file

from utils import http
from utils.endpoint import Endpoint


class Laid(Endpoint):
    def generate(self, avatars, text, usernames):
        base = Image.open('assets/laid/laid.png').convert('RGBA')
        avatar = http.get_image(avatars[0]).resize((115, 115)).convert('RGBA')
        final_image = Image.new('RGBA', base.size)

        # Put the base over the avatar
        final_image.paste(avatar, (512, 360), avatar)
        final_image.paste(base, (0, 0), base)

        b = BytesIO()
        final_image.save(b, format='png')
        b.seek(0)
        return send_file(b, mimetype='image/png')


def setup():
    return Laid()
