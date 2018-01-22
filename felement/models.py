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
    image = sa.Column(sa.Text, nullable=False)

    resistance_hydrolysis = sa.Column(sa.Enum(Resistance), nullable=False)
    resistance_caustic = sa.Column(sa.Enum(Resistance), nullable=False)
    resistance_oxidation = sa.Column(sa.Enum(Resistance), nullable=False)

    cleansed_ability = sa.Column(sa.Enum(Availability))
    water_repellent_impregnation = sa.Column(sa.Enum(Availability))
    protection_against_flying_sparks = sa.Column(sa.Enum(Availability))
    spark_water_protection = sa.Column(sa.Enum(Availability))
    flame_protection = sa.Column(sa.Enum(Availability))

    podged_one = sa.Column(sa.Enum(Availability))
    no_podged = sa.Column(sa.Enum(Availability))
    podged_two = sa.Column(sa.Enum(Availability))
    smooth_one = sa.Column(sa.Enum(Availability))
    smooth_two = sa.Column(sa.Enum(Availability))


class Image(db.Base):
    __tablename__ = 'images'

    id = sa.Column(sa.Integer, primary_key=True)
    url = sa.Column(sa.Text, nullable=False)

    metarial_id = sa.Column(sa.ForeignKey('materials.id'), nullable=False)

    materials = orm.relationship('Material', backref='images')
