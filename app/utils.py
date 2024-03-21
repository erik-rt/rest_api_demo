import pandas as pd
from .models import db


def load_csv(csv_file: str, table_name: str):
    df = pd.read_csv(csv_file)

    df["date"] = pd.to_datetime(df["date"]).dt.date

    print("Loading CSV data into database...")
    df.to_sql(table_name, con=db.engine, if_exists="replace", index=True)
    print("Data loaded")
    return
