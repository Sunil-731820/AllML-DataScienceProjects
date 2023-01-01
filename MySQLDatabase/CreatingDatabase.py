import mysql.connector

# Creating the connection object
conn_obj = mysql.connector.connect(host="localhost", user="root", passwd="root")

# creating the cursor object
cur_obj = conn_obj.cursor()

try:
    # creating a new database using query
    cur_obj.execute("create database New_PythonDB")

    # getting the list of all the databases which will now include the new database New_PythonDB
    dbms = cur_obj.execute("show databases")

except:
    conn_obj.rollback()  # it is used if the operation is failed then it will not reflect in your database

for x in cur_obj:
    print(x)

conn_obj.close()