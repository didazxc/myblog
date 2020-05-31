# -*- coding:utf-8 -*-
import click
import os
import waitress
from . import create_app
from .db import init_db,update_users


@click.group()
def cli():
    '''myblog is a blog web'''

@cli.command()
@click.option('-h','--host',default='0.0.0.0',type=str,show_default=True)
@click.option('-p','--port',default=80,type=int,show_default=True)
def serve(host,port):
    '''serve in waitress'''
    waitress.serve(create_app(), host=host, port=port)

@cli.command()
@click.option('-h','--host',default='0.0.0.0',type=str,show_default=True)
@click.option('-p','--port',default=80,type=int,show_default=True)
def test(host,port):
    '''in development env'''
    os.environ['FLASK_ENV']='development'
    app = create_app()
    app.run(debug=True, host=host, port=port)

@cli.group()
def deploy():
    '''deploy this web'''

@deploy.command('init-db')
def deploy_init_db():
    app = create_app()
    with app.app_context():
        click.echo(app.instance_path)
        click.echo(os.path.join(app.instance_path, 'myblog.sqlite'))
        init_db()
        update_users()

@deploy.command('update-users')
def deploy_update_users():
    with create_app().app_context():
        update_users()

def main():
    cli()
