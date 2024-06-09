#Import all libs
from connect_db import connect_db
import pandas as pd
from pathlib import Path

#Database access informations
DB_CONFIG = {
    'host': 'db',
    'database': 'treated_db',
    'user': 'root',
    'user_pass': 'root'
}

#Initialize the connection script
connect_db = connect_db(host=DB_CONFIG['host'],
                        database=DB_CONFIG['database'],
                        user=DB_CONFIG['user'],
                        password=DB_CONFIG['user_pass'])

#Create a connection
cnx = connect_db.connect()

#Create a cursor to manipulate the database
cursor = cnx.cursor()

#Create engine for converting the csv file to a sql table.
engine = connect_db.create_engine()

#Open the csv file and pass it to a sql table
with open(Path("databases/weather_data.csv")) as file:
    csv_data = pd.read_csv(file)

    sql_data = csv_data.to_sql(name=f"{DB_CONFIG['database']}",
                               con=engine,
                               if_exists='replace',
                               chunksize=100)

cursor.execute(f"SELECT * FROM {DB_CONFIG['database']}")
result = cursor.fetchall()

print(result)