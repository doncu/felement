#!/usr/bin/env python3

import os
import click

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
def initdb():
    from felement import db
    db.import_models()


if __name__ == '__main__':
    cli()
