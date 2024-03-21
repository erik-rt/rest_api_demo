from flask_restx import Namespace, Resource
from .models import Wallet
from flask import json, request
from flask_httpauth import HTTPBasicAuth
from datetime import datetime

api = Namespace("wallets", description="Get wallet information")
health = Namespace("health_check", description="Health check for the server")

auth = HTTPBasicAuth()

users = {
    "user": "password",
}


@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username


@health.route("/health_check")
class HealthCheck(Resource):
    @api.doc("health_check")
    def get(self):
        return json.dumps({"success": True}), 200, {"ContentType": "application/json"}


@api.route("/wallet_info")
class WalletInfo(Resource):
    @api.doc("get_wallet_info")
    @auth.login_required
    def get(self):
        wallet_address = request.args.get("wallet_address")
        from_date = request.args.get("from_date")
        to_date = request.args.get("to_date")

        from_date_obj = datetime.strptime(from_date, "%Y-%m-%d").date()
        to_date_obj = datetime.strptime(to_date, "%Y-%m-%d").date()

        wallet_info = Wallet.query.filter_by(
            wallet_address=wallet_address, from_date=from_date_obj, to_date=to_date_obj
        ).first()

        if wallet_info:
            return {
                "wallet_address": wallet_info.wallet_address,
                "from_date": wallet_info.from_date.isoformat(),
                "to_date": wallet_info.to_date.isoformat(),
                "total_points": wallet_info.total_points,
            }
        else:
            api.abort(404, "Wallet information not found")
