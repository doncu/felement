#!/usr/bin/env python3
import os
import click
import sqlalchemy as sa

from flask.cli import FlaskGroup


def create_app(*args):
    os.environ['SETTINGS'] = 'local'
    from felement.app import app
    return app


@click.group(cls=FlaskGroup, create_app=create_app)
@click.option('--debug/--no-debug', default=True, help='Enable/disable debug mode')
def cli(debug):
    os.environ['FLASK_DEBUG'] = '1' if debug else '0'


@cli.command()
@click.option('--db-uri', help='Path where create db')
def init_db(db_uri):
    import felement.models
    from felement import db

    engine = sa.create_engine(db_uri) if db_uri else db.engine
    session = db.create_session(engine=engine)

    db.Base.metadata.create_all(engine)


if __name__ == '__main__':
    cli()
