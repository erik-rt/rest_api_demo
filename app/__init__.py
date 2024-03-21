from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from .routes import api as api_ns, health
from .models import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wallets.db"

    db.init_app(app)

    api = Api(app, version="1.0", title="Wallet API", description="A simple Wallet API")

    api.add_namespace(api_ns, path="/api")
    api.add_namespace(health, path="/api")

    return app
