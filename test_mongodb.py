from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

try:
    client.admin.command("ping")
    print("MongoDB Atlas connection successful!")
except Exception as e:
    print("Connection failed:")
    print(e)