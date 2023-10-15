import mysql.connector

# Connecting from the server
conn = mysql.connector.connect(user='root',
                                password="root",
                                host='localhost',
                                database='AllDataSetsForDataScience')

print(conn)

# Disconnecting from the server
conn.close()