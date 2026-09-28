import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from dotenv import load_dotenv

def load(df):
    load_dotenv()
    server = os.getenv("SERVER")
    db = os.getenv("DB")
    user = os.getenv("DB_USER")
    passwd = os.getenv("DB_PASSWORD")

    connection_string = (
        f"mssql+pyodbc://{user}:{passwd}@{server}/{db}"
        "?driver=ODBC+Driver+18+for+SQL+Server"
        "&TrustServerCertificate=yes"
    )

    engine = create_engine(connection_string)

    pd.DataFrame.to_sql(df,"Sales", con=engine, 
              if_exists="replace",
              index=False)
