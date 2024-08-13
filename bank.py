from Database import *
import datetime


class Bank:

    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number

    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__account_number}_transaction"
                 f"(timeDate VARCHAR(30),"
                 f"account_number INTEGER,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER,"
                 f"balance INTEGER)")

    def deposit(self, amount):
        remain_amount = db_query(f"SELECT BALANCE FROM customers "
                                 f"WHERE USERNAME = '{self.__username}';")
        current_balance = remain_amount[0][0]
        new_balance = current_balance + amount
        db_query(f"UPDATE customers SET balance = {new_balance} "
                 f"WHERE USERNAME = '{self.__username}';")
        self.balanceEnquiry()
        db_query(f"INSERT INTO {self.__account_number}_transaction "
                 f"VALUES ('{datetime.datetime.now()}', '{self.__account_number}', 'Amount Deposit', {amount}, {new_balance});")

        print(f"{self.__username} AMOUNT OF {amount} SUCCESSFULLY DEPOSITED IN YOUR ACCOUNT {self.__account_number} ")
        mydb.commit()

    def balanceEnquiry(self):
        temp = db_query(f"SELECT balance FROM customers "
                        f"WHERE USERNAME = '{self.__username}'")
        print("--------------------------------------------")
        print(f"{self.__username} BALANCE is {temp[0][0]}")
        print("--------------------------------------------")

    def withDraw(self, amount):
        remain_amount = db_query(f"SELECT BALANCE FROM customers "
                                 f"WHERE USERNAME = '{self.__username}';")
        if amount > remain_amount[0][0]:
            print("-----------------------------------------------------")
            print("UFF! INSUFFICIENT BALANCE WE CAN'T PROCEED FURTHER  |")
            print("-----------------------------------------------------")

        else:
            current_balance = remain_amount[0][0]
            new_balance = current_balance - amount
            db_query(f"UPDATE customers SET balance = {new_balance} "
                     f"WHERE USERNAME = '{self.__username}';")
            self.balanceEnquiry()
            db_query(f"INSERT INTO {self.__account_number}_transaction "
                     f"VALUES ('{datetime.datetime.now()}', '{self.__account_number}', 'Amount WithDraw', {amount}, {new_balance});")
            mydb.commit()
            print(f"{self.__username} AMOUNT OF {amount} SUCCESSFULLY WITHDRAW FROM YOUR ACCOUNT {self.__account_number} ")

    # FUNCTION TO TRANSFER FUNDS
    def fundTransfer(self, rec_acc_no, amount):
        # Fetch sender's current balance
        sender_current_amount = db_query(f"SELECT BALANCE FROM customers "
                                         f"WHERE USERNAME = '{self.__username}';")
        if not sender_current_amount:
            print(f"Error: Sender '{self.__username}' does not exist.")
            return

        if amount > sender_current_amount[0][0]:
            print("-----------------------------------------------------")
            print("UFF! INSUFFICIENT BALANCE WE CAN'T PROCEED FURTHER  |")
            print("-----------------------------------------------------")
        else:
            current_balance1 = sender_current_amount[0][0]
            new_balance1 = current_balance1 - amount

            # Fetch receiver's current balance using the correct column (assuming account number)
            receiver_current_amount = db_query(f"SELECT BALANCE FROM customers "
                                               f"WHERE account_no = '{rec_acc_no}';")
            if not receiver_current_amount:
                print(f"Error: Receiver with account number '{rec_acc_no}' does not exist.")
                return

            current_balance2 = receiver_current_amount[0][0]
            new_balance2 = current_balance2 + amount

            # Update receiver's balance
            db_query(f"UPDATE customers SET BALANCE = {new_balance2} "
                     f"WHERE account_no = {rec_acc_no};")

            # Update sender's balance
            db_query(f"UPDATE customers SET BALANCE = {new_balance1} "
                     f"WHERE USERNAME = '{self.__username}';")

            self.balanceEnquiry()

            # Log the transaction for both sender and receiver
            db_query(f"INSERT INTO {self.__account_number}_transaction "
                     f"VALUES ('{datetime.datetime.now()}', '{self.__account_number}', 'Fund Transfer {rec_acc_no}', {amount}, {new_balance1});")

            db_query(f"INSERT INTO {rec_acc_no}_transaction "
                     f"VALUES ('{datetime.datetime.now()}', '{rec_acc_no}', 'Fund Receive {self.__account_number}', {amount}, {new_balance2});")

            print()
            print(
                f"{self.__username} AMOUNT OF {amount} SUCCESSFULLY TRANSFERRED FROM YOUR ACCOUNT {self.__account_number}")

