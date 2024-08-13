# USER REGISTRATION SIGNUP AND SIGNIN
import random
from Customer import *
from Database import *
from bank import *


def SignUp():
    username = input("CREATE USERNAME:- ")

    temp = db_query(f"SELECT USERNAME FROM CUSTOMERS WHERE USERNAME = '{username}';")

    if temp:
        print("USERNAME IS ALREADY EXIST !!PLEASE TRY WITH SOME OTHER USERNAME")
        SignUp()
    else:
        print("USERNAME IS AVAILABlE PLEASE PROCEED")
        password = input("Enter Your Password :- ")
        name = input("Enter Your Name :- ")
        age = input("Enter Your Age :- ")
        city = input("Enter Your City :- ")

        while True:
            account_number = int(random.randint(10000000, 999999999))
            temp = db_query(f"SELECT ACCOUNT_NO FROM CUSTOMERS WHERE ACCOUNT_NO = '{account_number}';")
            if temp:
                continue
            else:
                print(f"Your Account Number :- {account_number}")
                break
        # STORING DATA IN OUR DATABASE

    cust_obj = Customer(username, password, name, age, city, account_number)
    cust_obj.createUser()
    bank_obj = Bank(username, account_number)
    bank_obj.create_transaction_table()


def SignIn():
    username = input("ENTER USERNAME :- ")
    temp = db_query(f"SELECT USERNAME FROM CUSTOMERS WHERE USERNAME = '{username}';")

    if temp:
        while True:
            password = input("ENTER PASSWORD :- ")
            pwd = db_query(f"SELECT PASSWORD FROM CUSTOMERS WHERE USERNAME = '{username}';")

            if pwd[0][0] == password:
                print("SignIn SUCCESSFULLY")
                return username

            else:
                print("WRONG PASSWORD TRY AGAIN")
                continue

    else:
        print("Enter Valid UserName")
        SignIn()





