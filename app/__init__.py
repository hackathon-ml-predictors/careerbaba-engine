from flask import Flask

from .careerbaba_bp import careerbaba_bp
# from .extensions import jarvis
from .extensions import db

__all__ = ['create_app']

DEFAULT_BLUEPRINTS = (
    careerbaba_bp,
)


def create_app(config=None, blueprints=None):
    """Create Flask app.

    """

    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(__name__, instance_relative_config=True)
    configure_app(app, config)
    configure_blueprints(app, blueprints)
    configure_extensions(app)

    return app

def configure_app(app, config=None):
    """ Configure application.

    """

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

def configure_extensions(app):
    """ Configure extensions.

    """
    db.init_app(app)
    # jarvis.init_app(app)

def configure_blueprints(app, blueprints):
    """ Configure blueprints in views.

    """

    for blueprint in blueprints:
        app.register_blueprint(blueprint)