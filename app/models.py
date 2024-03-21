from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Wallet(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    wallet_address = db.Column(db.String(42), nullable=False)
    point_value = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)
