import os
import imghdr
import logging

from sqlalchemy import orm

from covador import opt
from covador.flask import json_body

from flask import current_app, jsonify, render_template, send_file

from felement import db
from felement import utils
from felement import models
from felement.app import app

logger = logging.getLogger('ajax')


def index():
    materials = db.session.query(models.Material).options(orm.joinedload('images'), orm.joinedload('paragraphs')).all()
    return render_template('index.html', materials=materials)


def image_view(filename):
    full_path = os.path.join(app.config['IMG_PATH'], filename)
    type_ = imghdr.what(full_path)
    return send_file(full_path, mimetype='image/{}'.format(type_))


@json_body(name=opt(str), surname=opt(str), email=opt(str), tel=opt(str), message=opt(str))
def send_email(**kwargs):
    try:
        utils.send_email(
            host=current_app.config['EMAIL_HOST'],
            log_pass=(current_app.config['EMAIL_USER'], current_app.config['EMAIL_PASS']),
            subject='Новое обращение на сайте',
            from_=current_app.config['EMAIL_FROM'],
            to=current_app.config['EMAIL_TO'],
            template='email.html',
            **kwargs
        )
    except Exception:
        logger.exception('Send mail error')
    return jsonify(result='ok')
