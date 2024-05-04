import mysql.connector
from .config import *
import pandas as pd


class MySQL_Database():
    def __init__(self, mode='read', env='dev'):
        conf = HOST_CONFIG[env]
        self.db_connection = mysql.connector.connect(
                                            host=conf['DATABASE'][mode]["HOST"],
                                            port=conf['DATABASE'][mode]["PORT"],
                                            user=conf['DATABASE'][mode]["USER"],
                                            password=conf['DATABASE'][mode]["PASSWORD"]
                                        )
    
    def execute_query(self, query, mode="read"):
        #Saving the Actions performed on the DB
        if mode=="read":
            result = pd.read_sql(query, self.db_connection)
        if mode=="write":
            #Creating a connection cursor
            cursor = self.db_connection.cursor()

            #Executing SQL Statements
            result = cursor.execute(query)
            self.db_connection.commit()

        # #Closing the cursor
        # cursor.close()
        return result
    
    def close_connection(self):
        self.db_connection.close()
