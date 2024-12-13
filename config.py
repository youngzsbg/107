import pymongo
import certifi

con_string = "mongodb+srv://youngzsbg:test@fsdi-flaskdata-107.k5qb3.mongodb.net/?retryWrites=true&w=majority&appName=FSDI-flaskdata-107"

client = pymongo.MongoClient(con_string, tlsCAFile=certifi.where())
db = client.get_database("organika2")