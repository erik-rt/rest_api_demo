from app import create_app
from app.models import db
from app.utils import load_csv
from dotenv import load_dotenv

app = create_app()
csv_file = "openblocklabs-dataset.csv"

if __name__ == "__main__":
    load_dotenv()
    with app.app_context():
        db.create_all()

        load_csv(csv_file, "wallet")
    app.run(debug=True)
