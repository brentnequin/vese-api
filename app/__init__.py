from flask import Flask
from flask_migrate import upgrade

from app.models import db, migrate
from app.views import views
from app.api import api

def create_app(app_config=None):

    app = Flask(__name__)
    app.config.from_object(app_config or 'app.config.Config')

    db.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(views)

    return app

def run():
    app = create_app()
    app.run()

if __name__ == "__main__":

    run()