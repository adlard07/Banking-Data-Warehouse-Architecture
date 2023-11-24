import sys
from mysql import connector
from dataclasses import dataclass 

from exception import CustomException
from logger import logging

@dataclass
class ConnectDB:
  def __init__(self):  
    self.host = "localhost"
    self.user = "root"
    self.password = "adelard"
    self.database = "mybank"
    
  def connect_database(self):
    try:
      mydb = connector.connect(
        host = self.host,
        user = self.user,
        password = self.password,
        database = self.database
      )
      logging.info('Connection Established!')
      return mydb
    except Exception as e:
      raise CustomException(e, sys)
  
if __name__=="__main__":
  mydb = ConnectDB()
  connection = mydb.connect_database()
  print("Connection Established!")