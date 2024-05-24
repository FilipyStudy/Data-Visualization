import pandas as pd
import subprocess
import os

SOURCE_DB = {
    'USER': 'postgres',
    'PASSWORD': 'secret',
    'HOST': 'destination_db'
}
databasePath = "database"

if os.path.exists(databasePath):
    with open (os.path.join(databasePath, "weather_data.csv")) as file:
        csv_database = pd.read_csv(file)
else:
    print("The database path was not found.")
    exit()

df_database = csv_database.to_sql()

print(df_database.head())