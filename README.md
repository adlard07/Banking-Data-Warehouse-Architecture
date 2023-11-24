# Banking Database Architecture Design

## Overview

This project involves the design and implementation of a relational database for a banking system. The database encompasses several tables to store essential information related to customers, accounts, branches, bankers, credit cards, loans, and loan payments. Additionally, a script has been developed to generate random data for testing and demonstration purposes.

## Tables

1. **Branch Table**
    - `branch_id`: Unique identifier for each branch.
    - `branch_name`: Name of the branch.
    - `branch_addr`: Address of the branch.

    ```bash
    create table branch(branch_id int, branch_name varchar(40), branch_adr varchar(40));
    ```


2. **Banker Table**
    - `banker_id`: Unique identifier for each banker.
    - `branch_id`: Foreign key referencing the Branch table.
    - `banker_name`: Full name of the banker.

    ```bash
    create table banker(banker_id int primary key auto_increment, branch_id int, banker_name varchar(20), foreign key (branch_id) references branch(branch_id));
    ```

3. **Account Table**
    - `account_id`: Unique identifier for each account.
    - `account_bal`: Current balance in the account.
    - `account_type`: Type of the account (e.g., savings, checking).
    - `branch_id`: Foreign key referencing the Branch table.

    ```bash
    create table accounts(account_id int primary key auto_increment, account_bal varchar(20), account_type varchar(20), branch_id int, foreign key (branch_id) references branch(branch_id));
    ```


4. **Customer Table**
    - `customer_id`: Unique identifier for each customer.
    - `customer_name`: Full name of the customer.
    - `account_id`: Foreign key referencing the Account table.
    - `dob`: Date of birth of the customer.
    - `mobile_no`: Mobile phone number of the customer.

       ```bash
       create table customers(customer_id int primary key auto_increment, customer_name varchar(20), account_id int, DOB date, mobile_no varchar(20), foreign key (account_id) references accounts(account_id));
       ```



5. **Credit Card Table**
    - `card_no`: Unique identifier for each credit card.
    - `customer_id`: Foreign key referencing the Customer table.
    - `account_id`: Foreign key referencing the Account table.
    - `exp_date`: Expiry date of the credit card.
    - `card_limit`: Credit limit assigned to the card.

    ```bash
    create table creditcard(card_id int primary key auto_increment, card_no varchar(20), customer_id int, account_id int, exp_month varchar(3), exp_year varchar(5), card_limit varchar(20), foreign key (customer_id) references customers(customer_id), foreign key (account_id) references accounts(account_id));
    ```


6. **Loan Table**
    - `loan_id`: Unique identifier for each loan.
    - `issued_amount`: Amount issued for the loan.
    - `branch_id`: Foreign key referencing the Branch table.
    - `account_id`: Foreign key referencing the Account table.
    
    ```bash
    create table loan(loan_id int primary key auto_increment, issued_amount varchar(20), account_id int, branch_id int, foreign key (account_id) references accounts(account_id), foreign key (branch_id) references branch(branch_id));
    ```


7. **Loan Payment Table**
    - `loan_payment_id`: Unique identifier for each loan payment.
    - `loan_id`: Foreign key referencing the Loan table.
    - `amount`: Amount paid towards the loan.
    
    ```bash
    create table loanpayment(loan_payment_id int primary key auto_increment, loan_id int, amount varchar(20), foreign key (loan_id) references loan(loan_id));
    ```


## Database Script

The provided script generates random data for each table, allowing for the population of the database with diverse and representative information. The script can be used for testing, development, and demonstration purposes.

## Generating Random Data

To generate random data for the tables, follow these steps:

1. Open a terminal in the project directory.

2. Run the script to generate random data using the provided commands:

   ```bash
   python -m src.ingestion
   ```

   The script will prompt you for the number of records to generate and then populate the tables with randomly generated data.

## Note

Ensure that you have the necessary dependencies installed and a connection to the database established before running the script. Modify the script or database connection details if needed.

Feel free to explore and extend the database schema or adapt the script based on project requirements.

## Usage

1. **Database Creation:**
   - Execute the script to create the necessary tables and relationships in your MySQL database.

2. **Data Generation:**
   - Run the script to populate the tables with random data.

3. **Customization:**
   - Adjust the script or the database schema according to specific project requirements.

## Dependencies

- MySQL Database Server

## References
- A reference ER table diagram is available for reference purposes

## Contributors

- Adelard Dcunha

Feel free to contribute, report issues, or suggest improvements.

Happy Banking! 🏦