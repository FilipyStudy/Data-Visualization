#Import all libs
from connect_db import connect_db
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
#Database access informations
DB_CONFIG = {
    'host': 'db',
    'database': 'treated_db',
    'user': 'root',
    'user_pass': 'root'
}

#Create a date parser function 
def dateparser(s):
    return datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')

#Initialize the connection script
connect_db = connect_db(host=DB_CONFIG['host'],
                        database=DB_CONFIG['database'],
                        user=DB_CONFIG['user'],
                        password=DB_CONFIG['user_pass'])

#Create a connection
cnx = connect_db.connect()

#Initialize the classifier of the algorithm
clf = RandomForestClassifier(random_state=0)

#Create a cursor to manipulate the database
cursor = cnx.cursor()

#Create engine for converting the csv file to a sql table.
engine = connect_db.create_engine()

#Defining a new limit to call the blocks
mpl.rcParams['agg.path.chunksize'] = 10000

#Open the csv file and pass it to a sql table
with open(Path("databases/weather_data.csv")) as file:
    #Read the file, using a function to parse the date to correct format.
    csv_data = pd.read_csv(file, parse_dates=['Date_Time'], date_parser=dateparser)

    #Convert the file to a sql database and upload the data.
    sql_data = csv_data.to_sql(name=f"{DB_CONFIG['database']}",
                               con=engine,
                               if_exists='replace',
                               chunksize=100)
    #Read the sql table
    sql_data = pd.read_sql_table('test_db', engine)

y = sql_data.iloc[:,3:]
x = sql_data.iloc[:,4:]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

plt.scatter(x_test, y_test, color='red')
plt.plot(x_test, y_pred, color='blue', linewidth=2)
plt.show()