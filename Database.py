import mysql.connector as sql

mydb = sql.connect(
    host="127.0.0.1",
    user='root',
    passwd='Shreyank@sk5',
    database='BANK_MANAGEMENT'
)

cursor = mydb.cursor()


def db_query(s):
    cursor.execute(s)
    result = cursor.fetchall()
    return result


def createCustomerTable():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS CUSTOMERS(
                    USERNAME VARCHAR(20),
                    PASSWORD VARCHAR(20),
                    NAME VARCHAR(20),
                    AGE INT,
                    CITY VARCHAR(20),
                    BALANCE INT,
                    ACCOUNT_NO INT,

                    STATUS BOOLEAN
                );
    ''')

mydb.commit()

if __name__ == '__main__':
    createCustomerTable()


