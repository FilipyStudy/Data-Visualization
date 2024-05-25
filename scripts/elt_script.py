import pandas as pd
import subprocess, os, psycopg2, time

for i in range(16):
    counter = 1
    print(f"Waiting every module goes on. Time passed: {counter}")
    counter += 1
    time.sleep(1)

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

def wait_ps(max_tries = 5):
    retries = 0
    result = subprocess.run(
        ['pg_isready', '-h', SOURCE_DB['host']],
        check=True,
        capture_output=True,
        text=True
    )
    while retries < 5:
        if 'accepting connections' in result.stdout:
            return True
        else:
            retries += 1
            time.sleep(2)
    return False

CONN_SOURCE = psycopg2.connect(host = SOURCE_DB['HOST'], 
                               database = 'source_db', 
                               user = SOURCE_DB['USER'], 
                               password = SOURCE_DB['PASSWORD'])

if os.path.exists("database"):
    with open (os.path.join("database", "weather_data.csv")) as file:
        csv_database = pd.read_csv(file)

if (wait_ps()):
    source_database = csv_database.to_sql('source_db', 
                                           CONN_SOURCE, 
                                           if_exists='replace')
else:
    print("The database path was not found.")
    exit()

print(source_database.head())