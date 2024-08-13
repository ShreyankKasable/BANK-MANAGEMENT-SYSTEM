from Register import *

status = False
print("WELCOME TO OUR BANKING SYSTEM")

while True:
    try:
        register = int(input("PRESS \n"
                             "1. SignUp \n"
                             "2. SignIn"))

        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            elif register == 2:
                user = SignIn()
                status = True
                break
        else:
            print("Please Enter Valid Input Operation")
    except ValueError:
        print("InValid Input try Again with ")

account_num = db_query(f"SELECT account_no FROM customers WHERE username = '{user}';")

while status:
    print()
    print("--------------------------------------------------------")
    print(F"WELCOME {user.capitalize()} CHOOSE YOUR BANKING SERVICE")
    print("--------------------------------------------------------")
    print()

    try:
        facility = int(input(" \n"
                             "1. Balance Enquiry \n"
                             "2. Cash Deposit \n"
                             "3. Cash WithDraw \n"
                             "4. Fund Transfer \n"))

        if (register >= 1) and (register <= 4):
            if facility == 1:
                bobj = Bank(user, account_num[0][0])
                bobj.balanceEnquiry()

            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter the amount you want to deposit :- "))
                        bank_obj = Bank(user, account_num[0][0])
                        bank_obj.deposit(amount)
                        mydb.commit()

                        break
                    except ValueError:
                        print("Enter valid Receiver Account NUmber")
                        continue

            elif facility == 3:
                while True:
                    try:
                        bobj = Bank(user, account_num[0][0])
                        amount = int(input("Enter the amount you want to WithDraw :- "))
                        bobj.withDraw(amount)
                        mydb.commit()

                        break
                    except ValueError:
                        print("Enter valid Receiver Account NUmber")
                        continue

            elif facility == 4:
                while True:
                    try:
                        receive = int(input("Enter Receiver Account Number :- "))
                        amount = int(input("Enter the amount you want to Transfer :- "))

                        obj = Bank(user, account_num[0][0])
                        obj.fundTransfer(receive, amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter valid Receiver Account NUmber")
                        continue
        else:
            print("Please Enter Valid Input Operation")
            continue
    except ValueError:
        print("InValid Input try Again with Number")
        continue


