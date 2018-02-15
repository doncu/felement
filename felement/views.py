import os
import imghdr
import logging

from covador import opt
from covador.flask import json_body

from flask import current_app, jsonify, render_template, send_file

from felement import db
from felement import utils
from felement import models
from felement.app import app

logger = logging.getLogger('ajax')


def index():
    base_query = db.session.query(models.Material).outerjoin(
        models.Description, models.Description.metarial_id == models.Material.id
    ).outerjoin(
        models.Image, models.Image.metarial_id == models.Material.id
    ).order_by(models.Material.id, models.Image.id, models.Description.id)

    materials = base_query.all()
    material_himical = base_query.filter(models.Material.has_chemical == True).all()
    material_phisical = base_query.filter(models.Material.has_physical == True).all()
    return render_template(
        'index.html',
        materials=materials,
        material_himical=material_himical,
        material_phisical=material_phisical
    )


def image_view(filename):
    full_path = os.path.join(app.config['IMG_PATH'], filename)
    type_ = imghdr.what(full_path)
    return send_file(full_path, mimetype='image/{}'.format(type_))


@json_body(name=opt(str), surname=opt(str), email=opt(str), tel=opt(str), message=opt(str))
def send_email(**kwargs):
    try:
        utils.send_email(
            host=current_app.config['EMAIL_SERVER'],
            log_pass=(current_app.config['EMAIL_USER'], current_app.config['EMAIL_PASS']),
            subject='Новое обращение на сайте',
            from_=current_app.config['EMAIL_FROM'],
            to=current_app.config['EMAIL_TO'],
            template='email.html',
            **kwargs
        )
    except Exception:
        logger.exception('Send mail error')
        return jsonify(result='error'), 400
    return jsonify(result='ok')
