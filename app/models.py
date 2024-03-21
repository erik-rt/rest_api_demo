from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallet_address = db.Column(db.String(128), unique=True, nullable=False)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=False)
    point_value = db.Column(db.Float, nullable=False)
