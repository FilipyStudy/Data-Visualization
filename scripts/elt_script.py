import pandas as pd
import subprocess
import os

SOURCE_DB = {
    'USER': 'postgres',
    'PASSWORD': 'secret',
    'HOST': 'source_db'
}
DESTINATION_DB = {
    'USER': 'postgres',
    'PASSWORD': 'secret',
    'HOST': 'destination_db'
}

if os.path.exists("database"):
    with open (os.path.join("database", "weather_data.csv")) as file:
        csv_database = pd.read_csv(file)
else:
    print("The database path was not found.")
    exit()

print(csv_database.head())