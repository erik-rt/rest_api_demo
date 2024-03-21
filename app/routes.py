from .models import Wallet
from .models import db
from flask import jsonify, request
from flask_httpauth import HTTPTokenAuth
from flask_restx import Namespace, Resource
import os

api = Namespace("wallets", description="Get wallet information")
health = Namespace("health_check", description="Health check for the server")

auth = HTTPTokenAuth(scheme="Bearer")

tokens = {os.getenv("BEARER_TOKEN"): "user"}


@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]


@health.route("/health_check")
class HealthCheck(Resource):
    def get(self):
        return jsonify(success=True)


@api.route("/wallet")
class WalletInfo(Resource):
    @auth.login_required
    def get(self):
        wallet_address = request.args.get("wallet_address")
        from_date = request.args.get("from_date")
        to_date = request.args.get("to_date")

        if not wallet_address or not from_date or not to_date:
            return {
                "error": "Missing wallet_address, from_date, or to_date parameter"
            }, 400

        try:
            total_points = (
                db.session.query(db.func.sum(Wallet.point_value))
                .filter(
                    Wallet.wallet_address == wallet_address,
                    Wallet.date >= from_date,
                    Wallet.date <= to_date,
                )
                .scalar()
            )

            # If no records found, return 0
            total_points = total_points if total_points is not None else 0

            return {
                "wallet_address": wallet_address,
                "from_date": from_date,
                "to_date": to_date,
                "total_points": total_points,
            }
        except Exception as e:
            return {"error": str(e)}, 500
