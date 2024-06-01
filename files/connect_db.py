from mysql import connector
from sqlalchemy import create_engine
class connect_db:
    #Contructor of the class
    def __init__(self, host, database, password, user):
        self.host = host
        self.database = database
        self.password = password
        self.user = user

    #Create and return a connection object to connect python to a database
    def connect(self):
        conn = connector.connect(host=self.host, 
                                 database=self.database,
                                 password = self.password,
                                 user=self.user)
        return conn
    
    #Create and return a cursor to modify and work over tables 
    def create_cursor(self):
        conn = connector.connect(host=self.host, 
                                 database=self.database,
                                 password = self.password,
                                 user=self.user)
        cursor = conn.cursor()
        return cursor
    
    #Check if the database is alive and accepting connections
    def check_connection(self):
        conn = connector.connect(host=self.host, 
                                 database=self.database,
                                 password = self.password,
                                 user=self.user)
        if(conn.is_connected()):
            #Return true if the script is connected to a database
            return True
        else:
            #Return false if the script is not connected to a database
            return False
    
    #Create and return a engine to work with pandas module
    @staticmethod    
    def create_engine():
        engine = create_engine("mysql://root:root@db/treated_db")
        return engine