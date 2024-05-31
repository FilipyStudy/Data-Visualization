from mysql import connector

class connect_db:
    #Contructor of the class
    def __init__(self, host, database, password, port):
        self.host = host
        self.database = database
        self.password = password
        self.port = port

    #Create and return a connection object to connect python to a database
    def connect(self):
        conn = connector.connect(host=self.host, 
                                 database=self.database,
                                 password = self.password,
                                 port=self.password)
        return conn
    
    #Create and return a cursor to modify and work over tables 
    def create_cursor(self):
        conn = connector.connect(host=self.host, 
                                 database=self.database,
                                 password = self.password,
                                 port=self.password)
        cursor = conn.cursor()
        return cursor
    
    #Check if the database is alive and accepting connections
    def check_connection(self):
        conn = connector.connect(host=self.host, 
                                 database=self.database,
                                 password = self.password,
                                 port=self.password)
        if(conn.is_connected()):
            #Return true if the script is connected to a database
            return True
        else:
            #Return false if the script is not connected to a database
            return False