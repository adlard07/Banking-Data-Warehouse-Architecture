import sys
import random
import numpy as np
import pandas as pd
from dataclasses import dataclass
from insert_into import PushData
from exception import CustomException


@dataclass
class CreateData:
    def __init__(self):
        self.cust_names = pd.read_csv('data/cust_names.txt', sep=' ', header=None, engine="python")
        self.banker_names = pd.read_csv('data/banker_names.txt', sep=', ', header=None, engine="python")
        
    def create_accounts(self):
        try:
            account_bal = np.random.randint(100000)
            account_types = ['savings', 'current', 'salary', 'checking', 'FD']
            acc_type = np.random.randint(5)
            account_type = account_types[acc_type]
            branch_id = np.random.randint(5000, 5002)
            return (
                account_bal,
                account_type,
                branch_id
                )
        except Exception as e:
            raise CustomException(e, sys)
    
    def create_customers(self):
        try:    
            self.cust_names.columns = ["first_name", "last_name"]
            first_name = list(self.cust_names["first_name"])
            last_name = list(self.cust_names["last_name"])
            fn = np.random.randint(len(first_name))
            ln = np.random.randint(len(last_name))
            customer_name = f"{first_name[fn]} {last_name[ln]}"
            fetch_data = PushData()
            table = fetch_data.fetch_table('Accounts')
            account_id = table[-1][0]
            y = np.random.randint(1960, 2005)
            m = np.random.randint(1, 13)
            d = np.random.randint(1, 30)
            dob = f"{y}-{m}-{d}"
            mobile_no = str(random.randint(9999999999,100000000000))
            return (
                customer_name, 
                account_id,
                dob, 
                mobile_no
                )
        except Exception as e:
            raise CustomException(e, sys)
        
    def create_banker(self):
        try:
            create_data = CreateData()
            _, _, branch_id = create_data.create_accounts()
            self.banker_names.columns = ["first_name", "last_name"]
            first_name = list(self.banker_names["first_name"])
            last_name = list(self.banker_names["last_name"])
            fn = np.random.randint(len(first_name))
            ln = np.random.randint(len(last_name))
            banker_name = f"{first_name[fn]} {last_name[ln]}"
            return (
                branch_id,
                banker_name
            )
        except Exception as e:
            raise CustomException(e, sys)
    
    def create_credit_card(self):
        try:
            card_no = str(random.randint(99999999999,999999999999))
            fetch_data = PushData()
            table = fetch_data.fetch_table('Customers')
            customer_id = table[-1][0]
            account_id = table[-1][2]
            exp_month = random.randint(1, 12)
            exp_year = random.randint(2023, 2028)
            card_limits = ['10000', '20000', '25000', '50000', '100000']
            limits = np.random.randint(5)
            card_limit = card_limits[limits]
            return (
                card_no, 
                customer_id,
                account_id,
                exp_month, 
                exp_year, 
                card_limit
                )
        except Exception as e:
            raise CustomException(e, sys)
        
    def create_loan(self):
        try:
            zeros = '000'
            number = random.randint(1, 100)
            issued_amount = f'{number}{zeros}'
            create_data = CreateData()
            _, _, branch_id = create_data.create_accounts()
            fetch_data = PushData()
            table = fetch_data.fetch_table('Accounts')
            account_id = table[-1][0]
            return (
                issued_amount,
                branch_id,
                account_id,
                )
        except Exception as e:
            raise CustomException(e, sys)
            
    
    def create_loan_payment(self):
        try:
            fetch_data = PushData()
            table = fetch_data.fetch_table('Loan')
            loan_id = table[-1][0]
            zeros = '00'
            number = random.randint(1, 1000)
            amount = f'{number}{zeros}'
            return (
                loan_id,
                amount
            )
        except Exception as e:
            raise CustomException(e, sys)
            
    
if __name__=="__main__":
    create_data = CreateData()
    accounts = f"{create_data.create_accounts()}"
    customers = f"{create_data.create_customers()}"
    banker = f"{create_data.create_banker()}"
    creditcard = f"{create_data.create_credit_card()}"
    loan = f"{create_data.create_loan()}"
    loanpayment = f"{create_data.create_loan_payment()}"
    print(
        accounts,'\n', 
        customers,'\n',
        banker, '\n',
        creditcard, '\n',
        loan, '\n',
        loanpayment
        )