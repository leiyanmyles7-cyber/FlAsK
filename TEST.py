from flask import*
# initialize the application
app=Flask(__name__)
# Define route/end point
@app.route("/api/home")
# define the function
def home():
    return jsonify({"message":"welcome home"})



@app.route("/api/services")
def services():
    return jsonify({"message":"welcome to services"})

@app.route("/api/about")
def about():
    return jsonify({"message":"welcome to about"})

@app.route("/api/contact")
def contact():
    return jsonify({"message":"Contact us for more information"})

@app.route("/api/products")
def contacts():
    return jsonify({"message":"Products available"})

@app.route("/api/students")
def students():
    return jsonify({"message":"list of students"})

@app.route("/api/courses")
def courses():
    return jsonify({"message":"Courses offered"})
    
@app.route("/api/teachers")    
def teachers():
    return jsonify({"message":"List of teachers"})

@app.route("/api/news")
def news():
    return jsonify({"message":"Latest news"})

@app.route("/api/gallery")
def gallery():
    return jsonify({"message":"Gallery images"})

@app.route("/api/faq")
def faq():
    return jsonify({"message":"Frequently asked questions"})

@app.route("/api/profile")
def profile():
    return jsonify({"message":"student profile information"})
# run the application
app.run(debug=True)
                    

