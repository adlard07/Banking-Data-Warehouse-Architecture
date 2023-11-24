import sys
from insert_into import PushData
from get_data import CreateData
from exception import CustomException

create_data = CreateData()
fetch_data = PushData()

try:
    try:
        # Create Accounts
        account = create_data.create_accounts()
        # print(str(account))
    except Exception as e:
        raise CustomException(e, sys)

    try:
        # Create Customers
        customer = create_data.create_customers()
        # print(str(customer))
    except Exception as e:
        raise CustomException(e, sys)

    try:
        # Create Banker
        banker = create_data.create_banker()
        # print(str(banker))
    except Exception as e:
        raise CustomException(e, sys)

    try:
        # Create Credit Card
        creditcard = create_data.create_credit_card()
        # print(str(creditcard))
    except Exception as e:
        raise CustomException(e, sys)

    try:
        # Create Loan
        loan = create_data.create_loan()
        # print(str(loan))
    except Exception as e:
        raise CustomException(e, sys)

    try:
        # Create Loanpayment
        loanpayment = create_data.create_loan_payment()
        # print(str(loanpayment))
    except Exception as e:
        raise CustomException(e, sys)
    
except Exception as e:
    raise CustomException(e, sys)


# class DataIngestion:
#     def push_into_db(self, account, customer, banker, creditcard, loan, loanpayment):
#         try:

try:
    table_name = "Banker"
    column_names = "branch_id, banker_name"
    values = f"{banker}"
    banker_table = fetch_data.insert_values(table_name, column_names, values)
    print(banker_table)

    table_name = "Accounts"
    column_names = "account_bal, account_type, branch_id"
    values = f"{account}"
    account_table = fetch_data.insert_values(table_name, column_names, values)
    print(account_table)

    table_name = "Customers"
    column_names = "customer_name, account_id, DOB, mobile_no"
    values = f"{customer}"
    customer_table = fetch_data.insert_values(table_name, column_names, values)
    print(customer_table)

    table_name = "Loan"
    column_names = "issued_amount, branch_id, account_id"
    values = f"{loan}"
    loan_table = fetch_data.insert_values(table_name, column_names, values)
    print(loan_table)

    table_name = "LoanPayment"
    column_names = "loan_id, amount"
    values = f"{loanpayment}"
    loanpayment_table = fetch_data.insert_values(table_name, column_names, values)
    print(loanpayment_table)
    
    table_name = "CreditCard"
    column_names = "card_no, customer_id, account_id, exp_month, exp_year, card_limit"
    values = f"{creditcard}"
    creditcard_table = fetch_data.insert_values(table_name, column_names, values)
    print(creditcard_table)
    
except Exception as e:
    raise CustomException(e, sys)
            
#             return(
#                 account_table,
#                 customer_table,
#                 banker_table,
#                 creditcard_table,
#                 loan_table,
#                 loanpayment_table
#                 )
            
#         except Exception as e:
#             raise CustomException(e, sys)
        
# if __name__=="__main__":
#     data_ingestion = DataIngestion()
#     account_table, customer_table, banker_table, creditcard_table, loan_table, loanpayment_table = data_ingestion.push_into_db(account, customer, banker, creditcard, loan, loanpayment)
#     print(account_table)