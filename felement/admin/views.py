import os

from flask_admin.form import upload
from flask_admin.contrib import sqla

import wtforms
from wtforms import validators

from felement import db
from felement import models
from felement.app import app
from felement.app import admin


class AdminModelView(sqla.ModelView):
    def __init__(self, model=None, name=None, category=None, endpoint=None, url=None):
        super().__init__(model or self.__model__, db.session, name, category, endpoint, url)


def register(category=None, name=None, url=None, endpoint=None, **kwargs):
    def decorator(cls):
        view = cls(category=category, name=name, url=url, endpoint=endpoint, **kwargs)
        cls.instance = view
        admin.add_view(view)
        return cls
    return decorator


@register(None, 'Волокна', '/admin/fibers', 'admin.fibers')
class MaterialView(AdminModelView):
    __model__ = models.Material

    inline_models = [
        (models.Image,
         dict(
             form_label='Изображение',
             form_extra_fields=dict(
                url=upload.ImageUploadField(
                    label='Изображение',
                    base_path=os.path.join(app.config['IMG_PATH']),
                    endpoint='image',
                    validators=[validators.DataRequired()]
                )
             ))
         )]

    column_list = ('name', 'notation')
    column_labels = dict(name='Название', notation='Обозначение')

    form_args = dict(
        name=dict(label='Название волокна', validators=[validators.DataRequired()]),
        notation=dict(label='Обозначение волокна', validators=[validators.DataRequired()]),
        resistance_hydrolysis=dict(label='Сопротивление гидролизу, кислоте'),
        resistance_caustic=dict(label='Сопротивление щёлочи'),

        cleansed_ability=dict(label='Очищаемая способность'),
        water_repellent_impregnation=dict(label='Водоотталкивающая пропитка'),
        protection_against_flying_sparks=dict(label='Защита от летящих искр'),
        spark_water_protection=dict(label='Защита от летящих искр, водо-отталкивающая пропитка'),
        flame_protection=dict(label='Защита от пламени'),
        podged_one=dict(label='Подпалённая с одной стороны'),
        no_podged=dict(label='Не опалённая'),
        podged_two=dict(label='Опалённая с обеих сторон'),
        smooth_one=dict(label='Гладкая с одной стороны'),
        smooth_two=dict(label='Гладкая с обеих сторон'),
    )
    form_overrides = dict(name=wtforms.StringField, notation=wtforms.StringField)
