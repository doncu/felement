import enum
import sqlalchemy as sa
from sqlalchemy import orm

from felement import db


class Resistance(enum.IntEnum):
    bad = 0
    average = 1
    good = 2


class Treatment(enum.IntEnum):
    unavailable = 0
    standard = 1
    on_request = 2


class Availability(enum.IntEnum):
    available = 0
    on_request = 1


class Material(db.Base):
    __tablename__ = 'materials'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False)
    notation = sa.Column(sa.Text, nullable=False)


class Image(db.Base):
    __tablename__ = 'images'

    id = sa.Column(sa.Integer, primary_key=True)
    url = sa.Column(sa.Text, nullable=False)

    metarial_id = sa.Column(sa.ForeignKey('materials.id'), nullable=False)

    materials = orm.relationship('Material', backref='images')


class Description(db.Base):
    __tablename__ = 'descriptions'

    id = sa.Column(sa.Integer, primary_key=True)
    field = sa.Column(sa.Text, nullable=False)
    value = sa.Column(sa.Text, nullable=False)

    metarial_id = sa.Column(sa.ForeignKey('materials.id'), nullable=False)

    materials = orm.relationship('Material', backref='paragraphs')
