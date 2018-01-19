import sqlalchemy as sa

from felement import db


# class AutoMark(db.Base):
#     __tablename__ = 'vakaavto_auto_mark'
#
#     id = sa.Column(sa.Integer, primary_key=True)
#     title = sa.Column(sa.Text, index=True)
#     image = sa.Column(sa.Text)
#
#     def __str__(self):
#         return self.title
