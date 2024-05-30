import pandas as pd
import subprocess, os, time, sqlalchemy
from mysql import connector

#Create a dict structure with informations about the database service/process
DB = {
    'USER': 'root',
    'PASSWORD': 'password',
    'DATABASE': 'db',
    'HOST': 'localhost'
}

#Check if the database service is alive to proceed, if not the function will trie 5 times until the process start.
def check_db():
    ping_db = subprocess.run(["mysqladmin" ,"ping", f"-p{DB['PASSWORD']}"],
                             capture_output=True,
                             text=True)
    print(f"First check: {ping_db.stdout}")
    print(f"First check error: {ping_db.stderr}")
    if ('mysqld is alive' in ping_db.stdout):
        return True
    else:
        retries = 0
        while ('mysqld is alive' not in ping_db.stdout and retries <= 5):
            print(f"Retrying to see the running status of the database for the {retries + 1} time.")
            time.sleep(5) #Wait 5 seconds to check again.
            ping_db = subprocess.run(['mysqladmin' ,'ping', f"-p{DB['PASSWORD']}"], 
                        capture_output=True,
                        text=True)
            retries += 1
            print(f"Retry output: {ping_db.stdout}")
            print(f"Retry output erro: {ping_db.stderr}")
        if ('mysqld is alive' in ping_db.stdout):
            return True
        else:
            return False
    
if (os.path.exists("database")):
    with open (os.path.join("database", "weather_data.csv")) as file:
        csv_database = pd.read_csv(file)
        print("CSV file are ready.")
else: 
    print('Database path was not found.')


#Return a cursor object to manipulate the database.
def create_cursor():
    if (check_db()):
        conn = connector.Connect(host=DB['HOST'],
                                user=DB['USER'],
                                password=DB['PASSWORD'])
        #Create a engine to insert the data into a mysql table with pandas module.
        ENGINE = sqlalchemy.create_engine(f'mysql://{DB['USER']}:{DB["PASSWORD"]}@{DB["HOST"]}')
        csv_database.to_sql(DB['DATABASE'], ENGINE, if_exists='replace')
        print('Database connected and cursor created.')
        cursor = conn.cursor()
        return cursor
    else:
        print("The database was not running properly.")

#Just for test purposes.
cursor = create_cursor()
cursor.execute('SELECT * FROM db')
cursor.fetchall
print(cursor.head())

#TODO: Transform and Load process of the data.