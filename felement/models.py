import sqlalchemy as sa
from sqlalchemy import orm

from felement import db
from felement import const


class Material(db.Base):
    __tablename__ = 'materials'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False)
    notation = sa.Column(sa.Text, nullable=False)

    has_chemical = sa.Column(sa.Boolean, default=True)
    has_physical = sa.Column(sa.Boolean, default=True)
    has_characteristics = sa.Column(sa.Boolean, default=True)

    work_temperature = sa.Column(sa.Integer)
    max_temperature = sa.Column(sa.Integer)
    resistance_load = sa.Column(sa.Enum(const.Resistance))
    resistance_abrasion = sa.Column(sa.Enum(const.Resistance))
    resistance_hydrolysis = sa.Column(sa.Enum(const.Resistance))
    resistance_acid = sa.Column(sa.Enum(const.Resistance))
    resistance_alkali = sa.Column(sa.Enum(const.Resistance))
    resistance_oxidation = sa.Column(sa.Enum(const.Resistance))
    application_of = sa.Column(sa.Text)

    water_repellent_impregnation = sa.Column(sa.Enum(const.Availability), default=const.Availability.default)
    protection_against_flying_sparks = sa.Column(sa.Enum(const.Availability), default=const.Availability.default)
    spark_water_protection = sa.Column(sa.Enum(const.Availability), default=const.Availability.default)
    flame_protection = sa.Column(sa.Enum(const.Availability), default=const.Availability.default)

    podged_one = sa.Column(sa.Enum(const.Availability), default=const.Availability.default)
    no_podged = sa.Column(sa.Enum(const.Availability), default=const.Availability.default)
    podged_two = sa.Column(sa.Enum(const.Availability), default=const.Availability.default)
    smooth_one = sa.Column(sa.Enum(const.Availability), default=const.Availability.default)
    smooth_two = sa.Column(sa.Enum(const.Availability), default=const.Availability.default)


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
