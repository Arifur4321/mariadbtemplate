#app.py
from flask import Flask, render_template, redirect, request, flash, jsonify
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
 
app = Flask(__name__)
       
app.secret_key = "caircocoders-ednalan"
       
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'dronescanner'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
 
@app.route('/')
def index():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    result = cur.execute("SELECT * FROM informationdrone ORDER BY ID")
    employee = cur.fetchall()
    print("see all array ",employee)
    return render_template('index.html', employee=employee)
 
@app.route("/ajax_add",methods=["POST","GET"])
def ajax_add():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
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
            cur.execute("INSERT INTO informationdrone (MacAddress,Latitude,Longitude, Atitude, Height, dateandtime) VALUES (%s,%s,%s,%s,%s,%s)",[txtMacAddress,txtLatitude,txtLongitude,txtAtitude,txtHeight,txtdateandtime])
            mysql.connection.commit()       
            cur.close()
            msg = 'New record created successfully'   
    return jsonify(msg)
 
@app.route("/ajax_update",methods=["POST","GET"])
def ajax_update():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        string = request.form['string']
        txtMacAddress = request.form['txtMacAddress']
        txtLatitude = request.form['txtLatitude']
        txtLongitude = request.form['txtLongitude']
        txtAtitude = request.form['txtAtitude']
        txtHeight = request.form['txtHeight']
        txtdateandtime = request.form['txtdateandtime']
        print(string)
        cur.execute("UPDATE informationdrone SET MacAddress = %s, Latitude = %s, Longitude = %s  , Atitude = %s , Height = %s , dateandtime = %s WHERE ID = %s ", [txtMacAddress, txtLatitude, txtLongitude,txtAtitude,txtHeight,txtdateandtime, string])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record successfully Updated'   
    return jsonify(msg)    


@app.route("/ajax_delete",methods=["POST","GET"])
def ajax_delete():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getID = request.form['string']
        print(getID)
        cur.execute('DELETE FROM informationdrone WHERE ID = {0}'.format(getID))
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'   
    return jsonify(msg) 
     
if __name__ == "__main__":
    app.run(debug=True)