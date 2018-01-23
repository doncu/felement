import sqlalchemy as sa

from felement import db


# class HowTo(db.Base):
#     __tablename__ = 'vakaavto_howto'
#
#     id = sa.Column(sa.Integer, primary_key=True)
#     title = sa.Column(sa.Text, index=True)
#     text = sa.Column(sa.Text)
#
#     def __str__(self):
#         return self.title