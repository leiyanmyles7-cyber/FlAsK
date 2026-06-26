from flask import*
import pymysql

# initialize the application
app=Flask(__name__)

# define the route/endpoint
@app.route("/api/signup",methods=["POST"])

# Define the function
def signup():

    # get user inputs from the form
    username=request.form["username"]
    email=request.form["email"]
    password=request.form["password"]
    phone=request.form["phone"]

    # connection to database
    connection=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="modcomfabian")
    
    # Define the cursor
    cursor=connection.cursor()

    # Define SQL to insert users
    sql="INSERT INTO users(username,password,email,phone) VALUES(%s,%s,%s,%s)"
    # define you data
    # NB: coming from step 3
    data=(username,password,email,phone)
    # execute/run query
    cursor.execute(sql,data)
    # commit/save changes
    connection.commit()
    return jsonify({"message":"user registration successfull"})

# Member signin/login
# Define the route/endpoint
@app.route("/api/signin",methods=["POST"])

# define the function
def signin():

   #get user inputs from the form 
   email=request.form["email"]
   password=request.form["password"]

   #connection to database 
   connection=pymysql.connect(
       host="localhost",
       user="root",
       password="",
       database="modcomfabian")
   
   #define the cursor
   cursor=connection.cursor(pymysql.cursors.DictCursor)    

   #define sql to select users
   sql="select * from users where email=%s and password=%s"    

  #define your data
  # NB;Coming from step 3
   data=(email,password)    

  #execute/run query    
   cursor.execute(sql,data)
   
  #wrong email and password
   if cursor.rowcount== 0:
       return jsonify({"message":"Invalid email or password"})    
  #correct email and password
   if cursor.rowcount==1:
    # fetch the user   
    user=cursor.fetchone()
    return jsonify({"message":"Login successful!","user":user})






















    # run the application 
app.run(debug=True)

        

    