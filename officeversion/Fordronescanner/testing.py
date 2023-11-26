import mysql.connector

# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host= '127.0.0.1',
   port= 3306,
  user= 'root',
  password= '1234',
  database= 'dronescanner'
)

 

# Create a cursor object to interact with the database
cursor = conn.cursor(dictionary=True)  # Setting dictionary=True to fetch rows as dictionaries

# Query to fetch data from a specific table
query = "SELECT * FROM informationdronenew"  # Replace 'your_table' with your actual table name
cursor.execute(query)

# Fetch all rows as dictionaries
result = cursor.fetchall()

# Print the fetched data
for row in result:
    print(row)

# Close cursor and connection
cursor.close()
conn.close()