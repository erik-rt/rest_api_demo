from app import create_app
from app.models import db
from app.utils import load_csv


def load_data():
    app = create_app()
    csv_file = "openblocklabs-dataset.csv"
    table_name = "wallet"

    with app.app_context():
        db.create_all()
        load_csv(csv_file, table_name)


if __name__ == "__main__":
    load_data()
