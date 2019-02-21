
#
from flask import Flask, render_template, request

app = Flask("MyFirstApp")#--> Flask object
@app.route("/")
def hello():
    return "<h1>Hello World</h1> <ul><li><a href=\"/morning\">Good Morning</a></li></ul><a href=\"style.css\"></a>"
#app.run(debug=True) 
#It will return a few instructions and among all of them, the most important is the URL (//127.0.0.1:5000/) if I copy and paste it on the browser I can see what I've just done typed between the parenthesis. I can print just a string, for example "Hello World" or direclty some html.

#
##-----------------------------------
## Task 2 - Use routes and decorators
##-----------------------------------
#
#from flask import Flask
#
#app = Flask("MyApp")
#
#@app.route("/morning")
#def morning():
#    return "<h1>Good Morning</h1>"
#
#@app.route("/afternoon")
#def afternoon():
#    return "<h1>Good Afternoon</h1>"
#
#@app.route("/night")
#def night():
#    return "<h1>Good Night</h1>"
#
#
##app.run(debug=True) 
#
#
#
##--------------------------------------------
## Task 3 - Using the render_template function
##--------------------------------------------
#
#from flask import Flask, render_template 
#
#app = Flask("MyApp")
#@app.route("/home")
#def homepage():
#    return render_template("templates/index.html")# Here I'm using an HTML file that in Flask is called template.
#
##app.run(debug=True) 
#
#
##----------------------------
## Task 4 - Using variables
##----------------------------
## Below an example of how a html looks like by using Jinja2
#
##<!DOCTYPE html>
##<html>
##  <head>
##    <title>My Flask App Page</title>
##    <link rel="stylesheet" href="{{ url_for("static", filename="css/style.css") }}">
##  </head>
##  <body>
##    {% if name %}
##      <p>Hello {{name}}!</p>
##    {% else %}
##      <p>Hello anonymus person!</p>
##    {% endif %}
##  </body>
##</html>
#
# #By using {% %} we can insert a variable coming from Python, that I'm setting below.
# 
# 
#from flask import Flask, render_template 
##
#app = Flask("MyApp")
#
#@app.route("/home2")
#def helloHello():
#    return "Hello World!"
#
#@app.route("/<name>")
#def helloSomeone(name):
#    return render_template("templates/index.html", name=name.title())# By doing this if I type any word or name after the URL created from Flask and visibile in the console, in the page on the browser I'll see the message: Hello Fabiana. This is because in the HTML page by using Jinja2 we're adding the parameter of the name typed in the address bar imported and used in the the HTML thanks to Jinja2
#
##app.run(debug=True) 
# 
# 
# #--------------------------------------
## Task 5 - Get email address from user
##---------------------------------------
# 
# #What to add in the HMTL file:
#
##  <p>Let's keep in touch!</p>
##  <div id="contact-form">
##    <form method="post" action="/signup">
##      <label for="email">Email address:</label>
##      <input type="email" id="email" name="email" required="required">
##      <input type="submit" id="submit-button" name="submit" value="Submit">
##    </form>
##  </div>



@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/confirmation", methods=["POST"])
def confirmation():
    form_data = request.form
    email = form_data["email"] #what I put in the [] is the attribute name I added in the form in about.hml 
    result = "All OK"
    return render_template("/confirmation.html", title="Form confirmation", **locals())#--> ** means that I can put as many arguments as I like without pre-set them.

app.run(debug=True) 