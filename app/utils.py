import pandas as pd
from .models import db


def load_csv(csv_file: str, table_name: str):
    df = pd.read_csv(csv_file)

    df["date"] = pd.to_datetime(df["date"]).dt.date

    print(f"Loading '{csv_file}' into database table '{table_name}'...")
    df.to_sql(table_name, con=db.engine, if_exists="replace", index=True)
    print("CSV data has been loaded into the database.")
    return
