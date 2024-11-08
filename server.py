from flask import Flask
import json

app = Flask(__name__)

@app.get("/") #this is home page
def home():    #perform this function if someone tries to get from home page
    return "hello from flask"

# Endpoints
@app.get("/test") #specifies the url page your trying to access
def test():
    return "hello from the test server"

# Endpoint using json
@app.get("/api/about")
def aboutGet():
    name = {"name": "Kendall"}
    return json.dumps(name)

#Create New Route /greet/{name}, this rout should accept name
# as part of the url and return an html message saying hello {name}

@app.get("/greet/<name>")
def greet(name):
    return f"""
<h1 style=color:blue>Hello {name}!</h1>"""

#Create a farewell message

@app.get("/farewell/<name>")
def farewell(name):
    return f"""
<h1 style=color:blue>Get From Yah {name}!</h1>"""

app.run(debug=True)