import logging
from flask import jsonify

from covador import opt
from covador import item
from covador.flask import json_body

from felement.common import email


logger = logging.getLogger('ajax')


@json_body(service=opt(int), mark=item(int), model=item(str), tel=item(str))
def send_email(**kwargs):
    try:
        email.send('', kwargs)
    except Exception:
        logger.exception('Send mail error')
    return jsonify(result='ok')
