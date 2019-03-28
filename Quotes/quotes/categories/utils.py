import os
import secrets
from quotes import create_app
from PIL import Image


def savePicture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(create_app().root_path, 'static/cat_images', picture_fn)
    form_picture.save(picture_path)
    output_size = (300, 300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn
