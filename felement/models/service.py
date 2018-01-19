import sqlalchemy as sa
from sqlalchemy import orm

from felement import db

#
# class Service(db.Base):
#     __tablename__ = 'vakaavto_services'
#
#     id = sa.Column(sa.Integer, primary_key=True)
#     alias = sa.Column(sa.Text, index=True, unique=True)
#     title = sa.Column(sa.Text, index=True)
#     text = sa.Column(sa.Text)
#
#     glyphicon = sa.Column(sa.Text)
#     image = sa.Column(sa.Text)
#
#     parent_id = sa.Column(sa.Integer, sa.ForeignKey('vakaavto_services.id'), nullable=True, default=None)
#     parent = orm.relationship('Service', backref='child', remote_side='Service.id')
#
#     def __str__(self):
#         return self.title
