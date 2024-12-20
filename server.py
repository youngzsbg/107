from flask import Flask, request, abort
import json
from config import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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


################################

#get

products = []

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.get("/api/products")
def get_products():
    products_db = []
    cursor = db.products.find({})
    for prod in cursor:
        if "title" in prod:
            products_db.append(fix_id(prod))
    return json.dumps(products_db)

#post

@app.post("/api/products")
def save_products():
    item = request.get_json()
    print(item)
    #products.append(item)
    db.products.insert_one(item)
    return json.dumps(fix_id(item))


#put

@app.put("/api/products/<int:index>")
def update_products(index):
    updated_item=request.get_json()
    if 0<= index <=len(products):
        products[index] = updated_item
        return json.dumps(updated_item)
    else:
        return "That index does not exist"
    
#delete

@app.delete("/api/products/<int:index>")
def delete_products(index):
    delete_item = request.get_json()
    if 0<= index <=len(products):
        delete_item = products.pop(index)
        return json.dumps(delete_item)
    else:
        return "That index does not exist"

# patch the method to update a specific element into python is: list.update

@app.patch("/api/products/<int:index>")
def patch_products(index):
    updated_field = request.get_json()
    if 0<= index <=len(products):
        updated_field(index).update(updated_field)
        return json.dumps(updated_field)
    else:
        return "That index does not exist"
#########################################################################
################# COUPONS#############################

@app.post("/api/coupons")
def save_coupon():
    item = request.get_json()
    db.coupons.insert_one(item)
    return json.dumps(fix_id(item))

@app.get("/api/coupons")
def get_coupons():
    coupons = []
    cursor = db.coupons.find({})
    for cp in cursor:
        coupons.append(fix_id(cp))
    return json.dumps(coupons)

@app.get("/api/coupons/<code>")
def validate_coupon(code):
    coupon = db.coupons.find_one({"code": code})
    if coupon == None:
        print("Error: invalid coupon")
        return abort(404, "Invalid Code")
    
    return json.dumps(fix_id(coupon))




app.run(debug=True)