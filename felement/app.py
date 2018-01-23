import datetime as dt
import os

from flask import Flask
from flask_admin import Admin

from felement import const
from felement import settings

conf = settings.SETTINGS_MAP[os.environ['SETTINGS']]
app = Flask(
    __name__,
    template_folder=conf.TEMPLATE_FOLDER,
    static_url_path=conf.STATIC_URL_PATH,
    static_folder=conf.STATIC_FOLDER
)
app.config.from_object(conf)

admin = Admin(app, name='admin')


@app.teardown_request
def remove_session(*args):
    from felement import db
    db.session.rollback()
    db.session.remove()


app.add_template_global(dt.datetime.now, name='now')
app.add_template_global(const.Resistance_TEXT, name='Resistance_TEXT')
app.add_template_global(const.Availability_TEXT, name='Availability_TEXT')

import felement.urls
import felement.admin.views
