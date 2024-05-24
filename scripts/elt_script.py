import pandas as pd
import subprocess
import os

SOURCE_DB = {
    'USER': 'postgres',
    'PASSWORD': 'secret',
    'HOST': 'destination_db'
}

csv_database = pd.read_csv(os.path.join("database", "weather_data.csv"))
df_database = csv_database.to_sql()

print(df_database.head())