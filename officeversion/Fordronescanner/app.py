#app.py
from flask import Flask, render_template, redirect, request, flash, jsonify
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
import mysql.connector

app = Flask(__name__)
       
app.secret_key = "caircocoders-ednalan"
       
# define database credentials
db_config = {
   'host': '127.0.0.1',
   'port': 3306,
  'user': 'root',
  'password': '1234',
  'database': 'dronescanner'
}

 
@app.route('/')
def index():
    cur = mysql.connector.connect(**db_config)
    cursor = cur.cursor(dictionary=True) 
    query = "SELECT * FROM informationdronenew"  # Replace 'your_table' with your actual table name
    cursor.execute(query)

# Fetch all rows as dictionaries
    employee = cursor.fetchall()
     
    # cur = mysql.connection.cursor()
    
    print("see all array ",employee)
    return render_template('index.html', employee=employee)
 
@app.route("/ajax_add",methods=["POST","GET"])
def ajax_add():
    
    cur = mysql.connector.connect(**db_config)
    mycursor = cur.cursor()
    if request.method == 'POST':
        txtMacAddress = request.form['txtMacAddress']
        txtLatitude = request.form['txtLatitude']
        txtLongitude = request.form['txtLongitude']
        txtAtitude = request.form['txtAtitude']
        txtHeight = request.form['txtHeight']
        txtdateandtime = request.form['txtdateandtime']

         
        if txtMacAddress == '':
            msg = 'Please Input MacAddress'  
        elif txtLatitude == '':
           msg = 'Please Input Latitude'  
        elif txtLongitude == '':
           msg = 'Please Input Longitude' 
        elif txtAtitude == '':
           msg = 'Please Input Latitude'  
        
        elif txtHeight == '':
           msg = 'Please Input Height'  
        elif txtdateandtime == '':
           msg = 'Please Input dateandtime'     
        else:        
            mycursor.execute("INSERT INTO informationdronenew (macaddress,Lat,Lon, Altitude, height, dateandtime) VALUES (%s,%s,%s,%s,%s,%s)",[txtMacAddress,txtLatitude,txtLongitude,txtAtitude,txtHeight,txtdateandtime])
            cur.commit()       
            mycursor.close()
            msg = 'New record created successfully'   
    return jsonify(msg)
 
@app.route("/ajax_update",methods=["POST","GET"])
def ajax_update():
     
    cur = mysql.connector.connect(**db_config)
    mycursor = cur.cursor()
    if request.method == 'POST':
        string = request.form['string']
        txtMacAddress = request.form['txtMacAddress']
        txtLatitude = request.form['txtLatitude']
        txtLongitude = request.form['txtLongitude']
        txtAtitude = request.form['txtAtitude']
        txtHeight = request.form['txtHeight']
        txtdateandtime = request.form['txtdateandtime']
        print("getID-------------------------------------------:", string)
        mycursor.execute("UPDATE informationdronenew SET macaddress = %s, Lat  = %s, Lon  = %s  , Altitude = %s , height = %s , dateandtime = %s WHERE ID = %s ", [txtMacAddress, txtLatitude, txtLongitude,txtAtitude,txtHeight,txtdateandtime, string])
        cur.commit()       
        mycursor.close()
        msg = 'Record successfully Updated'   
    return jsonify(msg)    


@app.route("/ajax_delete", methods=["POST"])
def ajax_delete():
    try:
        con = mysql.connector.connect(**db_config)
        cursor = con.cursor()

        if request.method == 'POST':
            getID = request.form['string']
            print("getID--------------------///////////:", getID)

            # Use parameterized query to prevent SQL injection
            delete_query = 'DELETE FROM informationdronenew WHERE ID = %s'
            cursor.execute(delete_query, (getID,))

            # Commit changes to the database
            con.commit()

            cursor.close()
            con.close()

            return "Deleted successfully"  # Return a success message

    except mysql.connector.Error as e:
        print("Error:", e)
        return "An error occurred while deleting data"  # Return an error message


if __name__ == "__main__":
    app.run(debug=True)