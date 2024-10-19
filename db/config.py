from flask_pymongo import PyMongo

class Config:
    MONGO_URI = "mongodb+srv://azam:mypassword@cluster0.fgi93.mongodb.net/portfolio"

mongo = PyMongo()