from connect_db import connect_db

#Database access informations
DB_CONFIG = {
    'host': 'localhost',
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
cnx = connect_db.connect

#Create a cursor to manipulate the database
cursor = connect_db.create_cursor