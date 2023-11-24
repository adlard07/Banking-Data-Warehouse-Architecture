import sys
from dataclasses import dataclass 

from connect_mysql import ConnectDB
from exception import CustomException

@dataclass
class PushData:
    def __init__(self):
        connect_db = ConnectDB()
        self.connection = connect_db.connect_database()
        self.query = "USE mybank;"
        self.cursor = self.connection.cursor()
        if self.connection.is_connected():
            self.db_Info = self.connection.get_server_info()
            self.cursor = self.connection.cursor()
            self.cursor.execute(self.query)         
            self.connection.commit()
        
    
    def fetch_table(self, table_name):
        try:
            query = f"SELECT * FROM {table_name}"
            self.cursor.execute(query)
            table = self.cursor.fetchall()
            self.connection.close()
            return table
        except Exception as e:
            raise CustomException(e, sys)
        
    def create_table(self, table_name, column_names):
        try:
            query = f'''CREATE TABLE {table_name}({column_names});'''
            
            self.cursor.execute(query)            
            self.connection.commit()
            self.connection.close()
            print("Table created!")
        except Exception as e:
            raise CustomException(e, sys)
        
        
    def insert_values(self, table_name, column_names, values):
        try:
            query = f"INSERT INTO {table_name} ({column_names}) VALUES {values}"
            self.cursor.execute(query)           
            self.connection.commit()

            self.cursor.execute(f"SELECT * FROM {table_name}")
            table = self.cursor.fetchall()
            self.connection.close()
            
            return table
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=="__main__":
    table_name = 'Account'
    column_names = "account_bal, account_type, branch_id"
    values = "'100000','FD', 5000"
    fetch_data = PushData()
    table = fetch_data.fetch_table(table_name)
    print(table)