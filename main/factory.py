from flask import Flask
from .core import db, guard
from .helpers import register_blueprints
from .settings import DevelopementConfig
from .models import User

import os


def create_app(package_name, package_path, settings_override=None,
               register_security_blueprint=True):
    """
    Returns a :class:`Flask` application instance configured with common
    functionality for the main platform.
    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    :param register_security_blueprint: flag to specify if the Flask-Security
                                        Blueprint should be registered. Defaults
                                        to `True`.
    """
    app = Flask(package_name, instance_relative_config=True)

    # Set app variables based in the environment
    app.config.from_object('main.settings.DevelopementConfig')

    # Override setting with settings_override values
    # app.config.from_object(settings_override)

    # Initialize a local database for the app
    db.init_app(app)

    with app.app_context():

      # Initialize the flask-praetorian instance for the app
      guard.init_app(app, User)

      # Registre all blueprints in the package_name
      register_blueprints(app, package_name, package_path)

      return app
