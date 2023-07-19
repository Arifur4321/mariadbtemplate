from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# define database credentials
db_config = {
   'host': '192.168.54.206',
   'port': 3307,
  'user': 'root',
  'password': '1234',
  'database': 'dronescanner'
}


@app.route('/')
def index():
 
  return render_template("index.html")

@app.route("/results", methods=['POST'])
def results():
  # get input from user for date interval
  start_date = request.form['start_date']
  end_date = request.form['end_date']

  # connect to the database and execute query with date interval filter
  mydb = mysql.connector.connect(**db_config)
  mycursor = mydb.cursor()
  sql = "SELECT * FROM informationdrone WHERE dateandtime BETWEEN %s AND %s"
  params = (start_date, end_date)
  mycursor.execute(sql, params)

  # get the results and render them in an HTML table
  data = mycursor.fetchall()
  return render_template("results.html", data=data)

if __name__ == '__main__':
  app.run(debug=True)