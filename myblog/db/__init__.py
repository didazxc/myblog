import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash

db = SQLAlchemy()

# 导入依赖db的模型模块
from . import models


def init_db():
    db.drop_all()
    db.create_all()
    click.echo('Initialized the database.')

def update_users():
    user = models.User(id=1, name='root')
    db.session.add(user)
    # user.password = generate_password_hash('dcjBlog')
    user.password = 'dcjBlog'
    db.session.commit()
    click.echo('Users already updated.')

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    update_users()

def init_app(app):
    db.init_app(app)
    app.cli.add_command(init_db_command)
